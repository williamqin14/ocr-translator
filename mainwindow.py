# This Python file uses the following encoding: utf-8
import sys
from tesseract import ocr
from lanmodel import aiQuery
from screenshot import getScreenshot
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QImage

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot(str)
    def screenshot(self):
        print('hi')
        file = './output.png'
        getScreenshot()
        self.ui.Image.setPixmap(QPixmap(file))
        print('image printed')
        text = ocr(file)
        self.ui.EngBrowser.setText(text)

    @Slot(str)
    def translate(self):
        text = self.ui.EngBrowser.toPlainText()
        translatedText = aiQuery(text)
        self.ui.JapBrowser.setText(translatedText)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
