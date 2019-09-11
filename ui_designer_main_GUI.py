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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.up_button = QtWidgets.QPushButton(self.centralwidget)
        self.up_button.setGeometry(QtCore.QRect(370, 270, 75, 75))
        self.up_button.setObjectName("up_button")
        self.left_button = QtWidgets.QPushButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(280, 360, 75, 75))
        self.left_button.setObjectName("left_button")
        self.down_button = QtWidgets.QPushButton(self.centralwidget)
        self.down_button.setGeometry(QtCore.QRect(370, 360, 75, 75))
        self.down_button.setObjectName("down_button")
        self.right_button = QtWidgets.QPushButton(self.centralwidget)
        self.right_button.setGeometry(QtCore.QRect(460, 360, 75, 75))
        self.right_button.setObjectName("right_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 90, 71, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.x_label = QtWidgets.QLabel(self.layoutWidget)
        self.x_label.setObjectName("x_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x_label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.y_label = QtWidgets.QLabel(self.layoutWidget)
        self.y_label.setObjectName("y_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y_label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.z_label = QtWidgets.QLabel(self.layoutWidget)
        self.z_label.setObjectName("z_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.z_label)
        self.up_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.up_button_2.setGeometry(QtCore.QRect(550, 270, 75, 75))
        self.up_button_2.setObjectName("up_button_2")
        self.up_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.up_button_3.setGeometry(QtCore.QRect(550, 360, 75, 75))
        self.up_button_3.setObjectName("up_button_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.up_button.setText(_translate("MainWindow", "W"))
        self.left_button.setText(_translate("MainWindow", "A"))
        self.down_button.setText(_translate("MainWindow", "S"))
        self.right_button.setText(_translate("MainWindow", "D"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">X: </span></p></body></html>"))
        self.x_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Y: </span></p></body></html>"))
        self.y_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Z: </span></p></body></html>"))
        self.z_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">null</span></p></body></html>"))
        self.up_button_2.setText(_translate("MainWindow", "R"))
        self.up_button_3.setText(_translate("MainWindow", "F"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

