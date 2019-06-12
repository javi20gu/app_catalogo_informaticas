# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Perfil.ui',
# licensing of 'Ui_Perfil.ui' applies.
#
# Created: Tue Jun 11 11:19:48 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Perfil(object):
    def setupUi(self, Dialog_Perfil):
        Dialog_Perfil.setObjectName("Dialog_Perfil")
        Dialog_Perfil.resize(605, 307)
        Dialog_Perfil.setMinimumSize(QtCore.QSize(605, 307))
        Dialog_Perfil.setMaximumSize(QtCore.QSize(605, 307))
        Dialog_Perfil.setStyleSheet("#Dialog_Perfil{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        Dialog_Perfil.setSizeGripEnabled(True)
        Dialog_Perfil.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog_Perfil)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titulo = QtWidgets.QLabel(Dialog_Perfil)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(25)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(35, 52, 74);")
        self.titulo.setObjectName("titulo")
        self.verticalLayout_3.addWidget(self.titulo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelUsuario = QtWidgets.QLabel(Dialog_Perfil)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUsuario.sizePolicy().hasHeightForWidth())
        self.labelUsuario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.labelUsuario.setFont(font)
        self.labelUsuario.setStyleSheet("color: rgb(139, 139, 139)")
        self.labelUsuario.setObjectName("labelUsuario")
        self.verticalLayout_2.addWidget(self.labelUsuario)
        spacerItem1 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.inputUsuario = QtWidgets.QLineEdit(Dialog_Perfil)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.inputUsuario.setFont(font)
        self.inputUsuario.setStyleSheet("border: 1px solid rgb(226, 234, 245);\n"
"border-radius:2px;\n"
"padding: 2px 3px;")
        self.inputUsuario.setFrame(False)
        self.inputUsuario.setReadOnly(True)
        self.inputUsuario.setObjectName("inputUsuario")
        self.verticalLayout_2.addWidget(self.inputUsuario)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPassword = QtWidgets.QLabel(Dialog_Perfil)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPassword.sizePolicy().hasHeightForWidth())
        self.labelPassword.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.labelPassword.setFont(font)
        self.labelPassword.setStyleSheet("color: rgb(139, 139, 139)")
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout.addWidget(self.labelPassword)
        spacerItem3 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.inputPassword = QtWidgets.QLineEdit(Dialog_Perfil)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(11)
        self.inputPassword.setFont(font)
        self.inputPassword.setStyleSheet("border: 1px solid rgb(226, 234, 245);\n"
"border-radius:2px;\n"
"padding: 2px 3px;")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setReadOnly(True)
        self.inputPassword.setObjectName("inputPassword")
        self.verticalLayout.addWidget(self.inputPassword)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.botonMostrarPassword = QtWidgets.QCheckBox(Dialog_Perfil)
        self.botonMostrarPassword.setCursor(QtCore.Qt.PointingHandCursor)
        self.botonMostrarPassword.setStyleSheet("#botonMostrarPassword {\n"
"color: rgb(95, 107, 115)\n"
"}\n"
"#botonMostrarPassword::indicator:unchecked {\n"
"border: 1px solid rgb(191, 204, 213)\n"
"}")
        self.botonMostrarPassword.setObjectName("botonMostrarPassword")
        self.verticalLayout_3.addWidget(self.botonMostrarPassword)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Perfil)
        self.buttonBox.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.labelUsuario.setBuddy(self.inputUsuario)
        self.labelPassword.setBuddy(self.inputPassword)

        self.retranslateUi(Dialog_Perfil)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_Perfil.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_Perfil.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Perfil)

    def retranslateUi(self, Dialog_Perfil):
        Dialog_Perfil.setWindowTitle(QtWidgets.QApplication.translate("Dialog_Perfil", "Hiren\'s Python", None, -1))
        self.titulo.setText(QtWidgets.QApplication.translate("Dialog_Perfil", "Cuenta", None, -1))
        self.labelUsuario.setText(QtWidgets.QApplication.translate("Dialog_Perfil", "Usuario:", None, -1))
        self.labelPassword.setText(QtWidgets.QApplication.translate("Dialog_Perfil", "Contraseña:", None, -1))
        self.botonMostrarPassword.setText(QtWidgets.QApplication.translate("Dialog_Perfil", "Mostrar Contraseña", None, -1))

