import sys
import os

import utility_controller as uc

HERE = os.path.dirname(__file__)
SITE_PACKAGES = os.path.join(HERE, "Lib", "site-packages")
# COMPAS_TIMBER = r"C:\Users\ckasirer\repos\compas_timber\src"
# COMPAS_CADWORK = r"C:\Users\ckasirer\repos\compas_cadwork\src"

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


for path in [HERE, SITE_PACKAGES]:#, COMPAS_TIMBER, COMPAS_CADWORK]:
    if path not in sys.path:
        sys.path.append(path)

from controller import Controller
from ui import UiMainWindow

cadwork_window = QWidget.find(uc.get_3d_hwnd())

if __name__ == '__main__':
    def excepthook_(type_, value, traceback):
        import traceback
        print(f"type_:{type_} value: {value} traceback: {traceback}")
        traceback.print_exception(type_, value, traceback)
    sys.excepthook = excepthook_
    
    controller = Controller()
    dialog = UiMainWindow(controller)
    cadwork_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dialog)
    dialog.show()