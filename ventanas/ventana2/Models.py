from typing import List, Dict, Any, Tuple

from PySide2.QtCore import Qt
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtWidgets import QCompleter


class Categories(QCompleter):

    items: List[Tuple[List[Dict[str, Any]]]] = [
        ('copia de seguridad', [
            {
                'id': 0,
                'name': "clonezilla",
                'logo': 'ventanas/asserts/logos/clonezilla.png',
                'description': 
                    "Es un software libre de recuperación ante desastres, sirve para la clonación de discos y particiones.",
                'download': 'https://clonezilla.org/downloads.php',
                'imagenes': [
                    "ventanas/asserts/img/clonezilla1.png",
                    "ventanas/asserts/img/clonezilla2",
                    "ventanas/asserts/img/clonezilla3",
                    "ventanas/asserts/img/clonezilla4"
                ]
            },
            {
                'id': 1,
                'name': "backupper",
                'logo': 'ventanas/asserts/logos/backupper.jpg',
                'description': 
                    "Es un software gratuito diseñado para crear y gestionar copias de seguridad de nuestras carpetas y de nuestros discos completos para poder recuperar los archivos en caso de pérdida o fallo del sistema.",
                'download': 'https://www.backup-utility.com/download.html',
                'imagenes': [
                    "ventanas/asserts/img/backup1.png",
                    "ventanas/asserts/img/backup2",
                    "ventanas/asserts/img/backup3",
                    "ventanas/asserts/img/backup4"
                ]
            },
            {
                'id': 2,
                'name': "fbackup",
                'logo': 'ventanas/asserts/logos/fbackup.png',
                'description': 
                    "Es una aplicación totalmente gratuita diseñada para realizar sencillas copias de seguridad de nuestros archivos en pocos segundos.",
                'download': 'http://www.fbackup.com/es/free-download.php',
                'imagenes': [
                    "ventanas/asserts/img/fbackup1.png",
                    "ventanas/asserts/img/fbackup2",
                    "ventanas/asserts/img/fbackup3",
                    "ventanas/asserts/img/fbackup4"
                ]
            },
            {
                'id': 3,
                'name': "macrium reflect",
                'logo': 'ventanas/asserts/logos/macriumreflect.png',
                'description': 
                    "Es un programa que se centra que ofrecer nos funciones centradas en las copias de seguridad de nuestros datos personales.",
                'download': 'https://www.macrium.com/reflectfree',
                'imagenes': [
                    "ventanas/asserts/img/macriumreflect1.png",
                    "ventanas/asserts/img/macriumreflect2",
                    "ventanas/asserts/img/macriumreflect3",
                    "ventanas/asserts/img/macriumreflect4"
                ]
            },
            {
                'id': 4,
                'name': "paragon drive copy professional",
                'logo': 'ventanas/asserts/logos/paragondrivecopyprofessional.jpg',
                'description': 
                    "Es una herramienta de copia de seguridad y migración de datos repleta de funciones para usuarios domésticos avanzados.",
                'download': 'https://www.paragon-software.com/home/drive-copy/', 
                'imagenes': [
                    "ventanas/asserts/img/paragondrivecopyprofessional1.png",
                    "ventanas/asserts/img/paragondrivecopyprofessional2",
                    "ventanas/asserts/img/paragondrivecopyprofessional3",
                    "ventanas/asserts/img/paragondrivecopyprofessional4"
                ]
            },

        ]),
        ('clonación', [
            {
                'id': 0,
                'name': "Cobian Backup",
                'logo': 'ventanas/asserts/logos/cobian.jpg',
                'description':
                    "Es un programa multitarea capaz de crear copias de seguridad en un equipo, en una red local o incluso en/desde un servidor FTP.",
                'download': 'https://www.cobiansoft.com/cobianbackup.html',
                'imagenes': [
                    "ventanas/asserts/img/cobian1.png",
                    "ventanas/asserts/img/cobian2",
                    "ventanas/asserts/img/cobian3",
                    "ventanas/asserts/img/cobian4"
                ]
            },
            {
                'id': 1,
                'name': "acronis true image",
                'logo': 'ventanas/asserts/logos/acronistrueimage.jpg',
                'description': 
                    "Es un programa de creación de imágenes de disco, puede crear una imagen de disco mientras se está ejecutando Microsoft Windows o Linux, o fuera de línea por arranque de CD / DVD, unidades Flash USB, PXE, u otros medios de inicio.",
                'download': '',
                'imagenes': [
                    "ventanas/asserts/img/acronistrueimage1.png",
                    "ventanas/asserts/img/acronistrueimage2",
                    "ventanas/asserts/img/acronistrueimage3",
                    "ventanas/asserts/img/acronistrueimage4"
                ]
            },
            {
                'id': 2,
                'name': "easeus todo backup",
                'logo': 'ventanas/asserts/logos/easeustodobackup.png',
                'description': 
                    "Es una herramienta de copia de seguridad confiable y profesional que ayuda a los usuarios personales proteger archivos, particiones, discos y todo el sistema de una manera fácil.",
                'download': 'https://www.acronis.com/en-us/homecomputing/thanks/acronis-true-image-2019/',
                'imagenes': [
                    "ventanas/asserts/img/easeustodobackup1.png",
                    "ventanas/asserts/img/easeustodobackup2",
                    "ventanas/asserts/img/easeustodobackup3",
                    "ventanas/asserts/img/easeustodobackup4"
                ]
            },
            {
                'id': 3,
                'name': "iperius backup",
                'logo': 'ventanas/asserts/logos/iperiusbackup.png',
                'description': 
                    "Es un programa de copia de seguridad para sistemas Windows.",
                'download': 'https://www.iperiusbackup.com/download-software-backup.aspx',
                'imagenes': [
                    "ventanas/asserts/img/iperiusbackup1.png",
                    "ventanas/asserts/img/iperiusbackup2",
                    "ventanas/asserts/img/iperiusbackup3",
                    "ventanas/asserts/img/iperiusbackup4"
                ]
            },
            {
                'id': 4,
                'name': "comodo",
                'logo': 'ventanas/asserts/logos/comodo.jpg',
                'description':
                    "Es una aplicación que nos permitirá, de forma cómoda, realizar backups, ya sean en un espacio de nuestro ordenador, mediante redes, mediante cd´s o a través de un servidor ftp.",
                'download': 'https://www.comodo.com/home/backup-online-storage/backup-first-time-setup.php',
                'imagenes': [
                    "ventanas/asserts/img/comodo1.png",
                    "ventanas/asserts/img/comodo2",
                    "ventanas/asserts/img/comodo3",
                    "ventanas/asserts/img/comodo4"
                ]
            },
        ]),
        ('testeo', [
            {
                'id': 0,
                'name': "crystal disk info",
                'logo': 'ventanas/asserts/logos/crystaldiskinfo.jpg',
                'description': 
                    "Es una aplicación diseñada para ayudarte a mantener con buena salud el disco duro de tu PC, ademas te muestra en su interfaz todo tipo de información detallada acerca del disco duro, desde la marca y el modelo al tamaño de buffer y caché, el número de serie, o incluso el firmware que utiliza.",
                'download': 'https://crystalmark.info/en/software/crystaldiskinfo/',
                'imagenes': [
                    "ventanas/asserts/img/crystaldiskinfo1.png",
                    "ventanas/asserts/img/crystaldiskinfo2",
                    "ventanas/asserts/img/crystaldiskinfo3",
                    "ventanas/asserts/img/crystaldiskinfo4"
                ]
            },
            {
                'id': 1,
                'name': "acronis drive monitor",
                'logo': 'ventanas/asserts/logos/acronisdrivemonitor.jpg',
                'description': 
                    "Es una aplicación gratuita de software que monitoriza el estado del disco duro de servidores, PC´s y portátiles.",
                'download': 'https://www.acronis.com/es-es/homecomputing/products/drive-monitor/support.html',
                'imagenes': [
                    "ventanas/asserts/img/acronisdrivemonitor1.png",
                    "ventanas/asserts/img/acronisdrivemonitor2",
                    "ventanas/asserts/img/acronisdrivemonitor3",
                    "ventanas/asserts/img/acronisdrivemonitor4"
                ]
            },
            {
                'id': 2,
                'name': "aida",
                'logo': 'ventanas/asserts/logos/aida.jpg',
                'description': 
                    "Es un programa informático de análisis, auditoría e información del sistema, ademas muestra información detallada sobre los componentes de un ordenador.",
                'download': 'https://www.aida64.com/downloads',
                'imagenes': [
                    "ventanas/asserts/img/aida1.png",
                    "ventanas/asserts/img/aida2",
                    "ventanas/asserts/img/aida3",
                    "ventanas/asserts/img/aida4"
                ]
            },
            {
                'id': 3,
                'name': "cpuz",
                'logo': 'ventanas/asserts/logos/cpuz.jpg',
                'description': 
                    "Es un software freeware, que nos brinda información detallada del procesador, chipset de sistema y el chipset de video entre otros que está instalado en la Computadora Personal.",
                'download': 'https://www.cpuid.com/softwares/cpu-z.html',
                'imagenes': [
                    "ventanas/asserts/img/cpuz1.png",
                    "ventanas/asserts/img/cpuz2",
                    "ventanas/asserts/img/cpuz3",
                    "ventanas/asserts/img/cpuz4"
                ]
            },
            {
                'id': 4,
                'name': "cpuid hwmonitor",
                'logo': 'ventanas/asserts/logos/cpuidhwmonitor.jpg',
                'description': 
                    "Es un programa de monitoreo de hardware que lee los sistemas de PC principales sensores de salud: voltajes, temperaturas, ventiladores de velocidad.",
                'download': 'https://www.cpuid.com/softwares/hwmonitor.html',
                'imagenes': [
                    "ventanas/asserts/img/cpuidhwmonitor1.png",
                    "ventanas/asserts/img/cpuidhwmonitor2",
                    "ventanas/asserts/img/cpuidhwmonitor3",
                    "ventanas/asserts/img/cpuidhwmonitor4"
                ]
            },
        ]),
        ('particiones', [
            {
                'id': 0,
                'name': "easeus partition master free",
                'logo': 'ventanas/asserts/logos/easeuspartitionmasterfree.jpg',
                'description': 
                    "Es un software de particiones gratuito que puede redimensionar, mover, fusionar, copiar y unir particiones en Windows.",
                'download': 'https://www.easeus.com/download/epmf-download.html',
                'imagenes': [
                    "ventanas/asserts/img/easeuspartitionmasterfree1.png",
                    "ventanas/asserts/img/easeuspartitionmasterfree2",
                    "ventanas/asserts/img/easeuspartitionmasterfree3",
                    "ventanas/asserts/img/easeuspartitionmasterfree4"
                ]
            },
            {
                'id': 1,
                'name': "minitool partition wizard free",
                'logo': 'ventanas/asserts/logos/minitoolpartitionwizardfree.png',
                'description':
                    "Es una herramienta sencilla y fácil de utilizar para gestionar y administrar particiones y discos desde sistemas operativos.",
                'download': 'https://www.partitionwizard.com/download.html',
                'imagenes': [
                    "ventanas/asserts/img/minitoolpartitionwizardfree1.png",
                    "ventanas/asserts/img/minitoolpartitionwizardfree2",
                    "ventanas/asserts/img/minitoolpartitionwizardfree3",
                    "ventanas/asserts/img/minitoolpartitionwizardfree4"
                ]
            },
            {
                'id': 2,
                'name': "aomei partition assistant",
                'logo': 'ventanas/asserts/logos/aomeipartitionassistant.jpg',
                'description': 
                    "Es un software que administra sus discos duros y particiones en el estado más razonable. Además, le permite migrar el SO al SSD, copiar el disco duro a otro HDD / SSD, convertir el disco entre MBR y GPT.",
                'download': 'https://www.disk-partition.com/download-home.html',
                'imagenes': [
                    "ventanas/asserts/img/aomeipartitionassistant1",
                    "ventanas/asserts/img/aomeipartitionassistant2",
                    "ventanas/asserts/img/aomeipartitionassistant3",
                    "ventanas/asserts/img/aomeipartitionassistant4"
                ]
            },
            {
                'id': 3,
                'name': "gparted",
                'logo': 'ventanas/asserts/logos/gparted.png',
                'description': 
                    "Es el editor de particiones compatible con Linux, para crear, reorganizar y eliminar particiones de disco.",
                'download': 'https://gparted.org/download.php',
                'imagenes': [
                    "ventanas/asserts/img/gparted1.png",
                    "ventanas/asserts/img/gparted2",
                    "ventanas/asserts/img/gparted3",
                    "ventanas/asserts/img/gparted4"
                ]
            },
            {
                'id': 4,
                'name': "active@ partition manager",
                'logo': 'ventanas/asserts/logos/active@partitionmanager.jpg',
                'description': 
                    "Es una aplicación gratuita que te ayuda a gestionar los dispositivos de almacenamiento y las unidades lógicas o particiones.",
                'download': 'http://www.pcdisk.com/download.html',
                'imagenes': [
                    "ventanas/asserts/img/active@partitionmanager1",
                    "ventanas/asserts/img/active@partitionmanager2",
                    "ventanas/asserts/img/active@partitionmanager3",
                    "ventanas/asserts/img/active@partitionmanager4"
                ]
            },
        ]),
        ('utiles', [
            {
                'id': 0,
                'name': "winrar",
                'logo': 'ventanas/asserts/logos/winrar.jpg',
                'description':
                    "Es un potente programa compresor y descompresor de datos.",
                'download': 'https://www.winrar.es/descargas',
                'imagenes': [
                    "ventanas/asserts/img/winrar1.png",
                    "ventanas/asserts/img/winrar2",
                    "ventanas/asserts/img/winrar3",
                    "ventanas/asserts/img/winrar4"
                ]
            },
            {
                'id': 1,
                'name': "vlc media player",
                'logo': 'ventanas/asserts/logos/vlcmediaplayer.png',
                'description': 
                    "Es un reproductor y framework multimedia, libre y de código abierto desarrollado por el proyecto VideoLAN.",
                'download': 'https://www.videolan.org/vlc/index.es.html',
                'imagenes': [
                    "ventanas/asserts/img/vlcmediaplayer1",
                    "ventanas/asserts/img/vlcmediaplayer2",
                    "ventanas/asserts/img/vlcmediaplayer3",
                    "ventanas/asserts/img/vlcmediaplayer4"
                ]
            },
            {
                'id': 2,
                'name': "7zip",
                'logo': 'ventanas/asserts/logos/7zip.png',
                'description':
                    "Es un potente compresor y descompresor de archivos que soporta un gran número de formatos, representando una excepcional alternativa gratuita.",
                'download': 'https://www.7-zip.org/download.html',
                'imagenes': [
                    "ventanas/asserts/img/7zip1",
                    "ventanas/asserts/img/7zip2",
                    "ventanas/asserts/img/7zip3",
                    "ventanas/asserts/img/7zip4"
                ]
            },
            {
                'id': 3,
                'name': "kaspersky",
                'logo': 'ventanas/asserts/logos/kaspersky.jpg',
                'description': 
                    "Es un antivirus que realiza una excelente combinación de protección reactiva y preventiva, protegiéndote eficazmente de virus, troyanos y todo tipo de programas malignos.",
                'download': 'https://www.kaspersky.es/downloads',
                'imagenes': [
                    "ventanas/asserts/img/kaspersky1.png",
                    "ventanas/asserts/img/kaspersky2",
                    "ventanas/asserts/img/kaspersky3",
                    "ventanas/asserts/img/kaspersky4"
                ]
            },
            {
                'id': 4,
                'name': "virtualbox",
                'logo': 'ventanas/asserts/logos/virtualbox.jpg',
                'description': 
                    "Es un programa de gran utilidad para todos aquellos que necesiten utilizar un sistema operativo puntualmente pero no quieran crear una partición en su equipo y por consiguiente tener que instalar dos sistemas operativos en el mismo ordenador.",
                'download': 'https://www.virtualbox.org/wiki/Downloads',
                'imagenes': [
                    "ventanas/asserts/img/virtualbox1",
                    "ventanas/asserts/img/virtualbox2",
                    "ventanas/asserts/img/virtualbox3",
                    "ventanas/asserts/img/virtualbox4"
                ]
            },
        ])
    ]

    ConcatenationRole = Qt.UserRole + 1

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.comprobar = tuple()
        self.create_model(data=self.items)

    def create_model(self, data: list) -> None:
        def addItems(parent, elements):
            for text, children in elements:
                for ad in children:
                    item = QStandardItem(ad.get('name').lower())
                    item.setData(data, Categories.ConcatenationRole)
                    parent.appendRow(item)

        model = QStandardItemModel(self)
        addItems(model, data)
        self.setModel(model)
