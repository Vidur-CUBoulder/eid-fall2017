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
        self.ui.Graph_PB.clicked.connect(self.f_Graph)
        #self.ui.SetAlarm_PB.clicked.connect(self.f_Alarm)
   
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
    
    def Time_Display(self):
        self.ui.Time_Value.setText(QtCore.QDateTime.currentDateTime().toString("hh:mm:ss"))
        humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
        humidity = str("{:0.2f}%".format(humidity))
        y_graph = [humidity]
        temp = str("{:0.2f}*".format(temp))
        self.ui.Humidity_Value.setText(humidity)
        self.ui.Temperature_Value.setText(temp)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


