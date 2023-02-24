# /bin/usr/env python3.10
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from window import MyWindow

information = {
        'info': [400, 400, 'Window'],  # -> [width, height, title]
        'create_button_list': [['a', 'b', 'c'], [100, 50, 200, 150]],  # -> [[elements], [setGeometry]]
        'button': [300, 300, 100, 50],  # ->  [[setGeometry], title, ]
        'text_field': [100, 310, 200, 30]  # -> [[setGeometry], ]
        }

app = QApplication(sys.argv)
window = MyWindow(information)
sys.exit(app.exec_())
