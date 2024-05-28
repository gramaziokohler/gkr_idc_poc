# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ct_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormCompasTimber(object):
    def setupUi(self, FormCompasTimber):
        FormCompasTimber.setObjectName("FormCompasTimber")
        FormCompasTimber.resize(618, 273)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormCompasTimber.sizePolicy().hasHeightForWidth())
        FormCompasTimber.setSizePolicy(sizePolicy)
        FormCompasTimber.setMinimumSize(QtCore.QSize(618, 193))
        FormCompasTimber.setMaximumSize(QtCore.QSize(524287, 524287))
        font = QtGui.QFont()
        font.setFamily("Arial")
        FormCompasTimber.setFont(font)
        FormCompasTimber.setLayoutDirection(QtCore.Qt.LeftToRight)
        FormCompasTimber.setStyleSheet("QWidget{\n"
"\n"
"background-color: #666666;\n"
"color: #AAAAAA;\n"
"}")
        self.dockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.dockWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 100))
        self.pushButton_3.setStyleSheet("QPushButton::pressed {\n"
"image: url(:/buttons/240318_ct_UI_Icons-54.png);\n"
"}\n"
"\n"
"QPushButton {\n"
"image: url(:/buttons/240318_ct_UI_Icons-57.png);\n"
"\n"
"background-color: transparent;\n"
"}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 100))
        self.pushButton.setStyleSheet("QPushButton::pressed {\n"
"image: url(:/buttons/240318_ct_UI_Icons-54.png);\n"
"}\n"
"\n"
"QPushButton {\n"
"image: url(:/buttons/240318_ct_UI_Icons-53.png);\n"
"\n"
"background-color: transparent;\n"
"}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 100))
        self.pushButton_2.setStyleSheet("QPushButton::pressed {\n"
"image: url(:/buttons/240318_ct_UI_Icons-54.png);\n"
"}\n"
"\n"
"QPushButton {\n"
"image: url(:/buttons/240318_ct_UI_Icons-55.png);\n"
"\n"
"background-color: transparent;\n"
"}\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(300, 25))
        self.label.setStyleSheet("\n"
"QLabel {\n"
"image: url(:/buttons/240318_ct_UI_Icons-59-59-59.png);\n"
"\n"
"background-color: transparent;\n"
"}\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        FormCompasTimber.setWidget(self.dockWidgetContents)

        self.retranslateUi(FormCompasTimber)
        QtCore.QMetaObject.connectSlotsByName(FormCompasTimber)

    def retranslateUi(self, FormCompasTimber):
        _translate = QtCore.QCoreApplication.translate
        FormCompasTimber.setWindowTitle(_translate("FormCompasTimber", "CompasTimber"))

import ui_resources