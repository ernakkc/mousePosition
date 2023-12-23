from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyautogui
import sys


class MousePosition(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.text_posit = "Mouse Position\n\n {} \n\n ------------------------------"
        self.label_position = QLabel()
        self.label_position.setAlignment(Qt.AlignCenter)
        self.label_position.setStyleSheet("color: rgb(0,0,0);font-weight: bold; font-size: 12pt")

        self.text_rgb = "RGB\n\n {}"
        self.label_rgb = QLabel()
        self.label_rgb.setAlignment(Qt.AlignCenter)
        self.label_rgb.setStyleSheet("color: rgb(0,0,0);font-weight: bold; font-size: 12pt")

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label_position)
        vertical_layout.addWidget(self.label_rgb)


        self.setLayout(vertical_layout)
        self.setWindowTitle("Mouse Position")
        self.setMaximumSize(300,200)
        self.setMinimumSize(300,200)


        zamanlayici = QTimer(self)
        zamanlayici.timeout.connect(self.position)
        zamanlayici.start(10)
        self.position()


    def position(self):
        posit = str(pyautogui.position()).replace("Point","")
        self.label_position.setText(self.text_posit.format(posit))

                
        im = pyautogui.screenshot()
        rgb = im.getpixel((pyautogui.position().x, pyautogui.position().y))
        self.label_rgb.setText(self.text_rgb.format(rgb))
        
        
app = QApplication(sys.argv)
widget = MousePosition()
widget.show()
app.exec_()        