

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"border-image:url(:/img/fondo.png)\n"
"}\n"
"padding: 50%;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_2.setMinimumSize(QtCore.QSize(100, 50))
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(60, 60))
        self.horizontalWidget_2.setStyleSheet("width:100px;\n"
"border-image:url(:/img/logo.png)\n"
"")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4.addWidget(self.horizontalWidget_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("  width: 50px; /* Diámetro del botón */\n"
"  height: 50px; /* Diámetro del botón (mismo valor que el ancho) */\n"
"  background-color: rgba(255, 255, 255, 0.7); /* Color blanco con opacidad del 70% */\n"
"  border: 2px solid #000; /* Borde de 2px sólido */\n"
"  border-radius: 50%; /* Hace que el botón sea circular */\n"
"  display: flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  cursor: pointer;\n"
"  font-weight: bold;\n"
"  text-decoration: none;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.verticalWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.verticalWidget)
        self.label_title.setStyleSheet("color:white;\n"
"font: 20pt \"Arial\";")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_DDL = QtWidgets.QRadioButton(self.verticalWidget)
        self.radioButton_DDL.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";")
        self.radioButton_DDL.setObjectName("radioButton_DDL")
        self.horizontalLayout_3.addWidget(self.radioButton_DDL)
        self.radioButton_DML = QtWidgets.QRadioButton(self.verticalWidget)
        self.radioButton_DML.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";")
        self.radioButton_DML.setObjectName("radioButton_DML")
        self.horizontalLayout_3.addWidget(self.radioButton_DML)
        self.radioButton_DCL = QtWidgets.QRadioButton(self.verticalWidget)
        self.radioButton_DCL.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";")
        self.radioButton_DCL.setObjectName("radioButton_DCL")
        self.horizontalLayout_3.addWidget(self.radioButton_DCL)
        self.buttonPlay = QtWidgets.QPushButton(self.verticalWidget)
        self.buttonPlay.setMinimumSize(QtCore.QSize(50, 50))
        self.buttonPlay.setMaximumSize(QtCore.QSize(50, 50))
        self.buttonPlay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonPlay.setStyleSheet("\n"
"border-image:url(:/img/play.png)\n"
"")
        self.buttonPlay.setText("")
        self.buttonPlay.setObjectName("buttonPlay")
        self.horizontalLayout_3.addWidget(self.buttonPlay)
        self.buttonReset = QtWidgets.QPushButton(self.verticalWidget)
        self.buttonReset.setMinimumSize(QtCore.QSize(50, 45))
        self.buttonReset.setMaximumSize(QtCore.QSize(50, 40))
        self.buttonReset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonReset.setStyleSheet("\n"
"border-image:url(:/img/reset.png)\n"
"")
        self.buttonReset.setText("")
        self.buttonReset.setObjectName("buttonReset")
        self.horizontalLayout_3.addWidget(self.buttonReset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.verticalWidget)
        self.label_3.setStyleSheet("font: 10pt \"Arial\";\n"
"color:white")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.textEdit_input = QtWidgets.QTextEdit(self.verticalWidget)
        self.textEdit_input.setStyleSheet("font: 12pt \"Arial\";")
        self.textEdit_input.setObjectName("textEdit_input")
        self.verticalLayout_2.addWidget(self.textEdit_input)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.label_2.setStyleSheet("font: 13pt \"Arial\";\n"
"color:white")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit_output = QtWidgets.QTextEdit(self.verticalWidget)
        self.textEdit_output.setStyleSheet("font: 12pt \"Arial\";")
        self.textEdit_output.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textEdit_output.setUndoRedoEnabled(False)
        self.textEdit_output.setObjectName("textEdit_output")
        self.verticalLayout_2.addWidget(self.textEdit_output)
        self.horizontalLayout_4.addWidget(self.verticalWidget)
        spacerItem2 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Volver"))
        self.label_title.setText(_translate("MainWindow", "TITULO"))
        self.radioButton_DDL.setText(_translate("MainWindow", "DML"))
        self.radioButton_DML.setText(_translate("MainWindow", "DML"))
        self.radioButton_DCL.setText(_translate("MainWindow", "DML"))
        self.label_3.setText(_translate("MainWindow", "Ingresa tu consulta MySql:"))
        self.label_2.setText(_translate("MainWindow", "Salida:"))
        self.textEdit_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">RESULTADO</span></p></body></html>"))
import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
