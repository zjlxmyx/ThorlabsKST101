# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_main_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_S = QtWidgets.QPushButton(self.centralwidget)
        self.button_S.setGeometry(QtCore.QRect(1570, 160, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_S.setFont(font)
        self.button_S.setObjectName("button_S")
        self.button_A = QtWidgets.QPushButton(self.centralwidget)
        self.button_A.setGeometry(QtCore.QRect(1470, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_A.setFont(font)
        self.button_A.setObjectName("button_A")
        self.button_W = QtWidgets.QPushButton(self.centralwidget)
        self.button_W.setGeometry(QtCore.QRect(1570, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_W.setFont(font)
        self.button_W.setObjectName("button_W")
        self.button_D = QtWidgets.QPushButton(self.centralwidget)
        self.button_D.setGeometry(QtCore.QRect(1670, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_D.setFont(font)
        self.button_D.setObjectName("button_D")
        self.button_R = QtWidgets.QPushButton(self.centralwidget)
        self.button_R.setGeometry(QtCore.QRect(1630, 450, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_R.setFont(font)
        self.button_R.setObjectName("button_R")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1470, 340, 241, 51))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_slow = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_slow.setGeometry(QtCore.QRect(20, 20, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_slow.setFont(font)
        self.radioButton_slow.setObjectName("radioButton_slow")
        self.radioButton_normal = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_normal.setGeometry(QtCore.QRect(90, 20, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_normal.setFont(font)
        self.radioButton_normal.setObjectName("radioButton_normal")
        self.radioButton_fast = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_fast.setGeometry(QtCore.QRect(170, 20, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_fast.setFont(font)
        self.radioButton_fast.setChecked(True)
        self.radioButton_fast.setObjectName("radioButton_fast")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1460, 40, 111, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 81, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_x = QtWidgets.QLabel(self.layoutWidget)
        self.label_x.setObjectName("label_x")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_x)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_y = QtWidgets.QLabel(self.layoutWidget)
        self.label_y.setObjectName("label_y")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_y)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_z = QtWidgets.QLabel(self.layoutWidget)
        self.label_z.setObjectName("label_z")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_z)
        self.button_MoveTo = QtWidgets.QPushButton(self.centralwidget)
        self.button_MoveTo.setGeometry(QtCore.QRect(1710, 50, 75, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_MoveTo.setFont(font)
        self.button_MoveTo.setObjectName("button_MoveTo")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1580, 49, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_xMove = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_xMove.setFont(font)
        self.checkBox_xMove.setObjectName("checkBox_xMove")
        self.gridLayout.addWidget(self.checkBox_xMove, 0, 0, 1, 1)
        self.lineEdit_xMoveTo = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_xMoveTo.setFont(font)
        self.lineEdit_xMoveTo.setAccessibleName("")
        self.lineEdit_xMoveTo.setInputMask("")
        self.lineEdit_xMoveTo.setText("")
        self.lineEdit_xMoveTo.setCursorPosition(0)
        self.lineEdit_xMoveTo.setPlaceholderText("")
        self.lineEdit_xMoveTo.setObjectName("lineEdit_xMoveTo")
        self.gridLayout.addWidget(self.lineEdit_xMoveTo, 0, 1, 1, 1)
        self.checkBox_yMove = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_yMove.setFont(font)
        self.checkBox_yMove.setObjectName("checkBox_yMove")
        self.gridLayout.addWidget(self.checkBox_yMove, 1, 0, 1, 1)
        self.lineEdit_yMoveTo = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_yMoveTo.setFont(font)
        self.lineEdit_yMoveTo.setAccessibleName("")
        self.lineEdit_yMoveTo.setInputMask("")
        self.lineEdit_yMoveTo.setText("")
        self.lineEdit_yMoveTo.setCursorPosition(0)
        self.lineEdit_yMoveTo.setPlaceholderText("")
        self.lineEdit_yMoveTo.setObjectName("lineEdit_yMoveTo")
        self.gridLayout.addWidget(self.lineEdit_yMoveTo, 1, 1, 1, 1)
        self.lineEdit_zMoveTo = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_zMoveTo.setFont(font)
        self.lineEdit_zMoveTo.setAccessibleName("")
        self.lineEdit_zMoveTo.setInputMask("")
        self.lineEdit_zMoveTo.setText("")
        self.lineEdit_zMoveTo.setCursorPosition(0)
        self.lineEdit_zMoveTo.setPlaceholderText("")
        self.lineEdit_zMoveTo.setObjectName("lineEdit_zMoveTo")
        self.gridLayout.addWidget(self.lineEdit_zMoveTo, 2, 1, 1, 1)
        self.checkBox_zMove = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_zMove.setFont(font)
        self.checkBox_zMove.setObjectName("checkBox_zMove")
        self.gridLayout.addWidget(self.checkBox_zMove, 2, 0, 1, 1)
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(1710, 110, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(200, 40, 1200, 800))
        self.label_camera.setText("")
        self.label_camera.setPixmap(QtGui.QPixmap("../../Desktop/Nanostrukturen_Logo.bmp"))
        self.label_camera.setObjectName("label_camera")
        self.slider_XY = QtWidgets.QSlider(self.centralwidget)
        self.slider_XY.setGeometry(QtCore.QRect(1470, 400, 241, 22))
        self.slider_XY.setMinimum(50000)
        self.slider_XY.setMaximum(20000000)
        self.slider_XY.setSingleStep(1)
        self.slider_XY.setPageStep(10000)
        self.slider_XY.setProperty("value", 15000000)
        self.slider_XY.setOrientation(QtCore.Qt.Horizontal)
        self.slider_XY.setObjectName("slider_XY")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1510, 450, 101, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_slow_Z = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_slow_Z.setGeometry(QtCore.QRect(20, 100, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_slow_Z.setFont(font)
        self.radioButton_slow_Z.setObjectName("radioButton_slow_Z")
        self.radioButton_fast_Z = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_fast_Z.setGeometry(QtCore.QRect(20, 20, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_fast_Z.setFont(font)
        self.radioButton_fast_Z.setChecked(True)
        self.radioButton_fast_Z.setObjectName("radioButton_fast_Z")
        self.radioButton_normal_Z = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_normal_Z.setGeometry(QtCore.QRect(20, 60, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_normal_Z.setFont(font)
        self.radioButton_normal_Z.setObjectName("radioButton_normal_Z")
        self.button_F = QtWidgets.QPushButton(self.centralwidget)
        self.button_F.setGeometry(QtCore.QRect(1630, 550, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_F.setFont(font)
        self.button_F.setObjectName("button_F")
        self.label_XY_Verlosity = QtWidgets.QLabel(self.centralwidget)
        self.label_XY_Verlosity.setGeometry(QtCore.QRect(1716, 360, 61, 41))
        self.label_XY_Verlosity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XY_Verlosity.setObjectName("label_XY_Verlosity")
        self.label_Z_Verlosity = QtWidgets.QLabel(self.centralwidget)
        self.label_Z_Verlosity.setGeometry(QtCore.QRect(1530, 590, 71, 31))
        self.label_Z_Verlosity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Z_Verlosity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Z_Verlosity.setObjectName("label_Z_Verlosity")
        self.slider_Z = QtWidgets.QSlider(self.centralwidget)
        self.slider_Z.setGeometry(QtCore.QRect(1480, 450, 22, 161))
        self.slider_Z.setMinimum(5000)
        self.slider_Z.setMaximum(10000000)
        self.slider_Z.setSingleStep(1)
        self.slider_Z.setPageStep(1000)
        self.slider_Z.setProperty("value", 8000000)
        self.slider_Z.setOrientation(QtCore.Qt.Vertical)
        self.slider_Z.setObjectName("slider_Z")
        self.button_camera = QtWidgets.QPushButton(self.centralwidget)
        self.button_camera.setGeometry(QtCore.QRect(1480, 670, 101, 61))
        self.button_camera.setCheckable(True)
        self.button_camera.setObjectName("button_camera")
        self.button_capture = QtWidgets.QPushButton(self.centralwidget)
        self.button_capture.setGeometry(QtCore.QRect(1480, 750, 101, 61))
        self.button_capture.setCheckable(False)
        self.button_capture.setObjectName("button_capture")
        self.button_RightUp = QtWidgets.QPushButton(self.centralwidget)
        self.button_RightUp.setGeometry(QtCore.QRect(110, 40, 70, 70))
        self.button_RightUp.setObjectName("button_RightUp")
        self.button_RightDown = QtWidgets.QPushButton(self.centralwidget)
        self.button_RightDown.setGeometry(QtCore.QRect(110, 120, 70, 70))
        self.button_RightDown.setObjectName("button_RightDown")
        self.button_LeftUp = QtWidgets.QPushButton(self.centralwidget)
        self.button_LeftUp.setGeometry(QtCore.QRect(30, 40, 70, 70))
        self.button_LeftUp.setObjectName("button_LeftUp")
        self.button_LeftDown = QtWidgets.QPushButton(self.centralwidget)
        self.button_LeftDown.setGeometry(QtCore.QRect(30, 120, 70, 70))
        self.button_LeftDown.setObjectName("button_LeftDown")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(50, 250, 111, 81))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 21, 19))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 25, 20, 19))
        self.label_4.setObjectName("label_4")
        self.label_wafer_x = QtWidgets.QLabel(self.groupBox_4)
        self.label_wafer_x.setGeometry(QtCore.QRect(40, 25, 52, 19))
        self.label_wafer_x.setObjectName("label_wafer_x")
        self.label_y_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_y_2.setGeometry(QtCore.QRect(40, 50, 52, 19))
        self.label_y_2.setObjectName("label_y_2")
        self.button_coord = QtWidgets.QPushButton(self.centralwidget)
        self.button_coord.setGeometry(QtCore.QRect(30, 200, 151, 31))
        self.button_coord.setObjectName("button_coord")
        self.lineEdit_xMoveTo_wafer = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xMoveTo_wafer.setGeometry(QtCore.QRect(40, 340, 82, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_xMoveTo_wafer.setFont(font)
        self.lineEdit_xMoveTo_wafer.setAccessibleName("")
        self.lineEdit_xMoveTo_wafer.setInputMask("")
        self.lineEdit_xMoveTo_wafer.setText("")
        self.lineEdit_xMoveTo_wafer.setCursorPosition(0)
        self.lineEdit_xMoveTo_wafer.setPlaceholderText("")
        self.lineEdit_xMoveTo_wafer.setObjectName("lineEdit_xMoveTo_wafer")
        self.lineEdit_yMoveTo_wafer = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_yMoveTo_wafer.setGeometry(QtCore.QRect(40, 370, 82, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_yMoveTo_wafer.setFont(font)
        self.lineEdit_yMoveTo_wafer.setAccessibleName("")
        self.lineEdit_yMoveTo_wafer.setInputMask("")
        self.lineEdit_yMoveTo_wafer.setText("")
        self.lineEdit_yMoveTo_wafer.setCursorPosition(0)
        self.lineEdit_yMoveTo_wafer.setPlaceholderText("")
        self.lineEdit_yMoveTo_wafer.setObjectName("lineEdit_yMoveTo_wafer")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 370, 21, 19))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 340, 20, 19))
        self.label_6.setObjectName("label_6")
        self.button_MoveTo_wafer = QtWidgets.QPushButton(self.centralwidget)
        self.button_MoveTo_wafer.setGeometry(QtCore.QRect(130, 340, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_MoveTo_wafer.setFont(font)
        self.button_MoveTo_wafer.setObjectName("button_MoveTo_wafer")
        self.label_camera.raise_()
        self.button_S.raise_()
        self.button_A.raise_()
        self.button_W.raise_()
        self.button_D.raise_()
        self.button_R.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.button_MoveTo.raise_()
        self.layoutWidget.raise_()
        self.button_home.raise_()
        self.slider_XY.raise_()
        self.groupBox_3.raise_()
        self.button_F.raise_()
        self.label_XY_Verlosity.raise_()
        self.label_Z_Verlosity.raise_()
        self.slider_Z.raise_()
        self.button_camera.raise_()
        self.button_capture.raise_()
        self.button_RightUp.raise_()
        self.button_RightDown.raise_()
        self.button_LeftUp.raise_()
        self.button_LeftDown.raise_()
        self.groupBox_4.raise_()
        self.button_coord.raise_()
        self.lineEdit_xMoveTo_wafer.raise_()
        self.lineEdit_yMoveTo_wafer.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.button_MoveTo_wafer.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Motor controller 1.0"))
        self.button_S.setText(_translate("MainWindow", "W"))
        self.button_A.setText(_translate("MainWindow", "A"))
        self.button_W.setText(_translate("MainWindow", "S"))
        self.button_D.setText(_translate("MainWindow", "D"))
        self.button_R.setText(_translate("MainWindow", "R"))
        self.groupBox.setTitle(_translate("MainWindow", "Velosity_XY"))
        self.radioButton_slow.setText(_translate("MainWindow", "slow"))
        self.radioButton_normal.setText(_translate("MainWindow", "normal"))
        self.radioButton_fast.setText(_translate("MainWindow", "fast"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Stage Coordinate:"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">X: </span></p></body></html>"))
        self.label_x.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Y: </span></p></body></html>"))
        self.label_y.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Z: </span></p></body></html>"))
        self.label_z.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.button_MoveTo.setText(_translate("MainWindow", "Move to"))
        self.checkBox_xMove.setText(_translate("MainWindow", "X"))
        self.checkBox_yMove.setText(_translate("MainWindow", "Y"))
        self.checkBox_zMove.setText(_translate("MainWindow", "Z"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Velosity_Z"))
        self.radioButton_slow_Z.setText(_translate("MainWindow", "slow"))
        self.radioButton_fast_Z.setText(_translate("MainWindow", "fast"))
        self.radioButton_normal_Z.setText(_translate("MainWindow", "normal"))
        self.button_F.setText(_translate("MainWindow", "F"))
        self.label_XY_Verlosity.setText(_translate("MainWindow", "15000000"))
        self.label_Z_Verlosity.setText(_translate("MainWindow", "8000000"))
        self.button_camera.setText(_translate("MainWindow", "Camera"))
        self.button_capture.setText(_translate("MainWindow", "Capture"))
        self.button_RightUp.setText(_translate("MainWindow", "Righ tUp"))
        self.button_RightDown.setText(_translate("MainWindow", "Right Down"))
        self.button_LeftUp.setText(_translate("MainWindow", "Left Up"))
        self.button_LeftDown.setText(_translate("MainWindow", "Left Down"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Wafer Coordinate:"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Y: </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">X: </span></p></body></html>"))
        self.label_wafer_x.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.label_y_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.button_coord.setText(_translate("MainWindow", "Wafer Coordinate System"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Y: </span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">X: </span></p></body></html>"))
        self.button_MoveTo_wafer.setText(_translate("MainWindow", "Move"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

