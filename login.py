import json
import mysql.connector
from mysql.connector import Error
from http.server import BaseHTTPRequestHandler, HTTPServer

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='aquasys'
        )
        return conexion if conexion.is_connected() else None
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def ejecutar_consulta(consulta, parametros=None, fetchone=False):
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute(consulta, parametros or ())
        resultado = cursor.fetchone() if fetchone else cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado
    return None

def validar_usuario(correo_electronico, contrasena=None):
    consulta = "SELECT * FROM Usuarios WHERE CorreoElectronico = %s" + ("" if contrasena is None else " AND Contrasena = %s")
    return ejecutar_consulta(consulta, (correo_electronico, contrasena) if contrasena else (correo_electronico), fetchone=(contrasena is not None)) is not None

def gestionar_entidad(entidad, accion, id_entidad=None, datos=None):
    acciones = {
        'cursos': "INSERT INTO Cursos (Nombre, Detalles) VALUES (%s, %s)",
        'empleados': "INSERT INTO Empleados (Nombre, Cargo) VALUES (%s, %s)",
        'roles': "INSERT INTO Roles (Nombre, Permisos) VALUES (%s, %s)",
        'embarques': "INSERT INTO Embarques (Destino, FechaSalida, NumeroContenedor, DetallesCarga, ContactoDestinatario) VALUES (%s, %s, %s, %s, %s)",
        'productos': "INSERT INTO Productos (Nombre, Precio) VALUES (%s, %s)"
    }
    
    if accion == 'crear':
        return ejecutar_consulta(acciones[entidad], datos)
    elif accion in ('eliminar', 'actualizar') and id_entidad is not None:
        if accion == 'eliminar':
            return ejecutar_consulta(f"DELETE FROM {entidad.capitalize()} WHERE ID = %s", (id_entidad,))
        else:  
            columnas = ', '.join([f"{col} = %s" for col in datos.keys()])
            consulta = f"UPDATE {entidad.capitalize()} SET {columnas} WHERE ID = %s"
            return ejecutar_consulta(consulta, (*datos.values(), id_entidad))
    return False

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        rutas = {
            '/': 'index.html',
            '/cursos': 'gestionar_cursos.html',
            '/empleados': 'gestionar_empleados.html',
            '/reportes': 'gestionar_reportes.html',
            '/capacitacion': 'gestionar_capacitacion.html',
            '/roles': 'gestionar_roles.html',
            '/embarques': 'gestionar_embarques.html',
            '/productos': 'gestionar_productos.html'
        }
        
        if self.path in rutas:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(f'templates/{rutas[self.path]}', 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            self.send_error(404, "404 Not Found")

    def do_POST(self):
        rutas_post = {
            '/login': self.login,
            '/crear_curso': self.crear_curso,
            '/gestionar_empleado': self.gestionar_empleado,
            '/asignar_capacitacion': self.asignar_capacitacion,
            '/gestionar_roles': self.gestionar_roles,
            '/gestionar_embarque': self.gestionar_embarque,
            '/gestionar_producto': self.gestionar_producto
        }
        
        if self.path in rutas_post:
            rutas_post[self.path]()
        else:
            self.send_error(404, "404 Not Found")

    def login(self):
        self._procesar_post(['correo', 'contrasena'], lambda data: validar_usuario(data['correo'], data['contrasena']))

    def crear_curso(self):
        self._procesar_post(['nombre', 'detalles'], lambda data: gestionar_entidad('cursos', 'crear', datos=(data['nombre'], data['detalles'])))

    def gestionar_empleado(self):
        self._procesar_post(['accion', 'empleado_id', 'datos'], lambda data: gestionar_entidad('empleados', data['accion'], data['empleado_id'], data['datos']))

    def asignar_capacitacion(self):
        self._procesar_post(['empleado_id', 'curso_id'], lambda data: gestionar_entidad('capacitacion', 'crear', datos=(data['empleado_id'], data['curso_id'])))

    def gestionar_roles(self):
        self._procesar_post(['accion', 'rol_id', 'datos'], lambda data: gestionar_entidad('roles', data['accion'], data['rol_id'], data['datos']))

    def gestionar_embarque(self):
        self._procesar_post(['accion', 'embarque_id', 'datos'], lambda data: gestionar_entidad('embarques', data['accion'], data['embarque_id'], data['datos']))

    def gestionar_producto(self):
        self._procesar_post(['accion', 'producto_id', 'datos'], lambda data: gestionar_entidad('productos', data['accion'], data['producto_id'], data['datos']))

    def _procesar_post(self, campos, funcion):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        if all(campo in data for campo in campos):
            if funcion(data):
                self._enviar_respuesta(200, {'mensaje': 'Operación realizada con éxito'})
            else:
                self._enviar_respuesta(500, {'mensaje': 'Error al realizar la operación'})
        else:
            self._enviar_respuesta(400, {'mensaje': 'Datos incompletos'})

    def _enviar_respuesta(self, codigo, mensaje):
        self.send_response(codigo)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(mensaje).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor corriendo en http://localhost:{port}/')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
