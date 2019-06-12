from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QDesktopWidget, QMessageBox
from ..ventana2.Ui import VentanaInicio


class Events:

    def __init__(self):
        self.boton_salir_login.clicked.connect(QCoreApplication.instance().quit)
        self.boton_salir_register.clicked.connect(QCoreApplication.instance().quit)
        self.boton_crear_sesion_login.clicked.connect(self.__event_show_crear_sesion)
        self.boton_volver_register.clicked.connect(self.__event_show_volver)
        self.boton_iniciar_sesion_login.clicked.connect(self.__event_iniciar_sesion)
        self.input_password_login.returnPressed.connect(self.__event_iniciar_sesion)
        self.input_email_login.returnPressed.connect(self.__event_iniciar_sesion)

    def __event_iniciar_sesion(self):
        login = self.login.connect(username=self.input_email_login.text(), password=self.input_password_login.text())
        if not login:
            QMessageBox.critical(QMessageBox(), 'Login', 'Email o Contraseña Incorrectos.', QMessageBox.Retry)
        else:
            self.ventanaInicio = VentanaInicio(login=self.login, padre=self)
            self.close()
            self.ventanaInicio.show()

    def __event_show_crear_sesion(self):
        self.stackedWidget.setCurrentIndex(1)
        self.setMaximumHeight(675)
        self.setMinimumHeight(675)
        self.__centrar()

    def __event_show_volver(self):
        self.stackedWidget.setCurrentIndex(0)
        self.setMaximumHeight(511)
        self.setMinimumHeight(511)
        self.__centrar()

    def __centrar(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

