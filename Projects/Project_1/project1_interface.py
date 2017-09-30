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

class Ui_DisplayWidget(object):
    def setupUi(self, DisplayWidget):
        DisplayWidget.setObjectName(_fromUtf8("DisplayWidget"))
        DisplayWidget.resize(523, 318)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.Temperature_Label = QtGui.QLabel(self.dockWidgetContents)
        self.Temperature_Label.setGeometry(QtCore.QRect(120, 36, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Temperature_Label.setFont(font)
        self.Temperature_Label.setObjectName(_fromUtf8("Temperature_Label"))
        self.Humidity_Label = QtGui.QLabel(self.dockWidgetContents)
        self.Humidity_Label.setGeometry(QtCore.QRect(120, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Humidity_Label.setFont(font)
        self.Humidity_Label.setObjectName(_fromUtf8("Humidity_Label"))
        self.Time_Label = QtGui.QLabel(self.dockWidgetContents)
        self.Time_Label.setGeometry(QtCore.QRect(120, 100, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time_Label.setFont(font)
        self.Time_Label.setObjectName(_fromUtf8("Time_Label"))
        self.Temperature_Value = QtGui.QLabel(self.dockWidgetContents)
        self.Temperature_Value.setGeometry(QtCore.QRect(300, 37, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Temperature_Value.setFont(font)
        self.Temperature_Value.setObjectName(_fromUtf8("Temperature_Value"))
        self.Humidity_Value = QtGui.QLabel(self.dockWidgetContents)
        self.Humidity_Value.setGeometry(QtCore.QRect(300, 70, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Humidity_Value.setFont(font)
        self.Humidity_Value.setObjectName(_fromUtf8("Humidity_Value"))
        self.Time_Value = QtGui.QLabel(self.dockWidgetContents)
        self.Time_Value.setGeometry(QtCore.QRect(300, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Time_Value.setFont(font)
        self.Time_Value.setObjectName(_fromUtf8("Time_Value"))
        self.Refresh_PB = QtGui.QPushButton(self.dockWidgetContents)
        self.Refresh_PB.setGeometry(QtCore.QRect(60, 180, 99, 27))
        self.Refresh_PB.setObjectName(_fromUtf8("Refresh_PB"))
        self.Graph_PB = QtGui.QPushButton(self.dockWidgetContents)
        self.Graph_PB.setGeometry(QtCore.QRect(220, 180, 99, 27))
        self.Graph_PB.setObjectName(_fromUtf8("Graph_PB"))
        self.SetAlarm_PB = QtGui.QPushButton(self.dockWidgetContents)
        self.SetAlarm_PB.setGeometry(QtCore.QRect(370, 180, 99, 27))
        self.SetAlarm_PB.setObjectName(_fromUtf8("SetAlarm_PB"))
        DisplayWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DisplayWidget)
        QtCore.QMetaObject.connectSlotsByName(DisplayWidget)

    def retranslateUi(self, DisplayWidget):
        DisplayWidget.setWindowTitle(_translate("DisplayWidget", "DockWidget", None))
        self.Temperature_Label.setText(_translate("DisplayWidget", "Temperature", None))
        self.Humidity_Label.setText(_translate("DisplayWidget", "Humidity", None))
        self.Time_Label.setText(_translate("DisplayWidget", "Time", None))
        self.Temperature_Value.setText(_translate("DisplayWidget", "0.00", None))
        self.Humidity_Value.setText(_translate("DisplayWidget", "0.00", None))
        self.Time_Value.setText(_translate("DisplayWidget", "0.00", None))
        self.Refresh_PB.setText(_translate("DisplayWidget", "Refresh", None))
        self.Graph_PB.setText(_translate("DisplayWidget", "Graph", None))
        self.SetAlarm_PB.setText(_translate("DisplayWidget", "Set Alarm", None))

