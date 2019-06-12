# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_card.ui',
# licensing of 'Ui_card.ui' applies.
#
# Created: Fri Jun  7 15:05:49 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Frame_Card(object):
    def setupUi(self, Frame_Card):
        Frame_Card.setObjectName("Frame_Card")
        Frame_Card.resize(249, 211)
        Frame_Card.setStyleSheet("QFrame {\n"
"border: 1px solid #edf2f6;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame_Card)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_titulo_card = QtWidgets.QLabel(Frame_Card)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_titulo_card.setFont(font)
        self.label_titulo_card.setStyleSheet("border: 0px solid #333;")
        self.label_titulo_card.setText("")
        self.label_titulo_card.setObjectName("label_titulo_card")
        self.verticalLayout.addWidget(self.label_titulo_card)
        self.image_card = QtWidgets.QLabel(Frame_Card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_card.sizePolicy().hasHeightForWidth())
        self.image_card.setSizePolicy(sizePolicy)
        self.image_card.setText("")
        self.image_card.setScaledContents(True)
        self.image_card.setAlignment(QtCore.Qt.AlignCenter)
        self.image_card.setObjectName("image_card")
        self.verticalLayout.addWidget(self.image_card)
        self.boton_ver_card = QtWidgets.QPushButton(Frame_Card)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        self.boton_ver_card.setFont(font)
        self.boton_ver_card.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_ver_card.setStyleSheet("border: 1px solid rgb(142, 231, 255);\n"
"padding: 7px;\n"
"color:rgb(109, 174, 194)")
        self.boton_ver_card.setObjectName("boton_ver_card")
        self.verticalLayout.addWidget(self.boton_ver_card)

        self.retranslateUi(Frame_Card)
        QtCore.QMetaObject.connectSlotsByName(Frame_Card)

    def retranslateUi(self, Frame_Card):
        Frame_Card.setWindowTitle(QtWidgets.QApplication.translate("Frame_Card", "Frame", None, -1))
        self.boton_ver_card.setText(QtWidgets.QApplication.translate("Frame_Card", "Ver", None, -1))

