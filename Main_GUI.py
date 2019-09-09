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
        self.up_button.setText('up')
        self.up_button.pressed.connect(lambda: Y_axis.move_at_velocity(1))
        self.up_button.released.connect(Y_axis.stop_profiled)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUIMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())