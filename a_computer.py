# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a_computer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(627, 650)
        self.pushButton7 = QtGui.QPushButton(Form)
        self.pushButton7.setGeometry(QtCore.QRect(60, 140, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName(_fromUtf8("pushButton7"))
        self.pushButton8 = QtGui.QPushButton(Form)
        self.pushButton8.setGeometry(QtCore.QRect(200, 140, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton8.setFont(font)
        self.pushButton8.setObjectName(_fromUtf8("pushButton8"))
        self.pushButton9 = QtGui.QPushButton(Form)
        self.pushButton9.setGeometry(QtCore.QRect(350, 140, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton9.setFont(font)
        self.pushButton9.setObjectName(_fromUtf8("pushButton9"))
        self.pushButtondivide = QtGui.QPushButton(Form)
        self.pushButtondivide.setGeometry(QtCore.QRect(490, 140, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButtondivide.setFont(font)
        self.pushButtondivide.setObjectName(_fromUtf8("pushButtondivide"))
        self.pushButton6 = QtGui.QPushButton(Form)
        self.pushButton6.setGeometry(QtCore.QRect(350, 270, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName(_fromUtf8("pushButton6"))
        self.pushButtonmutiply = QtGui.QPushButton(Form)
        self.pushButtonmutiply.setGeometry(QtCore.QRect(490, 270, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButtonmutiply.setFont(font)
        self.pushButtonmutiply.setObjectName(_fromUtf8("pushButtonmutiply"))
        self.pushButton5 = QtGui.QPushButton(Form)
        self.pushButton5.setGeometry(QtCore.QRect(200, 270, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName(_fromUtf8("pushButton5"))
        self.pushButton4 = QtGui.QPushButton(Form)
        self.pushButton4.setGeometry(QtCore.QRect(60, 270, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName(_fromUtf8("pushButton4"))
        self.pushButton3 = QtGui.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(350, 400, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName(_fromUtf8("pushButton3"))
        self.pushButtonsubstract = QtGui.QPushButton(Form)
        self.pushButtonsubstract.setGeometry(QtCore.QRect(490, 400, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButtonsubstract.setFont(font)
        self.pushButtonsubstract.setObjectName(_fromUtf8("pushButtonsubstract"))
        self.pushButton2 = QtGui.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(200, 400, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton1 = QtGui.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(60, 400, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(62, 39, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButtonplus = QtGui.QPushButton(Form)
        self.pushButtonplus.setGeometry(QtCore.QRect(490, 530, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButtonplus.setFont(font)
        self.pushButtonplus.setObjectName(_fromUtf8("pushButtonplus"))
        self.pushButton0 = QtGui.QPushButton(Form)
        self.pushButton0.setGeometry(QtCore.QRect(60, 530, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButton0.setFont(font)
        self.pushButton0.setObjectName(_fromUtf8("pushButton0"))
        self.pushButtonpoint = QtGui.QPushButton(Form)
        self.pushButtonpoint.setGeometry(QtCore.QRect(200, 530, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButtonpoint.setFont(font)
        self.pushButtonpoint.setObjectName(_fromUtf8("pushButtonpoint"))
        self.pushButtonequal = QtGui.QPushButton(Form)
        self.pushButtonequal.setGeometry(QtCore.QRect(350, 530, 75, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.pushButtonequal.setFont(font)
        self.pushButtonequal.setObjectName(_fromUtf8("pushButtonequal"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "computer", None))
        self.pushButton7.setText(_translate("Form", "7", None))
        self.pushButton8.setText(_translate("Form", "8", None))
        self.pushButton9.setText(_translate("Form", "9", None))
        self.pushButtondivide.setText(_translate("Form", "/", None))
        self.pushButton6.setText(_translate("Form", "6", None))
        self.pushButtonmutiply.setText(_translate("Form", "*", None))
        self.pushButton5.setText(_translate("Form", "5", None))
        self.pushButton4.setText(_translate("Form", "4", None))
        self.pushButton3.setText(_translate("Form", "3", None))
        self.pushButtonsubstract.setText(_translate("Form", "-", None))
        self.pushButton2.setText(_translate("Form", "2", None))
        self.pushButton1.setText(_translate("Form", "1", None))
        self.pushButtonplus.setText(_translate("Form", "+", None))
        self.pushButton0.setText(_translate("Form", "0", None))
        self.pushButtonpoint.setText(_translate("Form", ".", None))
        self.pushButtonequal.setText(_translate("Form", "=", None))

