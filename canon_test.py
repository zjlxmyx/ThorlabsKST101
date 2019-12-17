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
        Z_axis.start_polling(200)

        def on_timer():
            while True:
                time.sleep(0.2)
                self.position_refresh()
        t = Timer(0, on_timer)  # Quit after 5 seconds
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


    def stop_camera_Thread(self):
        self.camera_Thread.quit()


    def position_refresh(self):
        global pos_Z
        pos_Z = Z_axis.get_position()
        self.statusbar().showMessage(str(pos_Z))


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
        frame = jpeg.decode(image)
        liveImage = frame
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
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
        print(grad.var())


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

    def work(self):
        self.maxScore = 0
        self.maxPosition = None
        global Z_axis, pos_Z, liveImage
        pos_now = Z_axis.get_position()
        Z_axis.move_to_position(pos_now-30000)
        while Z_axis.is_moving():
            time.sleep(0.5)
        Z_axis.move_to_position(pos_now+30000)
        while Z_axis.is_moving():
            p = pos_Z
            score = extraLib.get_Sharpness_score(liveImage)
            if score > self.maxScore:
                self.maxPosition = p
                self.maxScore = score
        Z_axis.move_to_position(self.maxPosition)








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = GUIMainWindow()
    sys.exit(app.exec_())
