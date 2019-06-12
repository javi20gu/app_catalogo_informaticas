# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Acerca_De.ui',
# licensing of 'Ui_Acerca_De.ui' applies.
#
# Created: Mon Jun 10 11:23:51 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(545, 286)
        Dialog.setStyleSheet("#Dialog {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(20, 20, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(46, 75, 103)")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(66, 88, 108);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(97, 97, 97);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(97, 97, 97);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Hiren\'s Python", None, -1))
        self.titulo.setText(QtWidgets.QApplication.translate("Dialog", "Acerca de", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Hecho por Javier Hidalgo Criado.", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Contacto:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "Email: javihidalgo20@gmail.com", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "GitHub: https://github.com/javi20gu", None, -1))

