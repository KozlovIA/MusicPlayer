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
        ToxicMusicPlayer.resize(802, 610)
        ToxicMusicPlayer.setStyleSheet(u"background-image: url(source/image/backForForm.jpg);")
        self.centralwidget = QWidget(ToxicMusicPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 370, 791, 191))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 2, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 5, 0, 1, 3)

        self.playNext = QPushButton(self.gridLayoutWidget)
        self.playNext.setObjectName(u"playNext")
        self.playNext.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(0, 255, 255);\n"
"")

        self.gridLayout_2.addWidget(self.playNext, 0, 2, 1, 1)

        self.Play_Pause = QPushButton(self.gridLayoutWidget)
        self.Play_Pause.setObjectName(u"Play_Pause")
        self.Play_Pause.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(0, 255, 255);")

        self.gridLayout_2.addWidget(self.Play_Pause, 0, 1, 1, 1)

        self.playBack = QPushButton(self.gridLayoutWidget)
        self.playBack.setObjectName(u"playBack")
        self.playBack.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(0, 255, 255);")

        self.gridLayout_2.addWidget(self.playBack, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 3)

        self.playStop = QPushButton(self.gridLayoutWidget)
        self.playStop.setObjectName(u"playStop")
        self.playStop.setStyleSheet(u"background-image: url(source/image/backButton.jpg);\n"
"color: rgb(0, 255, 255);")

        self.gridLayout_2.addWidget(self.playStop, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 4)

        self.timeAfterStart = QLabel(self.gridLayoutWidget)
        self.timeAfterStart.setObjectName(u"timeAfterStart")
        self.timeAfterStart.setAutoFillBackground(False)
        self.timeAfterStart.setStyleSheet(u"ackground-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.timeAfterStart, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 5, 3, 1)

        self.timeSlider = QSlider(self.gridLayoutWidget)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.timeSlider, 1, 2, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 2)

        self.songTime = QLabel(self.gridLayoutWidget)
        self.songTime.setObjectName(u"songTime")
        self.songTime.setStyleSheet(u"ackground-image: url(source/image/backButton.jpg);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.songTime, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 2)

        self.volumeSlider = QSlider(self.gridLayoutWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.volumeSlider, 1, 6, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(230, 0, 291, 241))
        self.graphicsView.setStyleSheet(u"ackground-image: url(source/image/music.jpeg);")
        self.AddMusic = QLineEdit(self.centralwidget)
        self.AddMusic.setObjectName(u"AddMusic")
        self.AddMusic.setGeometry(QRect(220, 270, 301, 41))
        self.label_WriteNameorUrl = QLabel(self.centralwidget)
        self.label_WriteNameorUrl.setObjectName(u"label_WriteNameorUrl")
        self.label_WriteNameorUrl.setGeometry(QRect(220, 250, 181, 20))
        self.AddMusicButton = QPushButton(self.centralwidget)
        self.AddMusicButton.setObjectName(u"AddMusicButton")
        self.AddMusicButton.setEnabled(True)
        self.AddMusicButton.setGeometry(QRect(530, 280, 75, 23))
        ToxicMusicPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ToxicMusicPlayer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 21))
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
        self.Play_Pause.setText(QCoreApplication.translate("ToxicMusicPlayer", u"Play", None))
        self.playBack.setText(QCoreApplication.translate("ToxicMusicPlayer", u"<<", None))
        self.playStop.setText(QCoreApplication.translate("ToxicMusicPlayer", u"Stop", None))
        self.timeAfterStart.setText(QCoreApplication.translate("ToxicMusicPlayer", u"0:00", None))
        self.lineEdit.setText(QCoreApplication.translate("ToxicMusicPlayer", u"Now playing: none", None))
        self.songTime.setText(QCoreApplication.translate("ToxicMusicPlayer", u"0:00", None))
        self.AddMusic.setText("")
        self.label_WriteNameorUrl.setText(QCoreApplication.translate("ToxicMusicPlayer", u"Write the name or URL", None))
        self.AddMusicButton.setText(QCoreApplication.translate("ToxicMusicPlayer", u"Add to queue", None))
    # retranslateUi

