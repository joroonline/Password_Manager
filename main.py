# /bin/usr/env python3.10
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from window import MyWindow


app = QApplication(sys.argv)
window = MyWindow(400, 400)
sys.exit(app.exec_())
