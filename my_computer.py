# coding=utf-8
import sys
from PyQt4 import QtCore, QtGui
import a_computer


class MyCal(QtGui.QWidget):
    # 继承widgt
    def __init__(self):
        # 构造基类
        self.initdata()
        super(MyCal, self).__init__()
        self.my_ui = a_computer.Ui_Form()
        # 把ui关联起来,赋值记得用实例
        self.my_ui.setupUi(self)
        self.connect(self.my_ui.pushButton1, QtCore.SIGNAL('clicked()'), self.click_1)
        # 发信号，信号槽
        self.connect(self.my_ui.pushButton2, QtCore.SIGNAL('clicked()'), self.click_2)
        self.connect(self.my_ui.pushButton3, QtCore.SIGNAL('clicked()'), self.click_3)
        self.connect(self.my_ui.pushButton4, QtCore.SIGNAL('clicked()'), self.click_4)
        self.connect(self.my_ui.pushButton5, QtCore.SIGNAL('clicked()'), self.click_5)
        self.connect(self.my_ui.pushButton6, QtCore.SIGNAL('clicked()'), self.click_6)
        self.connect(self.my_ui.pushButton7, QtCore.SIGNAL('clicked()'), self.click_7)
        self.connect(self.my_ui.pushButton8, QtCore.SIGNAL('clicked()'), self.click_8)
        self.connect(self.my_ui.pushButton9, QtCore.SIGNAL('clicked()'), self.click_9)
        self.connect(self.my_ui.pushButton0, QtCore.SIGNAL('clicked()'), self.click_0)
        self.connect(self.my_ui.pushButtonpoint, QtCore.SIGNAL('clicked()'), self.click_point)
        self.connect(self.my_ui.pushButtonplus, QtCore.SIGNAL('clicked()'), self.click_plus)
        self.connect(self.my_ui.pushButtonequal, QtCore.SIGNAL('clicked()'), self.click_equal)
        self.connect(self.my_ui.pushButtondivide, QtCore.SIGNAL('clicked()'), self.click_divide)
        self.connect(self.my_ui.pushButtonsubstract, QtCore.SIGNAL('clicked()'), self.click_sustract)
        self.connect(self.my_ui.pushButtonmutiply, QtCore.SIGNAL('clicked()'), self.click_mutiply)

    def initdata(self):
        # 初始化数据
        self.num1 = ""
        self.num2 = ""
        self.opera = False
        self.point1 = 0
        self.point2 = 0
        self.opera_add = 0
        self.opera_minus = 0
        self.opera_divide = 0
        self.opera_mutipy = 0
        # 操作符默认是0

    def click_1(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "1"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "1"
            self.my_ui.lineEdit.setText(self.num2)

    def click_2(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "2"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "2"
            self.my_ui.lineEdit.setText(self.num2)

    def click_3(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "3"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "3"
            self.my_ui.lineEdit.setText(self.num2)

    def click_4(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "4"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "4"
            self.my_ui.lineEdit.setText(self.num2)

    def click_5(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "5"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "5"
            self.my_ui.lineEdit.setText(self.num2)

    def click_6(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "6"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "6"
            self.my_ui.lineEdit.setText(self.num2)

    def click_7(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "7"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "7"
            self.my_ui.lineEdit.setText(self.num2)

    def click_8(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "8"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "8"
            self.my_ui.lineEdit.setText(self.num2)

    def click_9(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "9"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "9"
            self.my_ui.lineEdit.setText(self.num2)

    def click_0(self):
        if self.opera == False:
            # 没点操作符，显示num1
            self.num1 += "0"
            self.my_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "0"
            self.my_ui.lineEdit.setText(self.num2)

    def click_point(self):
        if self.opera == False:
            if len(self.num1) != 0:
                if self.point1 == 0:
                    self.num1 += "."
                    self.my_ui.lineEdit.setText(self.num1)
        else:
            if len(self.num2) != 0:
                if self.point2 == 0:
                    self.num2 += "."
                    self.my_ui.lineEdit.setText(self.num2)

    def click_plus(self):
        self.opera = True
        self.opera_add = 1
        self.opera_divide = 0
        self.opera_minus = 0
        self.opera_mutipy = 0
        self.my_ui.lineEdit.setText("+")

    def click_divide(self):
            self.opera = True
            self.opera_add = 0
            self.opera_divide = 1
            self.opera_minus = 0
            self.opera_mutipy = 0
            self.my_ui.lineEdit.setText("/")

    def click_sustract(self):
            self.opera = True
            self.opera_add = 0
            self.opera_divide = 0
            self.opera_minus = 1
            self.opera_mutipy = 0
            self.my_ui.lineEdit.setText("-")

    def click_mutiply(self):
            self.opera = True
            self.opera_add = 0
            self.opera_divide = 0
            self.opera_minus = 0
            self.opera_mutipy = 1
            self.my_ui.lineEdit.setText("*")

    def click_equal(self):
        if self.opera_add == 1:
            print type(self.num1)
            self.my_ui.lineEdit.setText(str(float(self.num1) + float(self.num2)))
        if self.opera_minus == 1:
            self.my_ui.lineEdit.setText(str(float(self.num1) - float(self.num2)))
        if self.opera_mutipy == 1:
            self.my_ui.lineEdit.setText(str(float(self.num1) * float(self.num2)))
        if self.opera_divide == 1:
            self.my_ui.lineEdit.setText(str(float(self.num1) / float(self.num2)))
        self.initdata()


app = QtGui.QApplication(sys.argv)
my_cal = MyCal()
my_cal.show()
app.exec_()








