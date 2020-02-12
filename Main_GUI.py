import sys
import time
import cv2
import numpy as np
import ctypes
from ui_designer_main_GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import ThorlabsKST101 as KST
import ThorlabsKDC101 as KDC
from pyueye import ueye
import extraLib
import CanonLib
from turbojpeg import TurboJPEG
from threading import Timer
jpeg = TurboJPEG("turbojpeg.dll")


global liveImage, X_axis, Y_axis, Z_axis


class GUIMainWindow(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.label_camera.setScaledContents(True)

        self.hide_all_scale()
        self.hide_all_center_marks()
        self.show()

        self.init_UIconnect()
        # self.init_motor()
        self.pos_X = 0
        self.pos_Y = 0
        self.pos_Z = 0
        self.pos_alpha = 0

        self.leftup = None
        self.leftdown = None
        self.rightup = None
        self.rightdown = None

        self.STW = None
        self.WTS = None
        self.waferCoordFlag = False

        self.autoFocus_flag = False

        # auto focus thread

        self.autoFocus = AutoFocusThread()
        self.autoFocus_Thread = QtCore.QThread()
        self.autoFocus.moveToThread(self.autoFocus_Thread)
        self.autoFocus_Thread.started.connect(self.autoFocus.work)
        self.autoFocus.autoFocus_stop_signal.connect(self.autoFocusStop)



    def hide_all_scale(self):
        self.label_scale_2dot5.setVisible(False)
        self.label_scale_10.setVisible(False)
        self.label_scale_20.setVisible(False)
        self.label_scale_50.setVisible(False)
        self.label_scale_100.setVisible(False)

    def hide_all_center_marks(self):
        self.label_cross.setVisible(False)

    def init_motor(self):
        self.statusBar().showMessage('Initializing...')

        global X_axis, Y_axis, Z_axis, alpha_axis, Z825B_axis

        X_axis = KST.Motor('26000236')
        X_axis.connect()

        Y_axis = KST.Motor('26002702')
        Y_axis.connect()

        Z_axis = KST.Motor('26002711')
        Z_axis.connect()

        alpha_axis = KDC.Motor('27255326')
        alpha_axis.connect()

        Z825B_axis = KDC.Motor('27255268')
        Z825B_axis.connect()

        time.sleep(0.1)
        X_axis.start_polling(200)
        Y_axis.start_polling(200)
        Z_axis.start_polling(50)
        alpha_axis.start_polling(200)

        time.sleep(0.1)

        def on_timer():
            while True:
                time.sleep(0.2)
                self.position_refresh()
        t = Timer(1, on_timer)
        t.start()

        self.statusBar().showMessage('')

    def init_UIconnect(self):

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

        # Button of init motor
        self.button_init_motor.clicked.connect(self.init_motor)

        # B82Z
        self.button_Z825B.clicked.connect(self.Z825B_movement)

        # Slider of Velocity
        self.slider_XY.valueChanged.connect(lambda: self.label_XY_Verlosity.setText(str(self.slider_XY.value())))
        self.slider_XY.sliderReleased.connect(self.set_velosity_xy)
        self.slider_Z.valueChanged.connect(lambda: self.label_Z_Verlosity.setText(str(self.slider_Z.value())))
        self.slider_Z.sliderReleased.connect(self.set_velosity_z)



        # Button of saving corner position
        self.button_LeftUp.clicked.connect(self.save_leftup)
        self.button_LeftDown.clicked.connect(self.save_leftdown)
        self.button_RightUp.clicked.connect(self.save_rightup)
        self.button_RightDown.clicked.connect(self.save_rightdown)

        # new coordinate system
        self.button_coord.clicked.connect(self.create_wafer_coordinate)
        self.button_MoveTo_wafer.clicked.connect(self.move_to_wafer)

        # comboBox to select camera
        self.comboBox_cameraList.activated.connect(self.select_camera)
        self.comboBox_centerCross.activated.connect(self.select_center_mark)
        self.comboBox_scale.activated.connect(self.select_scale)

        self.button_autoFocus.clicked.connect(self.auto_focus)

        self.button_saveTo.clicked.connect(self.save_to)

    # function of showing position of motors
    def position_refresh(self):

        # isMoving = X_axis.is_moving() or Y_axis.is_moving() or Z_axis.is_moving()
        # if isMoving:
        #     self.label_isMoving.setText("Motors are moving")
        # else:
        #     self.label_isMoving.setText("Motors are stopped")

        self.pos_X = X_axis.get_position()
        self.label_x.setText(str(self.pos_X))

        self.pos_Y = Y_axis.get_position()
        self.label_y.setText(str(self.pos_Y))

        self.pos_Z = Z_axis.get_position()
        self.label_z.setText(str(self.pos_Z))

        self.pos_alpha = alpha_axis.get_position()
        self.label_alpha.setText(str(self.pos_alpha))

        if self.waferCoordFlag:
            waferPosition = extraLib.get_new_pos(self.STW, [self.pos_X, self.pos_Y])
            self.label_wafer_x.setText(str(waferPosition[0]))
            self.label_wafer_y.setText(str(waferPosition[1]))

    # function of move to button
    def move_to(self):
        if self.checkBox_xMove.isChecked():
            X_axis.move_to_position(int(self.lineEdit_xMoveTo.text()))

        if self.checkBox_yMove.isChecked():
            Y_axis.move_to_position(int(self.lineEdit_yMoveTo.text()))

        if self.checkBox_zMove.isChecked():
            Z_axis.move_to_position(int(self.lineEdit_zMoveTo.text()))

    def home(self):

        X_axis.set_vel_params(500000, 30000000)
        Y_axis.set_vel_params(500000, 30000000)
        Z_axis.set_vel_params(500000, 30000000)

        time.sleep(0.1)
        X_axis.home()
        Y_axis.home()
        Z_axis.home()
        Z825B_axis.home()


        time.sleep(0.5)
        while Y_axis.is_moving() or X_axis.is_moving() or Z_axis.is_moving():
            time.sleep(1)
        X_axis.move_to_position(3700000)
        Y_axis.move_to_position(3700000)
        Z_axis.move_to_position(4000000)

        time.sleep(0.1)
        X_axis.set_vel_params(500000, 15000000)
        Y_axis.set_vel_params(500000, 15000000)
        Z_axis.set_vel_params(500000, 15000000)


    def Z825B_movement(self):
        if Z825B_axis.get_position() == 0:
            Z825B_axis.move_to_position(686080)
        else:
            Z825B_axis.move_to_position(0)


    def set_velosity_xy(self):
        X_axis.set_vel_params(100000, self.slider_XY.value())
        Y_axis.set_vel_params(100000, self.slider_XY.value())

    def set_velosity_z(self):
        Z_axis.set_vel_params(100000, self.slider_Z.value())

    # set velocity panel ---------------------------------------------------------------------------
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
        Z_axis.set_vel_params(100000, 100000)
        self.slider_Z.setValue(100000)
        self.label_Z_Verlosity.setText('100000')

    # Keyboard motors controller -------------------------------------------------------------------
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

    # save and show position of corner on button ----------------------------------------------------
    def save_leftup(self):
        self.leftup = [self.pos_X, self.pos_Y, self.pos_Z]
        text = "Left Up" + "\nx= " + str(self.pos_X) + " \ny= " + str(self.pos_Y)
        self.button_LeftUp.setText(text)

    def save_leftdown(self):
        self.leftdown = [self.pos_X, self.pos_Y, self.pos_Z]
        text = "Left Down" + "\nx= " + str(self.pos_X) + " \ny= " + str(self.pos_Y)
        self.button_LeftDown.setText(text)

    def save_rightup(self):
        self.rightup = [self.pos_X, self.pos_Y, self.pos_Z]
        text = "Right Up" + "\nx= " + str(self.pos_X) + " \ny= " + str(self.pos_Y)
        self.button_RightUp.setText(text)

    def save_rightdown(self):
        self.rightdown = [self.pos_X, self.pos_Y, self.pos_Z]
        text = "Right Down" + "\nx= " + str(self.pos_X) + " \ny= " + str(self.pos_Y)
        self.button_RightDown.setText(text)

    def create_wafer_coordinate(self):
        self.STW, self.WTS = extraLib.get_matrix(self.leftdown[0:2], self.rightdown[0:2])
        self.waferCoordFlag = True

    def move_to_wafer(self):
        stageX = int(self.lineEdit_xMoveTo_wafer.text())
        stageY = int(self.lineEdit_yMoveTo_wafer.text())
        stagePosition = extraLib.get_new_pos(self.WTS, [stageX, stageY])
        X_axis.move_to_position(stagePosition[0])
        Y_axis.move_to_position(stagePosition[1])

    def select_center_mark(self):
        self.hide_all_center_marks()
        if self.comboBox_centerCross.currentIndex() == 1:
            self.label_cross.setVisible(True)

    def select_scale(self):
        self.hide_all_scale()
        if self.comboBox_scale.currentIndex() == 1:
            self.label_scale_2dot5.setVisible(True)
        elif self.comboBox_scale.currentIndex() == 2:
            self.label_scale_10.setVisible(True)
        elif self.comboBox_scale.currentIndex() == 3:
            self.label_scale_20.setVisible(True)
        elif self.comboBox_scale.currentIndex() == 4:
            self.label_scale_50.setVisible(True)
        elif self.comboBox_scale.currentIndex() == 5:
            self.label_scale_100.setVisible(True)

    # ------------------------------save to ----------------------------------

    def save_to(self):
        def on_timer():
            while True:
                time.sleep(0.2)
                self.label_camera.setText(time.strftime("%m%d%H%M%S", time.localtime()))
        t = Timer(0, on_timer)  # Quit after 5 seconds
        t.start()

        path = QtWidgets.QFileDialog.getExistingDirectory()

        self.label_savePath.setText(path)
        # self.CanonCamera.path = path

    # ------------------------------auto focus ----------------------------------

    def auto_focus(self):
        self.autoFocus_flag = True
        self.autoFocus_Thread.start()

    def autoFocusStop(self):
        self.autoFocus_flag = False
        self.autoFocus_Thread.quit()
        self.autoFocus_Thread.wait()




    # ------------------------------camera task ----------------------------------

    def select_camera(self):
        if self.comboBox_cameraList.currentIndex() == 1:

            self.CanonCamera = CameraThread_Canon_EOS_600D()
            self.camera_Thread = QtCore.QThread()
            self.CanonCamera.moveToThread(self.camera_Thread)
            self.camera_Thread.started.connect(self.CanonCamera.work)
            self.CanonCamera.stop_signal.connect(self.stop_camera_Thread)
            self.CanonCamera.restart_signal.connect(self.LiveView_restart)


            self.camera_init = self.camera_init_Canon
            self.camera_show = self.camera_show_Canon
            self.capture = self.capture_Canon
        elif self.comboBox_cameraList.currentIndex() == 2:
            # self.selectedCamera = CameraThread_UI_3480LE_M_GL()
            self.camera_init = self.camera_init_UI_3480LE
            self.camera_show = self.camera_show_UI_3480LE
            self.capture = self.capture_UI_3480LE

        self.button_camera.clicked.connect(self.camera_init)
        self.button_capture.clicked.connect(self.capture)

    def stop_camera_Thread(self):
        self.camera_Thread.quit()
        self.camera_Thread.wait()



    # ------------------------------camera for Canon_EOS_600D ----------------------------------

    def camera_init_Canon(self):

        if self.button_camera.isChecked():
            self.button_camera.setText('Camera ON')
            self.CanonCamera.CameraSignal.connect(self.camera_show)
            # self.CanonCamera.liveView_flag = True
            self.camera_Thread.start()
        else:
            self.button_camera.setText('Camera')
            self.CanonCamera.liveView_flag = False
            # self.sin.emit()

    def camera_show_Canon(self, image):
        global pos_Z, score, temp
        frame = jpeg.decode(image)
        Qimg = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        Qimg = Qimg.rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(Qimg)
        self.label_camera.setPixmap(pixmap)

        pos_Z = temp
        if self.autoFocus_flag:
            score = extraLib.get_Sharpness_score(frame)





    def capture_Canon(self):
        path = self.lineEdit_savePath.text()

        self.CanonCamera.path = path

        self.CanonCamera.capture_flag = True
        self.CanonCamera.liveView_flag = False

    def LiveView_restart(self):
        print("camera Thread finished = ", self.camera_Thread.isFinished())
        self.camera_Thread.quit()
        self.camera_Thread.wait()
        print("camera Thread finished = ", self.camera_Thread.isFinished())

        self.camera_Thread.start()

    # ------------------------------camera for UI_3480LE_M_GL ----------------------------------
    def camera_init_UI_3480LE(self):
        if self.button_camera.isChecked():
            self.camera = CameraThread_UI_3480LE_M_GL()
            self.camera.CameraSignal.connect(self.camera_show)
            self.SaveImage = None
            self.button_camera.setText('Camera ON')
            self.camera.flag = True
            self.camera.start()

        else:
            self.button_camera.setText('Camera')
            self.camera.flag = False

    def camera_show_UI_3480LE(self, image):
        self.SaveImage = image
        image1 = image / 4095 * 255
        image2 = image1.astype('uint8')

        png = np.reshape(image2, (1920, 2560))

        png = cv2.resize(png, (0, 0), fx=0.4, fy=0.4)

        Qimg = QtGui.QImage(png.data, png.shape[1], png.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap.fromImage(Qimg)
        self.label_camera.setPixmap(pixmap)

    def capture_UI_3480LE(self):
        ueye.is_ImageFile(self.camera.hCam, ueye.IS_IMAGE_FILE_CMD_SAVE, self.camera.IMAGE_FILE_PARAMS, self.camera.k)






    def closeEvent(self, event):
        self.CanonCamera.cameraObject.Terminate()
        self.camera_Thread.quit()


class CameraThread_UI_3480LE_M_GL(QtCore.QObject):
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
        self.autoParameter = ctypes.c_int(ueye.IS_AUTOPARAMETER_ENABLE)

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

        # ueye.is_AutoParameter(self.hCam, ueye.IS_AES_CMD_SET_ENABLE, self.autoParameter, ueye.sizeof(self.autoParameter))

        while self.flag:
            self.data = np.ctypeslib.as_array(ctypes.cast(self.pcImageMemory, ctypes.POINTER(ctypes.c_ubyte)), (self.height * self.pitch,))
            self.data.dtype = 'uint16'

            self.CameraSignal.emit(self.data)
            time.sleep(0.1)

        ueye.is_FreeImageMem(self.hCam, self.pcImageMemory, self.MemID)
        ueye.is_ExitCamera(self.hCam)


class CameraThread_Canon_EOS_600D(QtCore.QObject):
    CameraSignal = QtCore.pyqtSignal(np.ndarray)
    restart_signal = QtCore.pyqtSignal()
    stop_signal = QtCore.pyqtSignal()

    # def __init__(self):
    #     super().__init__()

    def work(self):
        global temp, Z_axis
        self.path = None
        self.ImageName = None
        self.data = None
        self.liveView_flag = True
        self.capture_flag = False
        self.cameraObject = CanonLib.CanonCamera()
        self.cameraObject.Init_Camera()
        self.cameraObject.set_LiveView_ready()
        time.sleep(2)

        while self.liveView_flag:
            try:
                temp = Z_axis.get_position()
            except:
                pass

            self.data = self.cameraObject.get_Live_image()
            if (self.data.size != 0) and (self.data[0] != 0):
                self.CameraSignal.emit(self.data)
            time.sleep(0.05)

        self.cameraObject.Release_Live()
        self.cameraObject.Terminate()
        time.sleep(0.5)
        if self.capture_flag:
            self.capture_flag = False
            self.cameraObject.Init_Camera()
            self.cameraObject.set_Capture_ready()
            self.cameraObject.get_Capture_image(self.path, self.ImageName)
            # time.sleep(2)
            self.cameraObject.Terminate()

            self.restart_signal.emit()
        else:
            self.stop_signal.emit()


class AutoFocusThread(QtCore.QObject):
    autoFocus_stop_signal = QtCore.pyqtSignal()

    def work(self):
        global Z_axis, pos_Z, score
        self.maxScore = 0
        self.maxPosition = pos_Z
        self.prange = 10000
        self.pos_now = pos_Z
        Z_axis.set_vel_params(100000, 1000000)
        Z_axis.move_at_velocity(1)

        while pos_Z < self.pos_now + self.prange:
            time.sleep(0.2)
        Z_axis.stop_profiled()
        Z_axis.set_vel_params(100000, 300000)
        # self.s = np.array([[0., 0.]])
        Z_axis.move_at_velocity(2)

        while pos_Z > self.pos_now - self.prange:
            if score > self.maxScore:
                self.maxPosition = pos_Z
                self.maxScore = score
            time.sleep(0.05)

        Z_axis.set_vel_params(100000, 1000000)
        Z_axis.move_to_position((self.maxPosition+500))
        self.autoFocus_stop_signal.emit()


class scanningThread(QtCore.QObject):
    focus_signal = QtCore.pyqtSignal()
    capture_signal = QtCore.pyqtSignal()

    def __init__(self):
        self.leftup = None
        self.leftdown = None
        self.rightup = None
        self.rightdown = None

        self.capturing_flag = False


    def work(self):
        global X_axis, Y_axis, Z_axis

        x_array, y_array = extraLib.get_scan_pos(self.leftdown[0:2], self.rightdown[0:2], self.rightup[0:2], self.leftup[0:2])

        for x in x_array:
            X_axis.move_to_position(x)
            for y in y_array:
                Y_axis.move_to_position(y)

                z = extraLib.Estimate_z_pos([x, y], self.leftdown, self.rightdown, self.rightup, self.leftup)
                Z_axis.move_to_position(z)

                while (X_axis.get_position() != x) and (Y_axis.get_position() != y and Z_axis.get_position() != z):
                    time.sleep(0.4)

                self.focus_signal.emit()
                time.sleep(0.5)

                while Z_axis.is_moving():
                    time.sleep(0.2)

                self.capturing_flag = True
                self.capture_signal.emit()
                while self.capturing_flag:
                    time.sleep(0.2)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = GUIMainWindow()
    sys.exit(app.exec_())
