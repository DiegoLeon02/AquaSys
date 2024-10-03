import mysql.connector

class DatabaseManager:
    def __init__(self):
        # Datos para la conexión MySQL
        self.connection = mysql.connector.connect(
            host="localhost",  # Cambia por la IP de tu servidor si no es local
            user="root",  # Cambia al usuario de tu base de datos
            password="tu_contraseña",  # Cambia por tu contraseña
            database="AQUASYS"  # Nombre de tu base de datos
        )
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Creación de tablas para usuarios, cursos y eventos
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS administradores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                correo VARCHAR(100) UNIQUE,
                contraseña VARCHAR(100)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(255),
                descripcion TEXT,
                pdf_url VARCHAR(255)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS eventos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255),
                ubicacion VARCHAR(255),
                fecha DATE
            )
        """)
        self.connection.commit()

    def insertar_administrador(self, nombre, correo, contraseña):
        sql = "INSERT INTO administradores (nombre, correo, contraseña) VALUES (%s, %s, %s)"
        valores = (nombre, correo, contraseña)
        self.cursor.execute(sql, valores)
        self.connection.commit()

    def verificar_administrador(self, correo, contraseña):
        sql = "SELECT * FROM administradores WHERE correo = %s AND contraseña = %s"
        self.cursor.execute(sql, (correo, contraseña))
        return self.cursor.fetchone()

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
