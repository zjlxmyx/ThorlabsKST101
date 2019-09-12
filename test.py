# from ThorlabsKST101 import *
# SN = '26000306'
#
# Y_axis = Motor(SN)
# # time.sleep(1)
# a = Y_axis.connect()
# # time.sleep(1)
# # Y_axis.home()
# #
# # Y_axis.get_vel_params()
# #
# # print(Y_axis.Acce,Y_axis.MaxV)
# #
# # Y_axis.move_to_position(37546)
# #
# # b = Y_axis.is_moving()
#
# e = Y_axis.start_polling(200)
#
# # while 1:
# #     # time.sleep(0.1)
# #     print(Y_axis.is_moving())
# #     print(Y_axis.get_position())
#
# # c,d = Y_axis.get_jog_mode()
#
#
# z = 1
# class A():
#     b = 1
#     def __init__(self):
#         self.c = 2
#
# test = A()
# print(test.b)
# print(test.c)


import sys
from PyQt5 import QtCore, QtWidgets


# 声明窗口
class Window(QtWidgets.QWidget):
    # 初始化
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()
    # 设置窗口的参数
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.setWindowTitle('按键检测')
        self.show()


    def keyPressEvent(self, event):

        # 这里event.key（）显示的是按键的编码
        if (event.key() == QtCore.Qt.Key_W) and (not event.isAutoRepeat()):
            print('start')

    def keyReleaseEvent(self, event):
        if (event.key() == QtCore.Qt.Key_W) and (not event.isAutoRepeat()):
            print('stop')

        # if event.key() == QtCore.Qt.Key_W:
        #     if not event.isAutoRepeat():
        #         print('stop')
        #     self.flag = event.isAutoRepeat()



    #     print("按下：" + str(event.key()))
    #     # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
    #     if (event.key() == Qt.Key_Escape):
    #         print('测试：ESC')
    #     if (event.key() == Qt.Key_A):
    #         print('测试：A')
    #     if (event.key() == Qt.Key_1):
    #         print('测试：1')
    #     if (event.key() == Qt.Key_Enter):
    #         print('测试：Enter')
    #     if (event.key() == Qt.Key_Space):
    #         print('测试：Space')
    #     # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
    #     if (event.key() == Qt.Key_P):
    #         if QApplication.keyboardModifiers() == Qt.ShiftModifier:
    #             print("shift + p")
    #         else :
    #             print("p")
    #
    #     if (event.key() == Qt.Key_O) and QApplication.keyboardModifiers() == Qt.ShiftModifier:
    #         print("shift + o")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())