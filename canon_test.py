import sys
import numpy as np
import CanonLib
from ui_canon_test import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
from turbojpeg import TurboJPEG
jpeg = TurboJPEG("turbojpeg.dll")
from ThorlabsKST101 import *
from threading import Timer
import extraLib

global liveImage
global Z_axis, pos_Z


class GUIMainWindow(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_image_show.setScaledContents(True)
        self.show()
        self.init_UI()

        Z_axis = Motor('26000236')
        Z_axis.connect()
        time.sleep(0.5)
        Z_axis.set_vel_params(100000, 1000000)
        Z_axis.start_polling(50)

        def on_timer():
            while True:
                time.sleep(0.05)
                self.position_refresh()
        t = Timer(3, on_timer)  # Quit after 5 seconds
        t.start()

        self.pushButton_up.pressed.connect(lambda: Z_axis.move_at_velocity(1))
        self.pushButton_up.released.connect(lambda: Z_axis.stop_profiled())

        self.pushButton_down.pressed.connect(lambda: Z_axis.move_at_velocity(2))
        self.pushButton_down.released.connect(lambda: Z_axis.stop_profiled())



        self.pushButton_camera.setText('Camera')


        self.camera = CameraThread()
        self.camera_Thread = QtCore.QThread()
        self.camera.moveToThread(self.camera_Thread)
        self.camera_Thread.started.connect(self.camera.work)
        self.camera.stop_signal.connect(self.stop_camera_Thread)

        self.camera.CameraSignal.connect(self.camera_show)

        self.autoFocus = AutoFocusThread()
        self.autoFocus_Thread = QtCore.QThread()
        self.autoFocus.moveToThread(self.autoFocus_Thread)
        self.autoFocus_Thread.started.connect(self.autoFocus.work)
        self.pushButton_autoFocus.clicked.connect(self.autoFocus_Thread.start)
        self.autoFocus.stop_signal.connect(self.autoFocus_Thread.quit)


    def stop_camera_Thread(self):
        self.camera_Thread.quit()


    def position_refresh(self):
        global Z_axis
        self.label_position.setText(str(Z_axis.get_position()))



    def init_UI(self):
        self.pushButton_camera.clicked.connect(self.camera_task)
        self.pushButton_capture.clicked.connect(self.camera_capture)
        # self.pushButton_autoFocus.clicked.connect(self.autoFocus_Thread.start)

    def camera_task(self):
        if self.pushButton_camera.isChecked():
            self.pushButton_camera.setText('Camera ON')
            self.camera.flag = True
            self.camera_Thread.start()

        else:
            self.pushButton_camera.setText('Camera')
            self.camera.flag = False

    def camera_capture(self):
        self.camera.flag = False
        time.sleep(0.5)
        self.camera.cameraObject.set_Capture_ready()
        self.camera.cameraObject.get_Capture_image()
        time.sleep(3)
        print(self.camera_Thread.isFinished())
        self.camera.flag = True
        self.camera_Thread.start()


    def camera_show(self, image):
        global liveImage, pos_Z, Z_axis
        frame = jpeg.decode(image)
        liveImage = frame
        pos_Z = Z_axis.get_position()
        # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        Qimg = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        Qimg = Qimg.rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(Qimg)
        self.label_image_show.setPixmap(pixmap)

        grad = extraLib.get_Sharpness_score(frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # grad_x = cv2.Sobel(frame, -1, 1, 0, ksize=5)
        # grad_y = cv2.Sobel(frame, -1, 0, 1, ksize=5)
        # grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
        Qimg = QtGui.QImage(grad.data, grad.shape[1], grad.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap.fromImage(Qimg)
        self.label_image_show_2.setPixmap(pixmap)
        self.label_score.setText(str(grad.var()))


    def closeEvent(self, event):
        self.camera.cameraObject.Terminate()
        self.camera_Thread.quit()


class CameraThread(QtCore.QObject):
    stop_signal = QtCore.pyqtSignal()
    CameraSignal = QtCore.pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.data = None
        self.flag = None
        self.cameraObject = CanonLib.CanonCamera()
        self.cameraObject.Init_Camera()


    def work(self):

        self.cameraObject.set_LiveView_ready()
        while self.flag:
            self.data = self.cameraObject.get_Live_image()
            if (self.data.size != 0) and (self.data[0] != 0):
                self.CameraSignal.emit(self.data)
                time.sleep(0.1)
        self.cameraObject.Release_Live()
        self.stop_signal.emit()
        # self.camera.Terminate()


class AutoFocusThread(QtCore.QObject):
    stop_signal = QtCore.pyqtSignal()

    def work(self):
        global Z_axis, pos_Z, liveImage
        self.maxScore = 0
        self.maxPosition = pos_Z

        self.pos_now = pos_Z
        Z_axis.set_vel_params(100000, 1000000)
        Z_axis.move_at_velocity(2)
        while pos_Z > self.pos_now-20000:
            time.sleep(0.2)
        Z_axis.stop_profiled()
        Z_axis.set_vel_params(100000, 100000)
        self.s = np.array([[0., 0., 0.]])
        Z_axis.move_to_position(self.pos_now+20000)
        while pos_Z != self.pos_now+20000:
            self.p = pos_Z
            self.image = liveImage
            self.shap = extraLib.get_Sharpness_score(self.image)
            self.score = self.shap.var()
            self.b = np.array([[Z_axis.get_position(), self.p, self.score]])
            self.s= np.r_[self.s, self.b]
            if self.score > self.maxScore:
                self.maxPosition = self.p
                self.maxScore = self.score

        Z_axis.set_vel_params(100000, 3000000)
        Z_axis.move_to_position(self.maxPosition)
        self.stop_signal.emit()








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = GUIMainWindow()
    sys.exit(app.exec_())
