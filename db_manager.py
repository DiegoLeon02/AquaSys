import mysql.connector

# Conectar base de datos MySQL
def conectar_db():
    conn = mysql.connector.connect(
        host='localhost',  
        user='root',     
        password='1234', 
        database='napoles'  
    )
    return conn

# Crear las tablas en MySQL si no existen
def crear_tablas():
    conn = conectar_db()
    cursor = conn.cursor()

    # Crear tabla Usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        UsuarioID INT AUTO_INCREMENT PRIMARY KEY,
        Nombre VARCHAR(100) NOT NULL,
        Apellido VARCHAR(100) NOT NULL,
        CorreoElectronico VARCHAR(100) UNIQUE NOT NULL,
        Contrasena VARCHAR(255) NOT NULL,
        RolID INT NOT NULL,
        FechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Activo TINYINT(1) DEFAULT 1
    )''')

    # Crear tabla Roles
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roles (
        RolID INT AUTO_INCREMENT PRIMARY KEY,
        NombreRol VARCHAR(50) NOT NULL UNIQUE,
        Descripcion VARCHAR(255)
    )''')

    # Crear tabla Embarques
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Embarques (
        EmbarqueID INT AUTO_INCREMENT PRIMARY KEY,
        UsuarioID INT NOT NULL,
        FechaEmbarque DATETIME NOT NULL,
        Destino VARCHAR(100) NOT NULL,
        Estado VARCHAR(50) NOT NULL DEFAULT 'Pendiente',
        Contenido VARCHAR(255) NOT NULL,
        FechaEntregaEstimada DATETIME NOT NULL,
        FechaEntrega DATETIME,
        FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
    )''')

    # Crear tabla Eventos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Eventos (
        EventoID INT AUTO_INCREMENT PRIMARY KEY,
        NombreEvento VARCHAR(100) NOT NULL,
        FechaEvento DATETIME NOT NULL,
        Lugar VARCHAR(255) NOT NULL,
        Descripcion VARCHAR(255),
        Estado VARCHAR(50) NOT NULL DEFAULT 'Programado'
    )''')

    # Crear tabla Notificaciones
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Notificaciones (
        NotificacionID INT AUTO_INCREMENT PRIMARY KEY,
        UsuarioID INT NOT NULL,
        EventoID INT,
        EmbarqueID INT,
        FechaEnvio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Mensaje VARCHAR(255) NOT NULL,
        FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID),
        FOREIGN KEY (EventoID) REFERENCES Eventos(EventoID),
        FOREIGN KEY (EmbarqueID) REFERENCES Embarques(EmbarqueID)
    )''')

    # Crear tabla NotasEmbarque
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS NotasEmbarque (
        NotaID INT AUTO_INCREMENT PRIMARY KEY,
        EmbarqueID INT NOT NULL,
        UsuarioID INT NOT NULL,
        FechaNota TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        DetalleNota VARCHAR(255) NOT NULL,
        FOREIGN KEY (EmbarqueID) REFERENCES Embarques(EmbarqueID),
        FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
    )''')

    # Crear tabla Transportistas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transportistas (
        TransportistaID INT AUTO_INCREMENT PRIMARY KEY,
        NombreTransportista VARCHAR(100) NOT NULL,
        Contacto VARCHAR(100)
    )''')

    # Crear tabla EmbarquesTransportistas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EmbarquesTransportistas (
        EmbarqueID INT NOT NULL,
        TransportistaID INT NOT NULL,
        AsignadoEn TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (EmbarqueID, TransportistaID),
        FOREIGN KEY (EmbarqueID) REFERENCES Embarques(EmbarqueID),
        FOREIGN KEY (TransportistaID) REFERENCES Transportistas(TransportistaID)
    )''')

    conn.commit()
    conn.close()

# Funciones para interactuar con la base de datos
def registrar_usuario(nombre, apellido, correo, contraseña, rol_id):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Usuarios (Nombre, Apellido, CorreoElectronico, Contrasena, RolID) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellido, correo, contraseña, rol_id))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        conn.close()

def validar_usuario(correo, contraseña):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE CorreoElectronico=%s AND Contrasena=%s", (correo, contraseña))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def crear_evento(nombre_evento, fecha_evento, lugar, descripcion):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Eventos (NombreEvento, FechaEvento, Lugar, Descripcion) VALUES (%s, %s, %s, %s)",
                   (nombre_evento, fecha_evento, lugar, descripcion))
    conn.commit()
    conn.close()

def crear_embarque(usuario_id, fecha_embarque, destino, estado, contenido, fecha_entrega_estimada):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Embarques (UsuarioID, FechaEmbarque, Destino, Estado, Contenido, FechaEntregaEstimada) VALUES (%s, %s, %s, %s, %s, %s)",
                   (usuario_id, fecha_embarque, destino, estado, contenido, fecha_entrega_estimada))
    conn.commit()
    conn.close()
