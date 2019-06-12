# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Ventana_Principal.ui',
# licensing of 'Ui_Ventana_Principal.ui' applies.
#
# Created: Tue Jun 11 11:21:24 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 646)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu = QtWidgets.QFrame(self.centralwidget)
        self.menu.setStyleSheet("background-color: #FFFFFF;\n"
"border: 1px solid #edf2f6;\n"
"border-top-color: rgb(255, 255, 255);\n"
"")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_categorias = QtWidgets.QLabel(self.menu)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(13)
        self.label_categorias.setFont(font)
        self.label_categorias.setStyleSheet("color: #020814;\n"
"border-color: transparent;")
        self.label_categorias.setTextFormat(QtCore.Qt.PlainText)
        self.label_categorias.setScaledContents(True)
        self.label_categorias.setAlignment(QtCore.Qt.AlignCenter)
        self.label_categorias.setMargin(7)
        self.label_categorias.setObjectName("label_categorias")
        self.verticalLayout_6.addWidget(self.label_categorias)
        self.line = QtWidgets.QFrame(self.menu)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setStyleSheet("background-color: transparent;\n"
"color:  rgb(190, 181, 255);\n")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(18, 14, 18, 14)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_filter_product = QtWidgets.QLineEdit(self.menu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_filter_product.setFont(font)
        self.input_filter_product.setStyleSheet("color: rgb(78, 91, 106);\n"
"border: 2px solid #edf2f6;\n"
"border-radius: 4px;\n"
"padding: 7px;\n"
"")
        self.input_filter_product.setText("")
        self.input_filter_product.setObjectName("input_filter_product")
        self.verticalLayout.addWidget(self.input_filter_product)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.line_3 = QtWidgets.QFrame(self.menu)
        self.line_3.setMinimumSize(QtCore.QSize(0, 0))
        self.line_3.setStyleSheet("background-color: transparent;\n"
"color:  rgb(190, 181, 255);\n")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem)
        self.boton_copia_seguridad = QtWidgets.QPushButton(self.menu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_copia_seguridad.setFont(font)
        self.boton_copia_seguridad.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_copia_seguridad.setStyleSheet("QPushButton {\n"
"border: 0px solid rgb(170, 255, 255);\n"
"padding:10;\n"
"color:rgb(198, 198, 198);\n"
"background-color:rgba(238, 238, 238,.4)    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color:rgb(118, 118, 118);\n"
"border: 1px solid rgb(249, 249, 249);\n"
"}")
        self.boton_copia_seguridad.setObjectName("boton_copia_seguridad")
        self.verticalLayout_6.addWidget(self.boton_copia_seguridad)
        self.boton_clonacion = QtWidgets.QPushButton(self.menu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_clonacion.setFont(font)
        self.boton_clonacion.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_clonacion.setStyleSheet("QPushButton {\n"
"border: 0px solid transparent;\n"
"padding:10;\n"
"color: rgb(198, 198, 198);\n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(118, 118, 118);\n"
"border: 1px solid rgb(249, 249, 249);\n"
"}")
        self.boton_clonacion.setObjectName("boton_clonacion")
        self.verticalLayout_6.addWidget(self.boton_clonacion)
        self.boton_herr_testeo = QtWidgets.QPushButton(self.menu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_herr_testeo.setFont(font)
        self.boton_herr_testeo.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_herr_testeo.setStyleSheet("QPushButton {\n"
"border: 0px solid transparent;\n"
"padding:10;\n"
"color: rgb(198, 198, 198);\n"
"background-color:rgba(238, 238, 238,.4)    \n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(118, 118, 118);\n"
"border: 1px solid rgb(249, 249, 249);\n"
"}")
        self.boton_herr_testeo.setObjectName("boton_herr_testeo")
        self.verticalLayout_6.addWidget(self.boton_herr_testeo)
        self.boton_herr_particiones = QtWidgets.QPushButton(self.menu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_herr_particiones.setFont(font)
        self.boton_herr_particiones.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_herr_particiones.setStyleSheet("QPushButton {\n"
"border: 0px solid transparent;\n"
"padding:10;\n"
"color: rgb(198, 198, 198);\n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(118, 118, 118);\n"
"border: 1px solid rgb(249, 249, 249);\n"
"}")
        self.boton_herr_particiones.setObjectName("boton_herr_particiones")
        self.verticalLayout_6.addWidget(self.boton_herr_particiones)
        self.boton_utiles = QtWidgets.QPushButton(self.menu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_utiles.setFont(font)
        self.boton_utiles.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_utiles.setStyleSheet("QPushButton {\n"
"border: 0px solid transparent;\n"
"padding:10;\n"
"color: rgb(198, 198, 198);\n"
"background-color:rgba(238, 238, 238,.4)    \n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(118, 118, 118);\n"
"border: 1px solid rgb(249, 249, 249);\n"
"}")
        self.boton_utiles.setObjectName("boton_utiles")
        self.verticalLayout_6.addWidget(self.boton_utiles)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.menu)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #edf2f6;\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left: 0px solid white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(35, 0, 35, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_categoria_actual = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(19)
        self.label_categoria_actual.setFont(font)
        self.label_categoria_actual.setStyleSheet("color: #020814;\n"
"border: 0px solid #333")
        self.label_categoria_actual.setObjectName("label_categoria_actual")
        self.horizontalLayout.addWidget(self.label_categoria_actual)
        self.verticalLayout_4.addWidget(self.frame)
        self.widget_Login = QtWidgets.QFrame(self.centralwidget)
        self.widget_Login.setEnabled(True)
        self.widget_Login.setStyleSheet("QFrame#frame {\n"
"background-color:#fff\n"
"}")
        self.widget_Login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widget_Login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widget_Login.setObjectName("widget_Login")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_Login)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_Login)
        self.stackedWidget.setStyleSheet("QStackedWidget#stackedWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_inicio = QtWidgets.QWidget()
        self.page_inicio.setStyleSheet("#page_inicio {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.page_inicio.setObjectName("page_inicio")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_inicio)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 179, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.page_inicio)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(94, 104, 116)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 278, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_categorias = QtWidgets.QWidget()
        self.page_categorias.setStyleSheet("")
        self.page_categorias.setObjectName("page_categorias")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_categorias)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.page_categorias)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("#scrollArea {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:0px solid #333;\n"
"\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 794, 540))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet("#scrollAreaWidgetContents {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(28, 28, 28, 28)
        self.gridLayout.setHorizontalSpacing(38)
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_categorias)
        self.page_resultados = QtWidgets.QWidget()
        self.page_resultados.setObjectName("page_resultados")
        self.verticalLayout_result = QtWidgets.QVBoxLayout(self.page_resultados)
        self.verticalLayout_result.setContentsMargins(28, 28, 28, 28)
        self.verticalLayout_result.setObjectName("verticalLayout_result")
        self.stackedWidget.addWidget(self.page_resultados)
        self.page_categoria = QtWidgets.QWidget()
        self.page_categoria.setObjectName("page_categoria")
        self.stackedWidget.addWidget(self.page_categoria)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.widget_Login)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 25)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 26))
        self.menubar.setObjectName("menubar")
        self.boton_menu_cerrar_sesion = QtWidgets.QMenu(self.menubar)
        self.boton_menu_cerrar_sesion.setObjectName("boton_menu_cerrar_sesion")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("background-color: rgb(104, 104, 104);\n"
"color: rgb(222, 222, 222)")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.boton_perfil_menu = QtWidgets.QAction(MainWindow)
        self.boton_perfil_menu.setObjectName("boton_perfil_menu")
        self.boton_cerrar_sesion = QtWidgets.QAction(MainWindow)
        self.boton_cerrar_sesion.setObjectName("boton_cerrar_sesion")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.boton_menu_cerrar_sesion.addAction(self.boton_perfil_menu)
        self.boton_menu_cerrar_sesion.addSeparator()
        self.boton_menu_cerrar_sesion.addAction(self.boton_cerrar_sesion)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.boton_menu_cerrar_sesion.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Hiren\'s Python", None, -1))
        self.label_categorias.setText(QtWidgets.QApplication.translate("MainWindow", "Categorias", None, -1))
        self.input_filter_product.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Busqueda", None, -1))
        self.boton_copia_seguridad.setText(QtWidgets.QApplication.translate("MainWindow", "Copia de Seguridad", None, -1))
        self.boton_clonacion.setText(QtWidgets.QApplication.translate("MainWindow", "Clonación", None, -1))
        self.boton_herr_testeo.setText(QtWidgets.QApplication.translate("MainWindow", "Herramientas de Testeo", None, -1))
        self.boton_herr_particiones.setText(QtWidgets.QApplication.translate("MainWindow", "Herramientas de Particiones", None, -1))
        self.boton_utiles.setText(QtWidgets.QApplication.translate("MainWindow", "Utiles", None, -1))
        self.label_categoria_actual.setText(QtWidgets.QApplication.translate("MainWindow", "Inicio", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Selecione Una Categoria", None, -1))
        self.boton_menu_cerrar_sesion.setTitle(QtWidgets.QApplication.translate("MainWindow", "Ajustes", None, -1))
        self.menuAyuda.setTitle(QtWidgets.QApplication.translate("MainWindow", "Ayuda", None, -1))
        self.boton_perfil_menu.setText(QtWidgets.QApplication.translate("MainWindow", "Cuenta", None, -1))
        self.boton_cerrar_sesion.setText(QtWidgets.QApplication.translate("MainWindow", "Cerrar Sesión", None, -1))
        self.actionAcerca_de.setText(QtWidgets.QApplication.translate("MainWindow", "Acerca de", None, -1))

