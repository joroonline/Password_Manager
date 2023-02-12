# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()

        self.setGeometry(300, 300, width, height)
        self.setWindowTitle('My Window')
        self.uiComponents()

        self.show()

    def uiComponents(self):
        button = QPushButton('CLICK!', self)
        button.setGeometry(300, 300, 100, 100)
        button.clicked.connect(self.on_click())

    def on_click(self):
        print('Button was clicked')
