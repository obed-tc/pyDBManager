from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class DatabaseConnectionDialog(QtWidgets.QDialog):

    def __init__(self, conexiones):
        super(DatabaseConnectionDialog, self).__init__()
        self.conexiones = conexiones
        self.setWindowTitle("Conectar a la base de datos")
        self.setFixedSize(400, 200)

        
        self.host_label = QtWidgets.QLabel("Host:")
        self.host_edit = QtWidgets.QLineEdit("127.0.0.1")
        self.user_label = QtWidgets.QLabel("Usuario:")
        self.user_edit = QtWidgets.QLineEdit("root")
        self.password_label = QtWidgets.QLabel("Contraseña:")
        self.password_edit = QtWidgets.QLineEdit()
        self.database_label = QtWidgets.QLabel("Base de datos:")
        self.database_edit = QtWidgets.QLineEdit()

        self.connect_button = QtWidgets.QPushButton("Conectar")
        self.connect_button.clicked.connect(self.connect_to_database)
        self.connection_data = {}
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.host_label)
        layout.addWidget(self.host_edit)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.database_label)
        layout.addWidget(self.database_edit)
        layout.addWidget(self.connect_button)
        self.setLayout(layout)

    def connect_to_database(self):
        host = self.host_edit.text()
        user = self.user_edit.text()
        password = self.password_edit.text()
        database = self.database_edit.text()

        try:
            db_connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            db_cursor = db_connection.cursor()
            self.connection_data["host"] = host
            self.connection_data["user"] = user
            self.connection_data["password"] = password
            self.connection_data["database"] = database
            self.conexiones.append(self.connection_data)
            print(self.conexiones)

            QtWidgets.QMessageBox.information(self, "Conexión exitosa", "Conexión a la base de datos exitosa.")
            self.accept()  # Cierra el diálogo después de la conexión exitosa
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error de conexión", f"Error al conectar a la base de datos: {e}")
