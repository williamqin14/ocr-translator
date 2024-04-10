# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(490, 60, 160, 116))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Screenshot_button = QPushButton(self.verticalLayoutWidget)
        self.Screenshot_button.setObjectName(u"Screenshot_button")

        self.verticalLayout.addWidget(self.Screenshot_button)

        self.Translate_button = QPushButton(self.verticalLayoutWidget)
        self.Translate_button.setObjectName(u"Translate_button")

        self.verticalLayout.addWidget(self.Translate_button)

        self.Image = QLabel(self.centralwidget)
        self.Image.setObjectName(u"Image")
        self.Image.setGeometry(QRect(90, 50, 321, 141))
        self.Image.setFrameShape(QFrame.Box)
        self.Image.setScaledContents(True)
        self.Image.setAlignment(Qt.AlignCenter)
        self.Image.setWordWrap(False)
        self.EngBrowser = QTextBrowser(self.centralwidget)
        self.EngBrowser.setObjectName(u"EngBrowser")
        self.EngBrowser.setGeometry(QRect(80, 240, 621, 121))
        self.EngBrowser.setReadOnly(False)
        self.JapBrowser = QTextBrowser(self.centralwidget)
        self.JapBrowser.setObjectName(u"JapBrowser")
        self.JapBrowser.setGeometry(QRect(80, 390, 621, 131))
        self.Logger = QLabel(self.centralwidget)
        self.Logger.setObjectName(u"Logger")
        self.Logger.setGeometry(QRect(80, 210, 621, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Screenshot_button.clicked.connect(MainWindow.screenshot)
        self.Translate_button.clicked.connect(MainWindow.translate)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.Screenshot_button.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.Translate_button.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.Image.setText(QCoreApplication.translate("MainWindow", u"Take a screen shot", None))
        self.Logger.setText("")
    # retranslateUi

