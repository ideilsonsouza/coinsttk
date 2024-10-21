import sys
import os
import subprocess
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow
from utils.message import Message
from view.FormTTK import WindowTKK

class AppController :
    def __init__(self) -> None:
        self.window_ttk = None
    
    def initialize(self):
        self.show_window_ttk()
    
    def show_window_ttk(self):
        self.window_ttk = WindowTKK()
        self.window_ttk.show()
  

if __name__ == '__main__':
    main = QApplication(sys.argv)
    controller = AppController()
    controller.initialize()
    sys.exit(main.exec_())
    