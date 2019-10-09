import sys
import time
import cv2
import numpy as np
from ui_designer_main_GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ThorlabsKST101 import *
from pyueye import ueye



class GUIMainWindow(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.init_UI()
        self.init_motor()

        # Multitasking for position from motors
        self.PositionThread = Thread()
        # Connecting the signal of new Thread to position refresh function
        self.PositionThread.PositionSignal.connect(self.position_refresh)
        self.PositionThread.start()

        self.camera = CameraThread()
        self.camera.CameraSignal.connect(self.camera_show)

        self.SaveImage = None



    def init_motor(self):
        global X_axis, Y_axis, Z_axis
        X_axis = Motor('26000284')
        X_axis.connect()

        Y_axis = Motor('26000306')
        Y_axis.connect()

        Z_axis = Motor('26000236')
        Z_axis.connect()

        time.sleep(0.1)
        X_axis.start_polling(200)
        Y_axis.start_polling(200)
        Z_axis.start_polling(200)

    def init_UI(self):

        # button function ------ motor move with velocity, and stop mode
        self.button_A.pressed.connect(lambda: X_axis.move_at_velocity(2))
        self.button_A.released.connect(lambda: X_axis.stop_profiled())

        self.button_D.pressed.connect(lambda: X_axis.move_at_velocity(1))
        self.button_D.released.connect(lambda: X_axis.stop_profiled())

        self.button_W.pressed.connect(lambda: Y_axis.move_at_velocity(1))
        self.button_W.released.connect(lambda: Y_axis.stop_profiled())

        self.button_S.pressed.connect(lambda: Y_axis.move_at_velocity(2))
        self.button_S.released.connect(lambda: Y_axis.stop_profiled())

        self.button_R.pressed.connect(lambda: Z_axis.move_at_velocity(1))
        self.button_R.released.connect(lambda: Z_axis.stop_profiled())

        self.button_F.pressed.connect(lambda: Z_axis.move_at_velocity(2))
        self.button_F.released.connect(lambda: Z_axis.stop_profiled())

        # change the velocity of moving
        self.radioButton_fast.clicked.connect(self.set_velosity_fast)
        self.radioButton_normal.clicked.connect(self.set_velosity_normal)
        self.radioButton_slow.clicked.connect(self.set_velosity_slow)

        self.radioButton_fast_Z.clicked.connect(self.set_velosity_fast_Z)
        self.radioButton_normal_Z.clicked.connect(self.set_velosity_normal_Z)
        self.radioButton_slow_Z.clicked.connect(self.set_velosity_slow_Z)

        # Button of Move to
        self.button_MoveTo.clicked.connect(self.move_to)

        # Button of Home
        self.button_home.clicked.connect(self.home)

        # Slider of Velocity
        self.slider_XY.valueChanged.connect(lambda: self.label_XY_Verlosity.setText(str(self.slider_XY.value())))
        self.slider_XY.sliderReleased.connect(self.set_velosity_xy)
        self.slider_Z.valueChanged.connect(lambda: self.label_Z_Verlosity.setText(str(self.slider_Z.value())))
        self.slider_Z.sliderReleased.connect(self.set_velosity_z)

        self.button_camera.clicked.connect(self.camera_task)
        self.button_capture.clicked.connect(self.capture)


    # function of showing position of motors
    def position_refresh(self):
        XPosition = X_axis.get_position()
        self.label_x.setText(str(XPosition))
        YPosition = Y_axis.get_position()
        self.label_y.setText(str(YPosition))
        ZPosition = Z_axis.get_position()
        self.label_z.setText(str(ZPosition))

    # function of move to button
    def move_to(self):
        if self.checkBox_xMove.isChecked():
            X_axis.move_to_position(int(self.lineEdit_xMoveTo.text()))

        if self.checkBox_yMove.isChecked():
            Y_axis.move_to_position(int(self.lineEdit_yMoveTo.text()))

        if self.checkBox_zMove.isChecked():
            Z_axis.move_to_position(int(self.lineEdit_zMoveTo.text()))


    def home(self):
        time.sleep(0.1)
        X_axis.set_vel_params(500000, 30000000)
        Y_axis.set_vel_params(500000, 30000000)
        Z_axis.set_vel_params(500000, 30000000)

        time.sleep(0.1)
        X_axis.home()
        Y_axis.home()
        Z_axis.home()


        time.sleep(0.5)
        while Y_axis.is_moving() or X_axis.is_moving():
            time.sleep(1)
        X_axis.move_to_position(3700000)
        Y_axis.move_to_position(3700000)
        Z_axis.move_to_position(4000000)

        time.sleep(0.1)
        X_axis.set_vel_params(500000, 15000000)
        Y_axis.set_vel_params(500000, 15000000)
        Z_axis.set_vel_params(500000, 15000000)

    def set_velosity_xy(self):
        X_axis.set_vel_params(100000, self.slider_XY.value())
        Y_axis.set_vel_params(100000, self.slider_XY.value())

    def set_velosity_z(self):
        Z_axis.set_vel_params(100000, self.slider_Z.value())

    # Keyboard motors controller
    def keyPressEvent(self, event):
        # press W
        if (event.key() == QtCore.Qt.Key_W) and (not event.isAutoRepeat()):
            Y_axis.move_at_velocity(1)

        # press S
        elif (event.key() == QtCore.Qt.Key_S) and (not event.isAutoRepeat()):
            Y_axis.move_at_velocity(2)

        # press A
        elif (event.key() == QtCore.Qt.Key_A) and (not event.isAutoRepeat()):
            X_axis.move_at_velocity(1)

        # press D
        elif (event.key() == QtCore.Qt.Key_D) and (not event.isAutoRepeat()):
            X_axis.move_at_velocity(2)

        # press R
        elif (event.key() == QtCore.Qt.Key_R) and (not event.isAutoRepeat()):
            Z_axis.move_at_velocity(1)

        # press F
        elif (event.key() == QtCore.Qt.Key_F) and (not event.isAutoRepeat()):
            Z_axis.move_at_velocity(2)

        # press Q
        elif event.key() == QtCore.Qt.Key_Q:
            if self.radioButton_slow.isChecked():
                self.radioButton_normal.setChecked(True)
                self.set_velosity_normal()
            else:
                self.radioButton_fast.setChecked(True)
                self.set_velosity_fast()

        # press E
        elif event.key() == QtCore.Qt.Key_E:
            if self.radioButton_fast.isChecked():
                self.radioButton_normal.setChecked(True)
                self.set_velosity_normal()
            else:
                self.radioButton_slow.setChecked(True)
                self.set_velosity_slow()

    def set_velosity_fast(self):
        X_axis.set_vel_params(100000, 15000000)
        Y_axis.set_vel_params(100000, 15000000)
        self.slider_XY.setValue(15000000)
        self.label_XY_Verlosity.setText('15000000')

    def set_velosity_normal(self):
        X_axis.set_vel_params(100000, 6000000)
        Y_axis.set_vel_params(100000, 6000000)
        self.slider_XY.setValue(6000000)
        self.label_XY_Verlosity.setText('6000000')

    def set_velosity_slow(self):
        X_axis.set_vel_params(100000, 500000)
        Y_axis.set_vel_params(100000, 500000)
        self.slider_XY.setValue(500000)
        self.label_XY_Verlosity.setText('500000')


    def set_velosity_fast_Z(self):
        Z_axis.set_vel_params(100000, 8000000)
        self.slider_Z.setValue(8000000)
        self.label_Z_Verlosity.setText('8000000')

    def set_velosity_normal_Z(self):
        Z_axis.set_vel_params(100000, 1000000)
        self.slider_Z.setValue(1000000)
        self.label_Z_Verlosity.setText('1000000')

    def set_velosity_slow_Z(self):
        Z_axis.set_vel_params(100000, 10000)
        self.slider_Z.setValue(10000)
        self.label_Z_Verlosity.setText('10000')

    def keyReleaseEvent(self, event):
        # release W
        if (event.key() == QtCore.Qt.Key_W) and (not event.isAutoRepeat()):
            Y_axis.stop_profiled()

        # release S
        elif (event.key() == QtCore.Qt.Key_S) and (not event.isAutoRepeat()):
            Y_axis.stop_profiled()

        # release A
        elif (event.key() == QtCore.Qt.Key_A) and (not event.isAutoRepeat()):
            X_axis.stop_profiled()

        # release D
        elif (event.key() == QtCore.Qt.Key_D) and (not event.isAutoRepeat()):
            X_axis.stop_profiled()

        # release R
        elif (event.key() == QtCore.Qt.Key_R) and (not event.isAutoRepeat()):
            Z_axis.stop_profiled()

        # release F
        elif (event.key() == QtCore.Qt.Key_F) and (not event.isAutoRepeat()):
            Z_axis.stop_profiled()

    def camera_show(self, image):
        self.SaveImage = image
        image1 = image / 4095 * 255
        image2 = image1.astype('uint8')

        png = np.reshape(image2, (1920, 2560))

        png = cv2.resize(png, (0, 0), fx=0.4, fy=0.4)

        Qimg = QtGui.QImage(png.data, png.shape[1], png.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap.fromImage(Qimg)
        self.label_camera.setPixmap(pixmap)

    def camera_task(self):
        if self.button_camera.isChecked():
            self.button_camera.setText('Camera ON')
            self.camera.flag = True
            self.camera.start()

        else:
            self.button_camera.setText('Camera')
            self.camera.flag = False


    def capture(self):
        ueye.is_ImageFile(self.camera.hCam, ueye.IS_IMAGE_FILE_CMD_SAVE, self.camera.IMAGE_FILE_PARAMS, self.camera.k)


# create the Thread Class
class Thread(QtCore.QThread):
    # define a new Signal without value
    PositionSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    # emit the signal every 0.2s
    def run(self):
        while True:
            time.sleep(0.2)
            self.PositionSignal.emit()


class CameraThread(QtCore.QThread):
    CameraSignal = QtCore.pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.hCam = ueye.HIDS(0)  # 0: first available camera;  1-254: The camera with the specified camera ID
        self.sInfo = ueye.SENSORINFO()
        self.cInfo = ueye.CAMINFO()
        self.pcImageMemory = ueye.c_mem_p()
        self.MemID = ueye.int()
        self.rectAOI = ueye.IS_RECT()
        self.pitch = ueye.INT()
        self.nBitsPerPixel = ueye.INT(16)  # take 8 bits per pixel for monochrome
        self.m_nColorMode = ueye.INT()  # Y8/RGB16/RGB24/REG32
        self.bytes_per_pixel = ueye.INT()
        self.width = None
        self.height = None
        self.data = None
        self.data1 = None
        self.data2 = None
        self.flag = True


    # emit the signal every 0.2s
    def run(self):

        a = ueye.is_InitCamera(self.hCam, None)
        b = ueye.is_GetCameraInfo(self.hCam, self.cInfo)
        c = ueye.is_GetSensorInfo(self.hCam, self.sInfo)

        d = ueye.is_ResetToDefault(self.hCam)
        e = ueye.is_SetDisplayMode(self.hCam, ueye.IS_SET_DM_DIB)

        g = ueye.is_AOI(self.hCam, ueye.IS_AOI_IMAGE_GET_AOI, self.rectAOI, ueye.sizeof(self.rectAOI))
        self.width = self.rectAOI.s32Width
        self.height = self.rectAOI.s32Height

        h = ueye.is_AllocImageMem(self.hCam, self.width, self.height, self.nBitsPerPixel, self.pcImageMemory,
                                  self.MemID)
        i = ueye.is_SetImageMem(self.hCam, self.pcImageMemory, self.MemID)
        f = ueye.is_SetColorMode(self.hCam, ueye.IS_CM_MONO12)

        ueye.is_CaptureVideo(self.hCam, ueye.IS_WAIT)

        j = ueye.is_InquireImageMem(self.hCam, self.pcImageMemory, self.MemID, self.width, self.height,
                                    self.nBitsPerPixel, self.pitch)
        self.IMAGE_FILE_PARAMS = ueye.IMAGE_FILE_PARAMS(self.pcImageMemory, self.MemID)
        self.IMAGE_FILE_PARAMS.nFileType = ueye.IS_IMG_PNG
        self.k = ueye.sizeof(self.IMAGE_FILE_PARAMS)

        while self.flag:
            self.data = np.ctypeslib.as_array(ctypes.cast(self.pcImageMemory, ctypes.POINTER(ctypes.c_ubyte)), (self.height * self.pitch,))
            self.data.dtype = 'uint16'

            self.CameraSignal.emit(self.data)
            time.sleep(0.1)

        ueye.is_FreeImageMem(self.hCam, self.pcImageMemory, self.MemID)
        ueye.is_ExitCamera(self.hCam)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = GUIMainWindow()
    sys.exit(app.exec_())
