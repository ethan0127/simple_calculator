#!/usr/bin/env python  
# -*- coding:utf-8 -*- 
# __author__ = 'yanzhengbin'
# __time__   = '2018/2/23 9:27'

from PyQt5 import QtWidgets
from calc import Ui_MainWindow
from functools import partial


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.flag = False
        self.setupUi(self)
        for item in range(1, 16):
            if item == 1:
                button_name = "pushButton"
            else:
                button_name = "pushButton_" + str(item)

            buttonname = self.__getattribute__(button_name)
            buttonname.clicked.connect(partial(self.get_value, button_name))

    def get_value(self, args):
        if self.flag:
            self.textBrowser.setText("0")
        text_area_value = self.textBrowser.toPlainText()
        button_value = "self." + args + ".text()"
        value = eval(button_value)
        self.flag = False
        if text_area_value == "0":
            text_area_new_value = value
        else:
            text_area_new_value = text_area_value + value
        self.textBrowser.setText(text_area_new_value)
        if value == "=":
            self.calculate(text_area_value)
            self.flag = True

    def calculate(self, a_string):
        try:
            result = eval(a_string)
            self.textBrowser.setText(a_string + "=" + str(result))
        except Exception as e:
            print("输入不合法")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyMainWindow()
    myshow.show()
    sys.exit(app.exec_())
