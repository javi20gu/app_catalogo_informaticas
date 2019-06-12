# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Ventana1.ui',
# licensing of 'Ui_Ventana1.ui' applies.
#
# Created: Mon Jun 10 11:10:04 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_iniciar_sesion = QtWidgets.QWidget()
        self.page_iniciar_sesion.setObjectName("page_iniciar_sesion")
        self.input_email_login = QtWidgets.QLineEdit(self.page_iniciar_sesion)
        self.input_email_login.setGeometry(QtCore.QRect(40, 160, 801, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.input_email_login.setFont(font)
        self.input_email_login.setStyleSheet("background-color: rgb(247, 248, 250);\n"
"border: 0px solid #eee;\n"
"border-radius: 7px;\n"
"padding-left: 10px")
        self.input_email_login.setClearButtonEnabled(True)
        self.input_email_login.setObjectName("input_email_login")
        self.etiqueta_login = QtWidgets.QLabel(self.page_iniciar_sesion)
        self.etiqueta_login.setGeometry(QtCore.QRect(260, 40, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(33)
        font.setWeight(75)
        font.setBold(True)
        self.etiqueta_login.setFont(font)
        self.etiqueta_login.setStyleSheet("color: rgb(31, 36, 41);")
        self.etiqueta_login.setAlignment(QtCore.Qt.AlignCenter)
        self.etiqueta_login.setObjectName("etiqueta_login")
        self.boton_crear_sesion_login = QtWidgets.QPushButton(self.page_iniciar_sesion)
        self.boton_crear_sesion_login.setGeometry(QtCore.QRect(470, 360, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.boton_crear_sesion_login.setFont(font)
        self.boton_crear_sesion_login.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_crear_sesion_login.setStyleSheet("background-color: #E1E7FA;\n"
"border: 0px solid #333;\n"
"border-radius:25px;\n"
"color: #1F2429")
        self.boton_crear_sesion_login.setObjectName("boton_crear_sesion_login")
        self.input_password_login = QtWidgets.QLineEdit(self.page_iniciar_sesion)
        self.input_password_login.setGeometry(QtCore.QRect(40, 240, 801, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.input_password_login.setFont(font)
        self.input_password_login.setStyleSheet("background-color: rgb(247, 248, 250);\n"
"border: 0px solid #eee;\n"
"border-radius: 7px;\n"
"padding-left: 10px")
        self.input_password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password_login.setClearButtonEnabled(True)
        self.input_password_login.setObjectName("input_password_login")
        self.boton_iniciar_sesion_login = QtWidgets.QPushButton(self.page_iniciar_sesion)
        self.boton_iniciar_sesion_login.setGeometry(QtCore.QRect(200, 360, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.boton_iniciar_sesion_login.setFont(font)
        self.boton_iniciar_sesion_login.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_iniciar_sesion_login.setStyleSheet("background-color: rgb(10, 63, 255);\n"
"border: 0px solid #333;\n"
"border-radius:25px;\n"
"color: #fff")
        self.boton_iniciar_sesion_login.setObjectName("boton_iniciar_sesion_login")
        self.boton_salir_login = QtWidgets.QPushButton(self.page_iniciar_sesion)
        self.boton_salir_login.setGeometry(QtCore.QRect(800, 0, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.boton_salir_login.setFont(font)
        self.boton_salir_login.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_salir_login.setStyleSheet("QPushButton {\n"
"    border: 0px solid #333;\n"
"outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(247, 248, 250)\n"
"}")
        self.boton_salir_login.setText("")
        self.boton_salir_login.setIconSize(QtCore.QSize(25, 25))
        self.boton_salir_login.setCheckable(False)
        self.boton_salir_login.setObjectName("boton_salir_login")
        self.stackedWidget.addWidget(self.page_iniciar_sesion)
        self.page_crear_sesion = QtWidgets.QWidget()
        self.page_crear_sesion.setObjectName("page_crear_sesion")
        self.input_nombre_apellidos_register = QtWidgets.QLineEdit(self.page_crear_sesion)
        self.input_nombre_apellidos_register.setGeometry(QtCore.QRect(40, 170, 801, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.input_nombre_apellidos_register.setFont(font)
        self.input_nombre_apellidos_register.setStyleSheet("background-color: rgb(247, 248, 250);\n"
"border: 0px solid #eee;\n"
"border-radius: 7px;\n"
"padding-left: 10px")
        self.input_nombre_apellidos_register.setClearButtonEnabled(True)
        self.input_nombre_apellidos_register.setObjectName("input_nombre_apellidos_register")
        self.etiqueta_crear_sesion_register = QtWidgets.QLabel(self.page_crear_sesion)
        self.etiqueta_crear_sesion_register.setGeometry(QtCore.QRect(290, 49, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(33)
        font.setWeight(75)
        font.setBold(True)
        self.etiqueta_crear_sesion_register.setFont(font)
        self.etiqueta_crear_sesion_register.setStyleSheet("color: rgb(31, 36, 41);")
        self.etiqueta_crear_sesion_register.setAlignment(QtCore.Qt.AlignCenter)
        self.etiqueta_crear_sesion_register.setObjectName("etiqueta_crear_sesion_register")
        self.input_password_register = QtWidgets.QLineEdit(self.page_crear_sesion)
        self.input_password_register.setGeometry(QtCore.QRect(40, 409, 801, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.input_password_register.setFont(font)
        self.input_password_register.setStyleSheet("background-color: rgb(247, 248, 250);\n"
"border: 0px solid #eee;\n"
"border-radius: 7px;\n"
"padding-left: 10px")
        self.input_password_register.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password_register.setClearButtonEnabled(True)
        self.input_password_register.setObjectName("input_password_register")
        self.input_edad_register = QtWidgets.QSpinBox(self.page_crear_sesion)
        self.input_edad_register.setGeometry(QtCore.QRect(40, 250, 801, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.input_edad_register.setFont(font)
        self.input_edad_register.setStyleSheet("background-color: rgb(247, 248, 250);\n"
"border: 0px solid #eee;\n"
"border-radius: 7px;\n"
"padding-left: 10px")
        self.input_edad_register.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.input_edad_register.setAccelerated(True)
        self.input_edad_register.setObjectName("input_edad_register")
        self.boton_crear_sesion_register = QtWidgets.QPushButton(self.page_crear_sesion)
        self.boton_crear_sesion_register.setGeometry(QtCore.QRect(330, 529, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.boton_crear_sesion_register.setFont(font)
        self.boton_crear_sesion_register.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_crear_sesion_register.setStyleSheet("background-color: rgb(10, 63, 255);\n"
"border: 0px solid #333;\n"
"border-radius:25px;\n"
"color: #fff")
        self.boton_crear_sesion_register.setObjectName("boton_crear_sesion_register")
        self.boton_volver_register = QtWidgets.QPushButton(self.page_crear_sesion)
        self.boton_volver_register.setGeometry(QtCore.QRect(350, 599, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.boton_volver_register.setFont(font)
        self.boton_volver_register.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_volver_register.setStyleSheet("border: 0px solid #333;\n"
"\n"
"color:  rgb(181, 186, 200)")
        self.boton_volver_register.setObjectName("boton_volver_register")
        self.input_email_register = QtWidgets.QLineEdit(self.page_crear_sesion)
        self.input_email_register.setGeometry(QtCore.QRect(40, 329, 801, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.input_email_register.setFont(font)
        self.input_email_register.setStyleSheet("background-color: rgb(247, 248, 250);\n"
"border: 0px solid #eee;\n"
"border-radius: 7px;\n"
"padding-left: 10px")
        self.input_email_register.setClearButtonEnabled(True)
        self.input_email_register.setObjectName("input_email_register")
        self.boton_salir_register = QtWidgets.QPushButton(self.page_crear_sesion)
        self.boton_salir_register.setGeometry(QtCore.QRect(800, 0, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.boton_salir_register.setFont(font)
        self.boton_salir_register.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_salir_register.setStyleSheet("QPushButton {\n"
"    border: 0px solid #333;\n"
"outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(247, 248, 250)\n"
"}")
        self.boton_salir_register.setText("")
        self.boton_salir_register.setIconSize(QtCore.QSize(25, 25))
        self.boton_salir_register.setCheckable(False)
        self.boton_salir_register.setObjectName("boton_salir_register")
        self.stackedWidget.addWidget(self.page_crear_sesion)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("background-color: rgb(122, 122, 122);\n"
"color: rgb(236, 236, 236)")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.input_email_login, self.input_password_login)
        MainWindow.setTabOrder(self.input_password_login, self.boton_iniciar_sesion_login)
        MainWindow.setTabOrder(self.boton_iniciar_sesion_login, self.boton_crear_sesion_login)
        MainWindow.setTabOrder(self.boton_crear_sesion_login, self.boton_salir_login)
        MainWindow.setTabOrder(self.boton_salir_login, self.input_nombre_apellidos_register)
        MainWindow.setTabOrder(self.input_nombre_apellidos_register, self.input_edad_register)
        MainWindow.setTabOrder(self.input_edad_register, self.input_email_register)
        MainWindow.setTabOrder(self.input_email_register, self.input_password_register)
        MainWindow.setTabOrder(self.input_password_register, self.boton_crear_sesion_register)
        MainWindow.setTabOrder(self.boton_crear_sesion_register, self.boton_volver_register)
        MainWindow.setTabOrder(self.boton_volver_register, self.boton_salir_register)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Hiren\'s Python", None, -1))
        self.input_email_login.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Introduzca su Email", None, -1))
        self.etiqueta_login.setText(QtWidgets.QApplication.translate("MainWindow", "Hiren\'s Python", None, -1))
        self.boton_crear_sesion_login.setText(QtWidgets.QApplication.translate("MainWindow", "Crear Sesión", None, -1))
        self.input_password_login.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Introduzca su Contraseña", None, -1))
        self.boton_iniciar_sesion_login.setText(QtWidgets.QApplication.translate("MainWindow", "Iniciar Sesión", None, -1))
        self.input_nombre_apellidos_register.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Introduzca su Nombre y Apellidos", None, -1))
        self.etiqueta_crear_sesion_register.setText(QtWidgets.QApplication.translate("MainWindow", "Crear Sesión", None, -1))
        self.input_password_register.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Introduzca su Contraseña", None, -1))
        self.input_edad_register.setSuffix(QtWidgets.QApplication.translate("MainWindow", " años", None, -1))
        self.input_edad_register.setPrefix(QtWidgets.QApplication.translate("MainWindow", "Introduzca su Edad: ", None, -1))
        self.boton_crear_sesion_register.setText(QtWidgets.QApplication.translate("MainWindow", "Crear Sesión", None, -1))
        self.boton_volver_register.setText(QtWidgets.QApplication.translate("MainWindow", "Volver", None, -1))
        self.input_email_register.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Introduzca su Email", None, -1))

