from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from .design.Ventana1 import Ui_MainWindow
from .Events import Events
from .Model import Login


class Ventana1(Events, Ui_MainWindow, QMainWindow):

    def __init__(self, login: Login):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setMaximumHeight(511)
        self.setMinimumHeight(511)
        self.setMaximumWidth(883)
        self.setMinimumWidth(883)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.statusbar.showMessage("© Javier Hidalgo")
        self.boton_salir_login.setIcon(QIcon('ventanas/ventana1/design/asserts/salir.png'))
        self.boton_salir_register.setIcon(QIcon('ventanas/ventana1/design/asserts/salir.png'))
        super(Ventana1, self).__init__()
        self.login = login
