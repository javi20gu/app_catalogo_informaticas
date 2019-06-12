from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTranslator, QLocale, QLibraryInfo
from sys import argv, exit
from ventanas.ventana1.Model import Login
from ventanas.ventana1.Ui import Ventana1


if __name__ == '__main__':
    app: QApplication = QApplication(argv)
    translator: QTranslator = QTranslator(app)
    locale: QLocale = QLocale.system().name()
    path: QLibraryInfo = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load('qt_{}'.format(locale), path)
    app.installTranslator(translator)
    login: Login = Login()
    widget: Ventana1 = Ventana1(login)
    widget.stackedWidget.setCurrentIndex(0)
    widget.show()
    exit(app.exec_())
