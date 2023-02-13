# -*- coding: utf-8 -*-
# /usr/bin/env python3.10

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QLabel


class MyWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()

        self.setGeometry(300, 300, width, height)
        self.setWindowTitle('My Window')

        self.button()
        self.text_field()

        self.show()

    def button(self):
        button = QPushButton('CLICK!', self)
        button.setGeometry(100, 100, 100, 50)
        button.clicked.connect(self.on_click)

    def text_field(self):
        self.textfield = QLineEdit(self)
        self.textfield.setGeometry(300, 100, 200, 30)

    def on_click(self):
        text = self.textfield.text()
        print(f'Text: {text}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow(400, 400)
    sys.exit(app.exec_())
