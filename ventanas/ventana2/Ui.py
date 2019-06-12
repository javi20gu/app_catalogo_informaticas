from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QFrame, QMainWindow, QSizePolicy, QStyledItemDelegate, QWidget, QDialog, QLineEdit

from .Events import Events
from .Models import Categories
from .design.card import Ui_Frame_Card
from .design.ventana_principal import Ui_MainWindow
from .design.result import Ui_Frame_Result
from .design.acerca_de import Ui_Dialog
from .design.perfil import Ui_Dialog_Perfil


class Card(Ui_Frame_Card, QFrame):

    def __init__(self, titulo: str, imagen: QPixmap, parent, *args, **kwargs):
        super(Ui_Frame_Card, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.padre = parent
        self.titulo = titulo
        self.label_titulo_card.setText(titulo)
        self.image_card.setPixmap(QPixmap(imagen))
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        self.setMaximumHeight(380)
        self.setMaximumWidth(340)
        self.boton_ver_card.clicked.connect(self.__event_info_product)
        estilo = self.image_card.styleSheet()
        self.image_card.setStyleSheet(estilo + ";padding: 50px")

    def __get_items(self, producto: str) -> dict:
        for text, children in self.padre.items:
            for ad in children:
                if producto.lower() == ad["name"].lower():
                    ad["title"] = text.title()
                    return ad

    def __event_info_product(self):
        self.result = self.__get_items(self.titulo)
        if not self.result:
            self.result = {'id': None, 'name': 'No Encontrado', 'title': ''}
        self.padre.stackedWidget.setCurrentIndex(2)
        for i in range(self.padre.verticalLayout_result.count()):
            widget = self.padre.verticalLayout_result.takeAt(i).widget()
            if widget is not None: 
                widget.deleteLater()

        self.padre.label_categoria_actual.setText('Aplicación')
        from .Ui import Result
        self.padre.verticalLayout_result.addWidget(Result(result=self.result))

# ========================================================================================

class Result(Ui_Frame_Result, QFrame):

    def __init__(self, result: dict) -> None:
        super(Ui_Frame_Result, self).__init__()
        self.setupUi(self)
        self.titulo.setText(result["name"].title())
        self.label.setText(result["title"])
        self.descripcion.setText(result["description"])
        if result["imagenes"]:
            self.imagen1.setPixmap(QPixmap(result["imagenes"][0]))
            self.imagen2.setPixmap(QPixmap(result["imagenes"][1]))
            self.imagen3.setPixmap(QPixmap(result["imagenes"][2]))
            self.imagen4.setPixmap(QPixmap(result["imagenes"][3]))
        else:
            self.imagen1.setPixmap(QPixmap("ventanas/asserts/img/notfound.png"))
            self.imagen2.setPixmap(QPixmap("ventanas/asserts/img/notfound.png"))
            self.imagen3.setPixmap(QPixmap("ventanas/asserts/img/notfound.png"))
            self.imagen4.setPixmap(QPixmap("ventanas/asserts/img/notfound.png"))
        if not result["download"]: 
            self.botonIr.close()
        else:
            self.botonIr.clicked.connect(lambda: self.__event_ir(result))
    
    def __event_ir(self, result):
        from webbrowser import open_new_tab
        open_new_tab(result["download"])
# ========================================================================================

class Perfil(Ui_Dialog_Perfil, QDialog):
    
    def __init__(self, padre) -> None:
        super(Ui_Dialog_Perfil, self).__init__()
        self.setupUi(self)
        email = padre.input_email_login.text()
        password = padre.input_password_login.text()
        self.inputUsuario.setText(email)
        self.inputPassword.setText(password)
        self.isPassword = False
        self.botonMostrarPassword.clicked.connect(self.__event_show_password)

    def __event_show_password(self):
        self.isPassword = not self.isPassword
        if self.isPassword:
            self.inputPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.inputPassword.setEchoMode(QLineEdit.EchoMode.Password)

# ========================================================================================

class AcercaDe(Ui_Dialog, QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)

# ========================================================================================

class VentanaInicio(Events, Ui_MainWindow, QMainWindow):

    STYLE_BUTTON_ACTIVE_1: str = """
        border: 0px solid transparent;
        padding:10;
        color: #3880ff;
        background-color: #f5f7fa
    """

    STYLE_BUTTON_ACTIVE_2: str = """
        color: #3880ff;
        padding:10;
        border: 0px solid transparent;
    """

    def __init__(self, login, padre=None, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        self.result: dict = None
        self.setupUi(self)

        self.ID_BOTON_COPIA_DE_SEGURIDAD: int = self.boton_copia_seguridad.winId()
        self.ID_BOTON_CLONACION: int = self.boton_clonacion.winId()
        self.ID_BOTON_HERR_PARTICIONES: int = self.boton_herr_particiones.winId()
        self.ID_BOTON_HERR_TESTEO: int = self.boton_herr_testeo.winId()
        self.ID_BOTON_UTILES: int = self.boton_utiles.winId()

        self.STYLE_DEFAULT_COPIA_DE_SEGURIDAD: str = self.boton_copia_seguridad.styleSheet()
        self.STYLE_DEFAULT_CLONACION: str = self.boton_clonacion.styleSheet()
        self.STYLE_DEFAULT_HERR_PARTICIONES: str = self.boton_herr_particiones.styleSheet()
        self.STYLE_DEFAULT_HERR_TESTEO: str = self.boton_herr_testeo.styleSheet()
        self.STYLE_DEFAULT_UTILES: str = self.boton_copia_seguridad.styleSheet()

        self.stackedWidget.setCurrentIndex(0)
        self.padre = padre
        self.login = login
        self.cat = Categories()
        delegate = CompleterDelegate(self.input_filter_product)
        self.cat.popup().setStyleSheet(
            """
                color: rgb(78, 91, 106);
                
            """
        )
        self.cat.popup().setItemDelegate(delegate)
        self.input_filter_product.setCompleter(self.cat)
        self.input_filter_product.returnPressed.connect(self.show_app)
        super(VentanaInicio, self).__init__()
        self.items = Categories.items
        self.boton_perfil_menu.triggered.connect(self.__event_show_perfil)

    def __event_show_perfil(self):
        self.ventana = Perfil(self.padre)
        self.ventana.exec_()


class CompleterDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(CompleterDelegate, self).initStyleOption(option, index)
