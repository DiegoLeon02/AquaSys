import os
from db_manager import DatabaseManager
from utils import UserManager, EventManager, CourseManager

DB_PATH = 'database/aquasys.db'

def initialize_database():
    """Dicho apartado crea la base de datos en caso de que no exista (TEMPORAL mientras se ve el funcionamiento)"""
    if not os.path.exists(DB_PATH):
        db = DatabaseManager(DB_PATH)
        db.create_tables()

def main():
    initialize_database()
    user_manager = UserManager(DB_PATH)
    event_manager = EventManager(DB_PATH)
    course_manager = CourseManager(DB_PATH)

    print("Bienvenido al Sistema AQUASYS.")
    
    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Gestión de cursos")
        print("4. Gestión de eventos")
        print("5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            email = input("Correo electrónico: ")
            password = input("Contraseña: ")
            if user_manager.login(email, password):
                print(f"Bienvenido {email}.")
            else:
                print("Credenciales incorrectas.")

        elif choice == "2":
            email = input("Correo electrónico: ")
            password = input("Contraseña: ")
            if user_manager.register(email, password):
                print(f"Usuario {email} registrado exitosamente.")
            else:
                print("El usuario ya existe.")

        elif choice == "3":
            print("\nGestión de Cursos")
            manage_courses(course_manager)

        elif choice == "4":
            print("\nGestión de Eventos")
            manage_events(event_manager)

        elif choice == "5":
            break

        else:
            print("Opción no válida.")

def manage_courses(course_manager):
    while True:
        print("\n1. Subir curso")
        print("2. Editar curso")
        print("3. Borrar curso")
        print("4. Volver")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            title = input("Título del curso: ")
            description = input("Descripción del curso: ")
            file_path = input("Ruta del archivo del curso (sube el archivo manualmente a la carpeta 'uploads/'): ")
            course_manager.add_course(title, description, file_path)
            print(f"Curso '{title}' subido con éxito.")

        elif choice == "2":
            course_id = input("ID del curso a editar: ")
            new_title = input("Nuevo título del curso: ")
            new_description = input("Nueva descripción del curso: ")
            course_manager.edit_course(course_id, new_title, new_description)
            print("Curso editado exitosamente.")

        elif choice == "3":
            course_id = input("ID del curso a eliminar: ")
            course_manager.delete_course(course_id)
            print("Curso eliminado con éxito.")

        elif choice == "4":
            break

        else:
            print("Opción no válida.")

def manage_events(event_manager):
    while True:
        print("\n1. Crear evento")
        print("2. Editar evento")
        print("3. Borrar evento")
        print("4. Volver")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            name = input("Nombre del evento: ")
            location = input("Ubicación: ")
            date = input("Fecha: ")
            event_manager.add_event(name, location, date)
            print(f"Evento '{name}' creado con éxito.")

        elif choice == "2":
            event_id = input("ID del evento a editar: ")
            new_name = input("Nuevo nombre del evento: ")
            new_location = input("Nueva ubicación: ")
            new_date = input("Nueva fecha: ")
            event_manager.edit_event(event_id, new_name, new_location, new_date)
            print("Evento editado exitosamente.")

        elif choice == "3":
            event_id = input("ID del evento a eliminar: ")
            event_manager.delete_event(event_id)
            print("Evento eliminado con éxito.")

        elif choice == "4":
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
