from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class DatabaseConnectionDialog(QtWidgets.QDialog):

    def __init__(self, conexiones):
        super(DatabaseConnectionDialog, self).__init__()
        self.conexiones = conexiones
        self.setWindowTitle("Conectar a la base de datos")
        self.setFixedSize(400, 260)

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

        self.test_connection_button = QtWidgets.QPushButton("Test Connection")
        self.test_connection_button.clicked.connect(self.test_connection)
        self.test_connection_button.setStyleSheet("background-color: #4CAF50; color: white;")

        self.create_user_button = QtWidgets.QPushButton("Crear Usuario")
        self.create_user_button.clicked.connect(self.create_user)
        self.create_user_button.setStyleSheet("background-color: #2196F3; color: white;")

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
        layout.addWidget(self.test_connection_button)
        layout.addWidget(self.create_user_button)
        self.setLayout(layout)
    def create_user(self):
        # You can implement the user creation logic here
        # For example, collect user information from QLineEdit fields
        user_name = self.user_edit.text()
        user_password = self.password_edit.text()

        # Perform the database operation to create a new user
        # Example code (replace with your actual logic):
        try:
            db_connection = mysql.connector.connect(
                host=self.host_edit.text(),
                user="root",
                password=self.password_edit.text(),
                database=self.database_edit.text()
            )
            db_cursor = db_connection.cursor()

            # Replace the following SQL statement with your actual query to create a user
            sql_query = f"CREATE USER '{user_name}'@'{self.host_edit.text()}' IDENTIFIED BY '{user_password}'"
            db_cursor.execute(sql_query)

            QtWidgets.QMessageBox.information(self, "Usuario creado", f"Usuario '{user_name}' creado correctamente.")
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error al crear usuario", f"Error al crear usuario: {e}")

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
            self.accept()
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error de conexión", f"Error al conectar a la base de datos: {e}")

    def test_connection(self):
        # Similar code as in connect_to_database, but without modifying self.conexiones or displaying a QMessageBox
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
            QtWidgets.QMessageBox.information(self, "Prueba de conexión exitosa", "Prueba de conexión a la base de datos exitosa.")
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error en la prueba de conexión", f"Error al probar la conexión a la base de datos: {e}")

# Example usage: