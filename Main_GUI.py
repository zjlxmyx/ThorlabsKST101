import sys
import time
from ui_designer_main_GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ThorlabsKST101 import *


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

    def init_motor(self):
        global X_axis, Y_axis
        X_axis = Motor('26000284')
        X_axis.connect()

        Y_axis = Motor('26000306')
        Y_axis.connect()

        time.sleep(0.1)
        X_axis.start_polling(200)
        Y_axis.start_polling(200)

        time.sleep(0.1)
        X_axis.set_vel_params(500000, 50000000)
        Y_axis.set_vel_params(500000, 50000000)

        time.sleep(0.1)
        X_axis.home()
        Y_axis.home()

        time.sleep(0.5)
        while Y_axis.is_moving() or X_axis.is_moving():
            time.sleep(1)
        X_axis.move_to_position(3700000)
        Y_axis.move_to_position(3700000)

        time.sleep(0.1)
        X_axis.set_vel_params(500000, 15000000)
        Y_axis.set_vel_params(500000, 15000000)

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

        # change the velocity of moving
        self.radioButton_fast.clicked.connect(lambda: X_axis.set_vel_params(50000, 15000000))
        self.radioButton_fast.clicked.connect(lambda: Y_axis.set_vel_params(50000, 15000000))
        self.radioButton_normal.clicked.connect(lambda: X_axis.set_vel_params(30000, 8000000))
        self.radioButton_normal.clicked.connect(lambda: Y_axis.set_vel_params(30000, 8000000))
        self.radioButton_slow.clicked.connect(lambda: X_axis.set_vel_params(10000, 1000000))
        self.radioButton_slow.clicked.connect(lambda: Y_axis.set_vel_params(10000, 1000000))

        # Button of Move to
        self.button_MoveTo.clicked.connect(self.move_to)

    # function of showing position of motors
    def position_refresh(self):
        XPosition = X_axis.get_position()
        self.label_x.setText(str(XPosition))
        YPosition = Y_axis.get_position()
        self.label_y.setText(str(YPosition))

    # function of move to button
    def move_to(self):
        if self.checkBox_xMove.isChecked():
            X_axis.move_to_position(int(self.lineEdit_xMoveTo.text()))

        if self.checkBox_yMove.isChecked():
            Y_axis.move_to_position(int(self.lineEdit_yMoveTo.text()))

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = GUIMainWindow()
    sys.exit(app.exec_())
