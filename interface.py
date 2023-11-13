from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableView
import re
import ast
data_array = [
    {"ID": 1, "Nombre": "Juan", "Edad": 25},
    {"ID": 2, "Nombre": "Daniel", "Edad": 23}
]
class Ui_Interface(object):
    
    def __init__(self):
        self.selected_checkbox = None
        self.db_cursor = None 
        self.datos=None
    def execute_selected_query(self, query):
        if self.selected_checkbox == self.radioButton_DDL:
            return self.execute_ddl_query(query)
        elif self.selected_checkbox == self.radioButton_DML:
            return self.execute_dml_query(query)
        elif self.selected_checkbox == self.radioButton_DCL:
            return self.execute_dcl_query(query)
    def checkbox_selected(self, checkbox):
        self.selected_checkbox = checkbox

    def execute_ddl_query(self, query):
        try:
                if self.db_connection is not None and self.db_connection.is_connected():
                        self.db_cursor = self.db_connection.cursor()

                        if query.strip().upper().startswith(("CREATE", "ALTER","DROP","SHOW")):
                                self.db_cursor.execute(query)
                                resultados = self.db_cursor.fetchall()
                                return f"{query}\nConsulta DDL ejecutada con éxito:\n{str(resultados)}"
                        else:
                                return "Error: Consulta DDL debe comenzar con 'CREATE' o 'ALTER' o 'DROP'."
                else:
                        self.conectar_mysql(self.data)
                        return "Reconexión exitosa. Vuelve a intentar la consulta."

        except mysql.connector.Error as mysql_error:
                return f"Error al ejecutar la consulta DDL: {str(mysql_error)}"
        except Exception as e:
                return f"Error al ejecutar la consulta DDL: {str(e)}"


    def execute_dml_query(self, query):
        try:
                if self.db_connection is not None and self.db_connection.is_connected():
                        self.db_cursor = self.db_connection.cursor()
                        if query.strip().upper().startswith(("SELECT","INSERT", "UPDATE", "DELETE","SHOW","FLUSH")):
                                self.db_cursor.execute(query)
                                resultados = self.db_cursor.fetchall()
                                print("Resultados:",resultados)
                                return f"{query}\nConsulta DML ejecutada con éxito:\n{str(resultados)}"
                        else:
                                return "Error: Consulta DML debe comenzar con 'SELECT','INSERT', 'UPDATE' o 'DELETE'."
                else:
                        self.conectar_mysql(self.data)
                        return "Reconexión exitosa. Vuelve a intentar la consulta."

        except mysql.connector.Error as mysql_error:
                return f"Error al ejecutar la consulta DML: {str(mysql_error)}"
        except Exception as e:
                return f"Error al ejecutar la consulta DML: {str(e)}"

    def execute_dcl_query(self, query):
        try:
                if self.db_connection is not None and self.db_connection.is_connected():
                        self.db_cursor = self.db_connection.cursor()
                        if query.strip().upper().startswith(("GRANT", "REVOKE","SHOW")):
                                self.db_cursor.execute(query)
                                resultados = self.db_cursor.fetchall()
                                return f"{query}\nConsulta DCL ejecutada con éxito:\n{str(resultados)}"
                        else:
                                return "Error: Consulta DCL debe comenzar con 'GRANT' o 'REVOKE'."
                else:
                        self.conectar_mysql(self.data)
                        return "Reconexión exitosa. Vuelve a intentar la consulta DCL."

        except mysql.connector.Error as mysql_error:
                return f"Error al ejecutar la consulta DCL: {str(mysql_error)}"
        except Exception as e:
                return f"Error al ejecutar la consulta DCL: {str(e)}"

    def execute_query(self):
        query = self.textEdit_input.toPlainText()
        if not query.strip():
            self.textEdit_output.setPlainText("Error: La consulta está vacía.")
            return
        if self.selected_checkbox is not None:
            result = self.execute_selected_query(query)
            matches = re.search(r'\[([^]]+)\]', result)
            if matches:
                self.textEdit_output.hide()

                contenido_corchetes = matches.group(0)
                try:
                        array_resultado = ast.literal_eval(contenido_corchetes)
                        self.datos=array_resultado
                        print("Data:",self.datos)

                        self.setup_table_view(self.verticalWidget, self.datos)

                except (SyntaxError, ValueError) as e:
                        print("Error al convertir:", e)
                        self.textEdit_output.show()
                        self.textEdit_output.setPlainText(result)


            else:
                self.textEdit_output.show()
                self.clear_table_view()
                self.textEdit_output.setPlainText(result)
        else:
            self.textEdit_output.setPlainText("Error: selecciona una opcion")
            return
    def conectar_mysql(self, datos):
        try:
                self.db_connection = mysql.connector.connect(
                host=datos['host'],
                user=datos['user'],
                password=datos['password'],
                database=datos['database']
                )
                self.db_cursor = self.db_connection.cursor()

                if self.db_connection.is_connected():
                        return True
                else:
                        return False
        except mysql.connector.Error as error:
                return False
    def clear_table_view(self):
        if hasattr(self, 'table_view') and self.table_view is not None:
                parent_layout = self.verticalLayout_2
                parent_layout.removeWidget(self.table_view)

                self.table_view.deleteLater()
                self.table_view = None


    def setup_table_view(self, parent_widget, data_array):
        self.clear_table_view()
        self.table_view = QTableView(parent_widget)
        self.table_view.setObjectName("tableView")

        # Configurar un modelo de datos para la tabla
        self.table_model = QStandardItemModel(self.table_view)

        # Obtener encabezados de columnas basados en los índices de la primera fila en el array
        if data_array:
                column_headers = [f"Columna {i}" for i in range(len(data_array[0]))]
                self.table_model.setHorizontalHeaderLabels(column_headers)

        # Poblar el modelo con datos del array de arrays
        for row_data in data_array:
                items = [QStandardItem(str(value)) for value in row_data]
                self.table_model.appendRow(items)

        # Establecer el modelo para la vista de la tabla
        self.table_view.setModel(self.table_model)

        # Agregar la vista de la tabla al diseño vertical
        parent_layout = parent_widget.layout()
        parent_layout.addWidget(self.table_view)


    def clear_fields(self):
        self.clear_table_view()
        self.textEdit_output.show()

        self.textEdit_input.clear()
        self.textEdit_output.clear()
        self.radioButton_DDL.setChecked(False)
        self.radioButton_DML.setChecked(False)
        self.radioButton_DCL.setChecked(False)
        self.selected_checkbox = None
    def setupUi(self, MainWindow,data,firstWindow):
        self.MainWindow = MainWindow
        self.firstWindow=firstWindow
        self.data=data
        self.conexion_mysql = self.conectar_mysql(data)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 600)
        MainWindow.showMaximized()
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
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
        self.pushButton_3.clicked.connect(self.close_window)

        self.verticalLayout_4.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 10pt \"Arial\";\n"
"color:white")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 10pt \"Arial\";\n"
"color:white")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 10pt \"Arial\";\n"
"color:white")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.check = QtWidgets.QWidget(self.centralwidget)

        if (self.conexion_mysql):
             self.check.setMinimumSize(QtCore.QSize(50, 50))
             self.check.setMaximumSize(QtCore.QSize(50, 50))
             self.check.setStyleSheet("width:100px;\n"
        "border-image:url(:/img/check.png)\n"
        "")
        self.check.setObjectName("check")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.check)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4.addWidget(self.check)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color:green")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        
        
        self.horizontalWidget_21 = QtWidgets.QWidget(self.centralwidget)

        if (self.conexion_mysql==False):
                self.horizontalWidget_21.setMinimumSize(QtCore.QSize(50, 50))
                self.horizontalWidget_21.setMaximumSize(QtCore.QSize(50, 50))
                self.horizontalWidget_21.setSizeIncrement(QtCore.QSize(0, 0))
                self.horizontalWidget_21.setStyleSheet("width:100px;\n"
"border-image:url(:/img/error.png)\n"
"")
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.error = QtWidgets.QHBoxLayout(self.horizontalWidget_21)
        self.error.setObjectName("error")
        self.verticalLayout_4.addWidget(self.horizontalWidget_21)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color:red")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
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
        self.buttonPlay.clicked.connect(self.execute_query)

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
        self.buttonReset.clicked.connect(self.clear_fields)
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
        if (self.datos!=None):
              self.setup_table_view(self.verticalWidget, self.datos)


        self.horizontalLayout_4.addWidget(self.verticalWidget)
        spacerItem2 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def close_window(self):
        # Cierra la ventana principal
        self.MainWindow.close()
        self.firstWindow.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Volver"))
        self.label.setText(_translate("MainWindow", "Host: "+self.data["host"]))
        self.label_4.setText(_translate("MainWindow", "User:"+self.data["user"]))
        self.label_5.setText(_translate("MainWindow", "Conexion:"))
        if (self.conexion_mysql):
            self.label_6.setText(_translate("MainWindow", "Exitosa"))
        else:
            self.label_7.setText(_translate("MainWindow", "Algo salio mal"))
        self.label_title.setText(_translate("MainWindow", "INTERFAZ DE BASE DE DATOS"))
        self.radioButton_DDL.setText(_translate("MainWindow", "DDL"))
        self.radioButton_DML.setText(_translate("MainWindow", "DML"))
        self.radioButton_DCL.setText(_translate("MainWindow", "DCL"))
        self.radioButton_DDL.clicked.connect(lambda: self.checkbox_selected(self.radioButton_DDL))
        self.radioButton_DML.clicked.connect(lambda: self.checkbox_selected(self.radioButton_DML))
        self.radioButton_DCL.clicked.connect(lambda: self.checkbox_selected(self.radioButton_DCL))

        self.label_3.setText(_translate("MainWindow", "Ingresa tu consulta MySql:"))
        self.label_2.setText(_translate("MainWindow", "Salida:"))
        self.textEdit_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">RESULTADO</span></p></body></html>"))

import images


