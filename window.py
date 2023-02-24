# -*- coding: utf-8 -*-
# /usr/bin/env python3.10

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QListWidget, QListWidgetItem


class MyWindow(QMainWindow):
    def __init__(self, information: dict):
        super().__init__()

        if information.get('info') is not None:
            width = information['info'][0]
            height = information['info'][1]
            title = information['info'][2]
            self.setGeometry(300, 300, width, height)  # -> size
            self.setWindowTitle(title)

        if information.get('button') is not None:
            self.button()

        if information.get('text_field') is not None:
            self.text_field()

        if information.get('create_button_list') is not None:
            self.create_button_list(information['create_button_list'])  # -> element

        self.show()

    def button(self):
        button = QPushButton('CLICK!', self)
        button.setGeometry(300, 300, 100, 50)
        button.clicked.connect(self.on_click)

    def create_button_list(self, items):
        self.list_widget = QListWidget(self)
        self.list_widget.move(100, 50)
        self.list_widget.resize(200, 150)

        for item in items[0]:
            list_item = QListWidgetItem(item)
            self.list_widget.addItem(list_item)

    def text_field(self):
        self.textfield = QLineEdit(self)
        self.textfield.setGeometry(100, 310, 200, 30)

    def on_click(self):
        if information['text_field'] is not None:
            text = self.textfield.text()
            print(f'Text: {text}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    information = {
        'info': [400, 400, 'Window'],  # -> [width, height, title]
        'create_button_list': [['a', 'b', 'c'], []],  # -> [[elements], [setGeometry]]
        'button': True,  # ->  [[setGeometry], title, ]
        'text_field': True  # -> [[setGeometry], ]
    }
    window = MyWindow(information)
    sys.exit(app.exec_())
