import sys
from ui_designer_main_GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ThorlabsKST101 import *


class GUIMainWindow(Ui_MainWindow):

    def __init__(self):
        super(GUIMainWindow, self).__init__()
        self.setupUi(MainWindow)

        self.init_motor()
        self.init_UI()

        self.PositionThread = Thread()
        self.PositionThread.PositionSignal.connect(self.position_refresh)
        self.PositionThread.start()

    def init_motor(self):
        global Y_axis
        Y_axis = Motor('26000306')
        Y_axis.connect()
        time.sleep(0.1)
        Y_axis.start_polling(200)
        time.sleep(0.1)
        Y_axis.set_vel_params(10000, 1000000)
        time.sleep(0.1)
        Y_axis.home()

    def init_UI(self):

        # button pressed function ------ motor move with velocity
        self.up_button.pressed.connect(lambda: Y_axis.move_at_velocity(1))
        # button released function ----- motor stopped
        self.up_button.released.connect(Y_axis.stop_profiled)

        self.down_button.pressed.connect(lambda: Y_axis.move_at_velocity(2))
        self.down_button.released.connect(Y_axis.stop_profiled)

    def position_refresh(self):
        YPosition = Y_axis.get_position()
        self.y_label.setText(str(YPosition))


class Thread(QtCore.QThread):
    PositionSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            time.sleep(0.2)
            self.PositionSignal.emit()







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUIMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())