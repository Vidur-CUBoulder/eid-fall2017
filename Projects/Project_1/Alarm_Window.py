# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alarm_Window.ui'
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

class Ui_user_input(object):
    def setupUi(self, user_input):
        user_input.setObjectName(_fromUtf8("user_input"))
        user_input.resize(777, 298)
        self.centralwidget = QtGui.QWidget(user_input)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Description_Label = QtGui.QLabel(self.centralwidget)
        self.Description_Label.setGeometry(QtCore.QRect(240, 130, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Description_Label.setFont(font)
        self.Description_Label.setObjectName(_fromUtf8("Description_Label"))
        self.okay_button = QtGui.QPushButton(self.centralwidget)
        self.okay_button.setGeometry(QtCore.QRect(370, 180, 99, 27))
        self.okay_button.setObjectName(_fromUtf8("okay_button"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 130, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        user_input.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(user_input)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        user_input.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(user_input)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        user_input.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(user_input)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        user_input.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(user_input)
        QtCore.QMetaObject.connectSlotsByName(user_input)

    def retranslateUi(self, user_input):
        user_input.setWindowTitle(_translate("user_input", "MainWindow", None))
        self.Description_Label.setText(_translate("user_input", "Set Humidity Alaram at", None))
        self.okay_button.setText(_translate("user_input", "Okay", None))
        self.toolBar.setWindowTitle(_translate("user_input", "toolBar", None))

