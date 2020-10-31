# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'soccf.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SOCCF(object):
    def setupUi(self, SOCCF):
        if SOCCF.objectName():
            SOCCF.setObjectName(u"SOCCF")
        SOCCF.resize(545, 217)
        self.centralwidget = QWidget(SOCCF)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pbtn_open_writer = QPushButton(self.centralwidget)
        self.pbtn_open_writer.setObjectName(u"pbtn_open_writer")

        self.horizontalLayout.addWidget(self.pbtn_open_writer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.fcr = QPushButton(self.centralwidget)
        self.fcr.setObjectName(u"fcr")

        self.gridLayout.addWidget(self.fcr, 0, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.fid = QLineEdit(self.centralwidget)
        self.fid.setObjectName(u"fid")

        self.gridLayout.addWidget(self.fid, 0, 1, 1, 1)

        self.fsa = QPushButton(self.centralwidget)
        self.fsa.setObjectName(u"fsa")

        self.gridLayout.addWidget(self.fsa, 2, 2, 1, 1)

        self.fop = QPushButton(self.centralwidget)
        self.fop.setObjectName(u"fop")

        self.gridLayout.addWidget(self.fop, 3, 2, 1, 1)

        self.fin = QTextBrowser(self.centralwidget)
        self.fin.setObjectName(u"fin")

        self.gridLayout.addWidget(self.fin, 2, 1, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        SOCCF.setCentralWidget(self.centralwidget)

        self.retranslateUi(SOCCF)

        QMetaObject.connectSlotsByName(SOCCF)
    # setupUi

    def retranslateUi(self, SOCCF):
        SOCCF.setWindowTitle(QCoreApplication.translate("SOCCF", u"Snapshot of Codemao Community Forum", None))
        self.label_2.setText(QCoreApplication.translate("SOCCF", u"\u6b22\u8fce\u4f7f\u7528\u7f16\u7a0b\u732b\u5e16\u5b50\u5feb\u7167\u521b\u5efa\u5668\uff01(Snapshot of Codemao Community Forum)", None))
        self.label.setText(QCoreApplication.translate("SOCCF", u"\u4f5c\u8005 https://shequ.codemao.cn/user/3819961", None))
        self.pbtn_open_writer.setText(QCoreApplication.translate("SOCCF", u"\u6253\u5f00\u4e3b\u9875", None))
        self.label_4.setText("")
        self.fcr.setText(QCoreApplication.translate("SOCCF", u"\u521b\u5efa\u5feb\u7167", None))
        self.label_3.setText(QCoreApplication.translate("SOCCF", u"\u5e16\u5b50\u53f7\uff1a", None))
        self.fsa.setText(QCoreApplication.translate("SOCCF", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.fop.setText(QCoreApplication.translate("SOCCF", u"\u7acb\u5373\u6253\u5f00", None))
    # retranslateUi

