# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_1_Interface.ui'
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

class Ui_DisplayWindow(object):
    def setupUi(self, DisplayWindow):
        DisplayWindow.setObjectName(_fromUtf8("DisplayWindow"))
        DisplayWindow.resize(774, 381)
        DisplayWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(DisplayWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Time_Label = QtGui.QLabel(self.centralwidget)
        self.Time_Label.setGeometry(QtCore.QRect(270, 140, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Time_Label.setFont(font)
        self.Time_Label.setObjectName(_fromUtf8("Time_Label"))
        self.Time_Value = QtGui.QLabel(self.centralwidget)
        self.Time_Value.setGeometry(QtCore.QRect(470, 140, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Time_Value.setFont(font)
        self.Time_Value.setObjectName(_fromUtf8("Time_Value"))
        self.Temperature_Label = QtGui.QLabel(self.centralwidget)
        self.Temperature_Label.setGeometry(QtCore.QRect(270, 79, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Temperature_Label.setFont(font)
        self.Temperature_Label.setObjectName(_fromUtf8("Temperature_Label"))
        self.Humidity_Label = QtGui.QLabel(self.centralwidget)
        self.Humidity_Label.setGeometry(QtCore.QRect(270, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Humidity_Label.setFont(font)
        self.Humidity_Label.setObjectName(_fromUtf8("Humidity_Label"))
        self.Humidity_Value = QtGui.QLabel(self.centralwidget)
        self.Humidity_Value.setGeometry(QtCore.QRect(470, 110, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Humidity_Value.setFont(font)
        self.Humidity_Value.setObjectName(_fromUtf8("Humidity_Value"))
        self.Temperature_Value = QtGui.QLabel(self.centralwidget)
        self.Temperature_Value.setGeometry(QtCore.QRect(470, 80, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Temperature_Value.setFont(font)
        self.Temperature_Value.setObjectName(_fromUtf8("Temperature_Value"))
        self.Refresh_PB = QtGui.QPushButton(self.centralwidget)
        self.Refresh_PB.setGeometry(QtCore.QRect(370, 250, 99, 27))
        self.Refresh_PB.setObjectName(_fromUtf8("Refresh_PB"))
        self.alarm_display_label = QtGui.QLabel(self.centralwidget)
        self.alarm_display_label.setGeometry(QtCore.QRect(270, 170, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.alarm_display_label.setFont(font)
        self.alarm_display_label.setObjectName(_fromUtf8("alarm_display_label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 170, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.alarm_display_label_2 = QtGui.QLabel(self.centralwidget)
        self.alarm_display_label_2.setGeometry(QtCore.QRect(270, 200, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.alarm_display_label_2.setFont(font)
        self.alarm_display_label_2.setObjectName(_fromUtf8("alarm_display_label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 200, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        DisplayWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DisplayWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        DisplayWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DisplayWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DisplayWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(DisplayWindow)

    def retranslateUi(self, DisplayWindow):
        DisplayWindow.setWindowTitle(_translate("DisplayWindow", "Temperature & Humidity Display ", None))
        self.Time_Label.setText(_translate("DisplayWindow", "Time", None))
        self.Time_Value.setText(_translate("DisplayWindow", "0.00", None))
        self.Temperature_Label.setText(_translate("DisplayWindow", "Temperature", None))
        self.Humidity_Label.setText(_translate("DisplayWindow", "Humidity", None))
        self.Humidity_Value.setText(_translate("DisplayWindow", "0.00", None))
        self.Temperature_Value.setText(_translate("DisplayWindow", "0.00", None))
        self.Refresh_PB.setText(_translate("DisplayWindow", "Refresh", None))
        self.alarm_display_label.setText(_translate("DisplayWindow", "Set Humidity Alarm", None))
        self.alarm_display_label_2.setText(_translate("DisplayWindow", "Set Temp Alarm", None))

