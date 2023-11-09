
from PyQt5 import QtCore, QtGui, QtWidgets
from config import DatabaseConnectionDialog
from interface import Ui_Interface
conexiones=[]
class Ui_MainWindow(object):
    def update_connection_buttons(self):
        for i in reversed(range(self.horizontalLayout_3.count())):
                widget = self.horizontalLayout_3.itemAt(i).widget()
                if widget is not None:
                        self.horizontalLayout_3.removeWidget(widget)
                        widget.deleteLater()

        for i, conexion in enumerate(conexiones):
                button = QtWidgets.QPushButton(f"Conexión {i+1}\nHost: {conexion['host']}\nUser: {conexion['user']}\nDatabase: {conexion['database']}")

                button.setMinimumSize(QtCore.QSize(300, 200))
                button.setMaximumSize(QtCore.QSize(300, 200))
                button.setStyleSheet("\n"
                                     "font-size:18px;"
                "width: 300px; /* Ajusta el ancho según tus necesidades */\n"
                "background-color: rgba(255, 255, 255, 0.7); /* Color blanco con opacidad del 70% */\n"
                "border-radius: 10px; /* Borde redondeado */\n"
                "padding: 20px; /* Espaciado interno */\n"
                "box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave */\n"
                "")
                button.setObjectName("pushButton")
                button.clicked.connect(lambda _, c=conexion: self.print_connection(c))
                self.horizontalLayout_3.addWidget(button)


    def print_connection(self, connection):
        self.second_window = QtWidgets.QMainWindow()
        self.ui_segunda_ventana = Ui_Interface()
        self.ui_segunda_ventana.setupUi(self.second_window,connection,self.MainWindow)
        self.second_window.show()
        self.MainWindow.hide()
        
    def open_database_connection_dialog(self):
        dialog = DatabaseConnectionDialog(conexiones)
        dialog.exec_()
        self.update_connection_buttons()
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1198, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"border-image:url(:/img/fondo.png)\n"
"}\n"
"padding: 50%;")
        MainWindow.showMaximized()
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_3.setStyleSheet("QWidget#verticalWidget_3{\n"
"  background-color: rgba(255, 255, 255, 0.7); /* Color blanco con opacidad del 70% */\n"
"  border-radius: 10px; /* Borde redondeado */\n"
"\n"
"  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave */\n"
"}")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.verticalWidget_3)
        self.horizontalWidget_2.setMinimumSize(QtCore.QSize(100, 50))
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(60, 60))
        self.horizontalWidget_2.setStyleSheet("width:100px;\n"
"border-image:url(:/img/logo.png)\n"
"")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5.addWidget(self.horizontalWidget_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalWidget_4 = QtWidgets.QWidget(self.verticalWidget_3)
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget_4)
        self.label_4.setStyleSheet("color:black;\n"
"font: 10pt \"MS Serif\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.verticalLayout_5.addWidget(self.horizontalWidget_4)
        self.horizontalLayout_6.addWidget(self.verticalWidget_3)
        spacerItem1 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalWidget_2)
        self.label.setStyleSheet("color:white;\n"
"font: 87 24pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_2.setStyleSheet("\n"
"color:white;\n"
"font: 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_5.addWidget(self.verticalWidget_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color:white;\n"
"font: 87 12pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("width:100px;\n"
"border-image:url(:/img/button.png)\n"
"")
        self.pushButton_2.clicked.connect(self.open_database_connection_dialog)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalWidget_21 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_21.setMinimumSize(QtCore.QSize(1000, 200))
        self.horizontalWidget_21.setMaximumSize(QtCore.QSize(1000, 200))
        self.horizontalWidget_21.setStyleSheet("")
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        for i, conexion in enumerate(conexiones):
                self.pushButton = QtWidgets.QPushButton(f"Conexión {conexion['host']}\n{conexion['user']}\n{conexion['database']}")

                self.pushButton.setMinimumSize(QtCore.QSize(300, 200))
                self.pushButton.setMaximumSize(QtCore.QSize(300, 200))
                self.pushButton.setStyleSheet("\n"
        "width: 300px; /* Ajusta el ancho según tus necesidades */\n"
        "  background-color: rgba(255, 255, 255, 0.7); /* Color blanco con opacidad del 70% */\n"
        "  border-radius: 10px; /* Borde redondeado */\n"
        "  padding: 20px; /* Espaciado interno */\n"
        "  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave */\n"
        "\n"
        "")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(lambda _, c=conexion: self.print_connection(c))
                self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.horizontalWidget_21)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 579, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 579, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(176, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface"))
        self.label_4.setText(_translate("MainWindow", "Create By Josue"))
        self.label.setText(_translate("MainWindow", "Bienvenido a la interface de base de datos"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/>a</p></body></html>"))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/>Text</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Interface de base de datos\nIntegrantes:\nJosue\nEnrique"))
        self.label_3.setText(_translate("MainWindow", "MYSQL Connections"))
        if (len(conexiones)>0):
             self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>A</p><p>A</p><p>A</p></body></html>"))
import images


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
