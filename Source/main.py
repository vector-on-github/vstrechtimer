import PyQt5
from PyQt5 import QtCore
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets, uic
import sys
import os
from os import path
import pyautogui
import time
import threading
print("[+] Libraries Initialized...")
print("[+] Executing...")
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        print("[+] Loading UI...")
        uic.loadUi('strechtimer.ui', self)
        self.alertCount = 0
        self.timeinmins = 0
        self.isiton = False
        self.howmuch = self.findChild(QtWidgets.QSpinBox, "howmuch")
        self.menustart = self.findChild(QtWidgets.QAction, "actionStart")
        self.menustart.triggered.connect(self.startTimer)
        self.launch_status_label = self.findChild(QtWidgets.QLabel, 'launch_status')
        self.launch_uptime_label = self.findChild(QtWidgets.QLabel, "launch_uptime")
        self.startbutton = self.findChild(QtWidgets.QPushButton, 'startbtn')
        self.startbutton.clicked.connect(self.startTimer)
        self.killbutton = self.findChild(QtWidgets.QPushButton, "killbtn")
        self.killbutton.clicked.connect(self.terminateProcess)
        self.menuabout = self.findChild(QtWidgets.QAction, "actionAbout_Developer")
        self.menuabout.triggered.connect(self.showAbout)
        self.show()
    
    def showAbout(self):
        print("[+] About: Developed by Vivek Tiwari | MIT")
        pyautogui.alert("Developed by Vivek Tiwari | MIT  \n A friendly reminder app which will remind you to take a strech in interval of times \n Inspired by Sandeep Maheshwari's Caught In The Web series Video 1", "ABOUT")

    def terminateProcess(self):
        sys.exit()

    
    def alertUserforStrech(self):
            print('[+] Firing alert...')
            pyautogui.alert("Please have some strech...")
            self.alertCount = self.alertCount + 1
            self.launch_status_label.setProperty("text", "RUNNING (infinite loop), Alerted : " + str(self.alertCount))
            self.thetimeloop(self.isiton, self.timeinmins)
            print('[+] Loop reinitialized...')

    def thetimeloop(self, isiton, mins):
        if isiton:
            miliseconds = 60000 * int(mins)
            print("[+] firing timeloop of : " + str(miliseconds) + " miliseconds")
            QtCore.QTimer.singleShot(miliseconds, self.alertUserforStrech)
                

    def startTimer(self):
        # This is executed when the button is pressed
        print('[+] Starting Timer...')
        self.timeinmins = self.howmuch.value()
        print("[+] Time in minutes : " + str(self.timeinmins))
        self.isiton = True
        self.launch_status_label.setProperty("text", "RUNNING (infinite loop), Alerted : " + str(self.alertCount))
        self.launch_uptime_label.setProperty("text", str(time.strftime('%Y-%m-%d %I:%M:%S', time.localtime(time.time()))))
        threadfortimefunction = threading.Thread(target=self.thetimeloop(self.isiton, self.timeinmins), args=(1,), daemon=True)
        threadfortimefunction.start()
        self.startbutton.setProperty("enabled", "false")
        self.menustart.setProperty("enabled", "false")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setFixedSize(670, 500)
app.exec_()

print("[+] APP STATUS OK")