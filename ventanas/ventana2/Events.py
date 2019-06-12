from PySide2.QtGui import QPixmap
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QPushButton


class Events:

    def __init__(self):
        self.boton_copia_seguridad.clicked.connect(
            lambda: self.__event_show_categories(self.boton_copia_seguridad)
        )
        self.boton_clonacion.clicked.connect(
            lambda: self.__event_show_categories(self.boton_clonacion)
        )
        self.boton_herr_particiones.clicked.connect(
            lambda: self.__event_show_categories(self.boton_herr_particiones)
        )
        self.boton_herr_testeo.clicked.connect(
            lambda: self.__event_show_categories(self.boton_herr_testeo)
        )
        self.boton_utiles.clicked.connect(
            lambda: self.__event_show_categories(self.boton_utiles)
        )
        self.boton_cerrar_sesion.triggered.connect(self.__event_cerrar_sesion)
        self.actionAcerca_de.triggered.connect(self.__event_show_acerca_de)

    @Slot()
    def __event_cerrar_sesion(self):
        self.login.close_session()
        self.padre.show()
        self.padre.input_email_login.clear()
        self.padre.input_password_login.clear()
        self.padre.input_email_login.setFocus()
        self.padre.stackedWidget.setCurrentIndex(0)
        self.close()
        del self
    
    @Slot()
    def show_app(self) -> None:
        self.result = self.__get_items(self.input_filter_product.text())
        if not self.result:
            self.result = {'id': None, 'name': 'No Encontrado', 'title': '', "description": 'Programa no encontrado', 'download': None, 'imagenes': None}
        self.stackedWidget.setCurrentIndex(2)
        for i in range(self.verticalLayout_result.count()):
            widget = self.verticalLayout_result.takeAt(i).widget()
            if widget is not None: 
                widget.deleteLater()

        self.label_categoria_actual.setText('Busqueda')
        from .Ui import Result
        self.verticalLayout_result.addWidget(Result(result=self.result))

    def __get_items(self, producto: str) -> dict:
        for text, children in self.items:
            for ad in children:
                if self.input_filter_product.text().lower() == ad["name"].lower():
                    ad["title"] = text.title()
                    return ad

    @Slot(QPushButton)
    def __event_show_categories(self, button: QPushButton):
        from .Ui import Card

        self.__reset_style()
        self.stackedWidget.setCurrentIndex(1)

        if button.winId() == self.ID_BOTON_COPIA_DE_SEGURIDAD:
            data: list = self.items[0][1]
            num_elementos: int = len(data)
            self.label_categoria_actual.setText("Copia de Seguridad")
            self.boton_copia_seguridad.setStyleSheet(self.STYLE_BUTTON_ACTIVE_1)

            for num_datos in range(num_elementos):
                if num_datos < 3:
                    self.gridLayout.addWidget(Card(data[num_datos]["name"].title(), QPixmap(data[num_datos]["logo"]), self), num_datos, 0)
                elif num_datos > 3:
                    for i in range(2):
                        self.gridLayout.addWidget(Card(data[i+3]["name"].title(), QPixmap(data[i+3]["logo"]), self), i, 1)

        elif button.winId() == self.ID_BOTON_CLONACION:
            self.label_categoria_actual.setText("Clonación")
            self.boton_clonacion.setStyleSheet(self.STYLE_BUTTON_ACTIVE_2)
            self.gridLayout.removeWidget(self.gridLayout.widget())

            data: list = self.items[1][1]
            num_elementos: int = len(data)

            for num_datos in range(num_elementos):
                if num_datos < 3:
                    self.gridLayout.addWidget(Card(data[num_datos]["name"].title(), QPixmap(data[num_datos]["logo"]), self), num_datos, 0)
                elif num_datos > 3:
                    for i in range(2):
                        self.gridLayout.addWidget(Card(data[i+3]["name"].title(), QPixmap(data[i+3]["logo"]), self), i, 1)

        elif button.winId() == self.ID_BOTON_HERR_TESTEO:
            data: list = self.items[2][1]
            num_elementos: int = len(data)

            self.label_categoria_actual.setText("Herramientas de Testeo")
            self.boton_herr_testeo.setStyleSheet(self.STYLE_BUTTON_ACTIVE_1)

            for num_datos in range(num_elementos):
                if num_datos < 3:
                    self.gridLayout.addWidget(Card(data[num_datos]["name"].title(), QPixmap(data[num_datos]["logo"]), self), num_datos, 0)
                elif num_datos > 3:
                    for i in range(2):
                        self.gridLayout.addWidget(Card(data[i+3]["name"].title(), QPixmap(data[i+3]["logo"]), self), i, 1)

        elif button.winId() == self.ID_BOTON_HERR_PARTICIONES:

            data: list = self.items[3][1]
            num_elementos: int = len(data)

            self.label_categoria_actual.setText("Herramientas de Particiones")
            self.boton_herr_particiones.setStyleSheet(self.STYLE_BUTTON_ACTIVE_2)

            for num_datos in range(num_elementos):
                if num_datos < 3:
                    self.gridLayout.addWidget(Card(data[num_datos]["name"].title(), QPixmap(data[num_datos]["logo"]), self), num_datos, 0)
                elif num_datos > 3:
                    for i in range(2):
                        self.gridLayout.addWidget(Card(data[i+3]["name"].title(), QPixmap(data[i+3]["logo"]), self), i, 1)

        elif button.winId() == self.ID_BOTON_UTILES:

            data: list = self.items[4][1]
            num_elementos: int = len(data)

            self.label_categoria_actual.setText("Utiles")
            self.boton_utiles.setStyleSheet(self.STYLE_BUTTON_ACTIVE_1)

            for num_datos in range(num_elementos):
                if num_datos < 3:
                    self.gridLayout.addWidget(Card(data[num_datos]["name"].title(), QPixmap(data[num_datos]["logo"]), self), num_datos, 0)
                elif num_datos > 3:
                    for i in range(2):
                        self.gridLayout.addWidget(Card(data[i+3]["name"].title(), QPixmap(data[i+3]["logo"]), self), i, 1)

        else:
            raise RuntimeError('Id del Elemnto Desconocido')

    def __reset_style(self):
        self.boton_copia_seguridad.setStyleSheet(self.STYLE_DEFAULT_COPIA_DE_SEGURIDAD)
        self.boton_clonacion.setStyleSheet(self.STYLE_DEFAULT_CLONACION)
        self.boton_herr_particiones.setStyleSheet(self.STYLE_DEFAULT_HERR_PARTICIONES)
        self.boton_herr_testeo.setStyleSheet(self.STYLE_DEFAULT_HERR_TESTEO)
        self.boton_utiles.setStyleSheet(self.STYLE_DEFAULT_UTILES)

    @Slot()
    def show(self):
        self.statusbar.showMessage("Bienvenido {}".format(self.login.get_username()), 8000)
        super().show()

    @Slot()
    def __event_show_acerca_de(self):
        from .Ui import AcercaDe
        self.ventana = AcercaDe()
        self.ventana.exec_()
