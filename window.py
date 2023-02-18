# -*- coding: utf-8 -*-
# /usr/bin/env python3.10

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QComboBox, QListWidget, QListWidgetItem


class MyWindow(QMainWindow):
    def __init__(self, information: dict):
        super().__init__()

        if information.get('size') is not None:
            width = information['size'][0]
            height = information['size'][1]
            self.setGeometry(300, 300, width, height)  # -> size
            self.setWindowTitle('My Window')

        #        self.button()
        #        self.text_field()
        if information.get('element') is not None:
            self.create_button_list(information['element'])  # -> element

        self.show()

    def button(self):
        button = QPushButton('CLICK!', self)
        button.setGeometry(100, 100, 100, 50)
        button.clicked.connect(self.on_click)

    def create_button_list(self, items):
        self.list_widget = QListWidget(self)
        self.list_widget.move(100, 50)
        self.list_widget.resize(200, 150)

        for item in items:
            list_item = QListWidgetItem(item)
            self.list_widget.addItem(list_item)

    def text_field(self):
        self.textfield = QLineEdit(self)
        self.textfield.setGeometry(300, 100, 200, 30)

    def on_click(self):
        text = self.textfield.text()
        print(f'Text: {text}')

    def button_clicked(self, element):
        print(f'Button {element} wurde angeklickt')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    information = {
        'size': [400, 400],
        'element': ['a', 'b', 'c']
    }
    window = MyWindow(information)
    sys.exit(app.exec_())
