import sys
import os
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd

import Adafruit_DHT
from PyQt4 import QtCore, QtGui

# DHT22 config options...
DHT_PIN  = 4
DHT_TYPE = Adafruit_DHT.DHT22

# Import the created interface
from project1_interface import Ui_DisplayWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

#build the UI...
        self.ui = Ui_DisplayWindow()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.Time_Display)
        self.timer.start()

        self.ui.Refresh_PB.clicked.connect(self.f_Refresh)
        #self.ui.Graph_PB.clicked.connect(self.f_Graph)
        

    def f_Humidity_Alarm(self):
        val_humidity = self.ui.lineEdit.text()
        if(float(humidity) > float(val_humidity)):
            self.ui.alarm_display_label.setStyleSheet('color:red')
        else:
            self.ui.alarm_display_label.setStyleSheet('color:default')
    
    def f_Temp_Alarm(self):
        val_temp = self.ui.lineEdit_2.text()
        if(float(temp) >= float(val_temp)):
            self.ui.alarm_display_label_2.setStyleSheet('color:red')
        else:
            self.ui.alarm_display_label_2.setStyleSheet('color:default')

    def f_Graph(self):
        humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
        times = pd.date_range('2017-10-06', periods=500, freq='1min')
        
        fig, ax = plt.subplots(1)
        fig.autofmt_xdate()
        plt.plot(times, range(times.size))

        xfmt = mdates.DateFormatter('%H')
        ax.xaxis.set_major_formatter(xfmt)

        plt.show()


    def f_Refresh(self):
        # Refresh all label values  
        self.ui.Humidity_Value.setText("0.00")
        self.ui.Temperature_Value.setText("0.00")
        self.ui.Time_Value.setText("00:00:00")
        self.ui.alarm_display_label.setStyleSheet('color:default')
        self.ui.alarm_display_label_2.setStyleSheet('color:default')
        self.ui.lineEdit.setText(" ")
        self.ui.lineEdit_2.setText(" ")
    
    def Time_Display(self):
        self.ui.Time_Value.setText(QtCore.QDateTime.currentDateTime().toString("hh:mm:ss"))
        global humidity
        global temp
        humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
        humidity = str(humidity)
        temp = str(temp)
        self.ui.Humidity_Value.setText(humidity)
        self.ui.Temperature_Value.setText(temp)
        
        try:
            self.f_Humidity_Alarm()
        except ValueError:
            pass
        
        try:
            self.f_Temp_Alarm()
        except ValueError:
            pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


