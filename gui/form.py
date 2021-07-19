# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ToxicMusicPlayer(object):
    def setupUi(self, ToxicMusicPlayer):
        if not ToxicMusicPlayer.objectName():
            ToxicMusicPlayer.setObjectName(u"ToxicMusicPlayer")
        ToxicMusicPlayer.resize(800, 610)
        ToxicMusicPlayer.setStyleSheet(u"background-image: url(source/image/backGround.jpg);")
        self.centralwidget = QWidget(ToxicMusicPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 370, 791, 191))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 5, 2, 1)

        self.timeSlider = QSlider(self.gridLayoutWidget)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.timeSlider, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 5, 0, 1, 3)

        self.playNext = QPushButton(self.gridLayoutWidget)
        self.playNext.setObjectName(u"playNext")
        self.playNext.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.playNext, 0, 2, 1, 1)

        self.Pause = QPushButton(self.gridLayoutWidget)
        self.Pause.setObjectName(u"Pause")
        self.Pause.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.Pause, 0, 1, 1, 1)

        self.playBack = QPushButton(self.gridLayoutWidget)
        self.playBack.setObjectName(u"playBack")
        self.playBack.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.playBack, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 3)

        self.playStop = QPushButton(self.gridLayoutWidget)
        self.playStop.setObjectName(u"playStop")
        self.playStop.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.playStop, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 4)

        self.timeAfterStart = QLabel(self.gridLayoutWidget)
        self.timeAfterStart.setObjectName(u"timeAfterStart")
        self.timeAfterStart.setAutoFillBackground(False)
        self.timeAfterStart.setStyleSheet(u"ackground-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.timeAfterStart, 1, 1, 1, 1)

        self.volumeSlider = QSlider(self.gridLayoutWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.volumeSlider, 1, 6, 1, 1)

        self.songTime = QLabel(self.gridLayoutWidget)
        self.songTime.setObjectName(u"songTime")
        self.songTime.setStyleSheet(u"ackground-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.songTime, 1, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 2, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(190, 0, 400, 360))
        self.graphicsView.setStyleSheet(u"ackground-image: url(source/image/music.jpeg);")
        ToxicMusicPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ToxicMusicPlayer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        ToxicMusicPlayer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ToxicMusicPlayer)
        self.statusbar.setObjectName(u"statusbar")
        ToxicMusicPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(ToxicMusicPlayer)

        QMetaObject.connectSlotsByName(ToxicMusicPlayer)
    # setupUi

    def retranslateUi(self, ToxicMusicPlayer):
        ToxicMusicPlayer.setWindowTitle(QCoreApplication.translate("ToxicMusicPlayer", u"ToxicMusicPlayer", None))
        self.playNext.setText(QCoreApplication.translate("ToxicMusicPlayer", u">>", None))
        self.Pause.setText(QCoreApplication.translate("ToxicMusicPlayer", u"Pause", None))
        self.playBack.setText(QCoreApplication.translate("ToxicMusicPlayer", u"<<", None))
        self.playStop.setText(QCoreApplication.translate("ToxicMusicPlayer", u"Stop", None))
        self.timeAfterStart.setText(QCoreApplication.translate("ToxicMusicPlayer", u"0:00", None))
        self.songTime.setText(QCoreApplication.translate("ToxicMusicPlayer", u"0:00", None))
    # retranslateUi

