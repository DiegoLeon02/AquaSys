import os
from db_manager import DatabaseManager
from utils import UserManager, EventManager, CourseManager, ProductManager, CampaignManager

DB_PATH = 'database/aquasys.db'

def initialize_database():
    """Crea la base de datos en caso de que no exista (TEMPORAL mientras se ve el funcionamiento)"""
    if not os.path.exists(DB_PATH):
        db = DatabaseManager(DB_PATH)
        db.create_tables()

def main():
    initialize_database()
    user_manager = UserManager(DB_PATH)
    event_manager = EventManager(DB_PATH)
    course_manager = CourseManager(DB_PATH)
    product_manager = ProductManager(DB_PATH)
    campaign_manager = CampaignManager(DB_PATH)

    print("Bienvenido al Sistema AQUASYS.")
    
    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Gestión de cursos")
        print("4. Gestión de eventos")
        print("5. Gestión de productos")
        print("6. Gestión de campañas")
        print("7. Salir")
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
            print("\nGestión de Productos")
            manage_products(product_manager)

        elif choice == "6":
            print("\nGestión de Campañas")
            manage_campaigns(campaign_manager)

        elif choice == "7":
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

def manage_products(product_manager):
    while True:
        print("\n1. Añadir producto")
        print("2. Editar producto")
        print("3. Borrar producto")
        print("4. Volver")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            name = input("Nombre del producto: ")
            description = input("Descripción del producto: ")
            code = input("Código del producto: ")
            quantity = input("Cantidad del producto: ")
            price = input("Precio del producto: ")
            product_manager.add_product(name, description, code, quantity, price)
            print(f"Producto '{name}' añadido con éxito.")

        elif choice == "2":
            product_id = input("ID del producto a editar: ")
            new_name = input("Nuevo nombre del producto: ")
            new_description = input("Nueva descripción del producto: ")
            new_code = input("Nuevo código del producto: ")
            new_quantity = input("Nueva cantidad del producto: ")
            new_price = input("Nuevo precio del producto: ")
            product_manager.edit_product(product_id, new_name, new_description, new_code, new_quantity, new_price)
            print("Producto editado exitosamente.")

        elif choice == "3":
            product_id = input("ID del producto a eliminar: ")
            product_manager.delete_product(product_id)
            print("Producto eliminado con éxito.")

        elif choice == "4":
            break

        else:
            print("Opción no válida.")

def manage_campaigns(campaign_manager):
    while True:
        print("\n1. Crear campaña")
        print("2. Editar campaña")
        print("3. Borrar campaña")
        print("4. Volver")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            name = input("Nombre de la campaña: ")
            objective = input("Objetivo de la campaña: ")
            start_date = input("Fecha de inicio: ")
            end_date = input("Fecha de finalización: ")
            main_text = input("Texto principal: ")
            multimedia = input("Ruta del archivo multimedia (opcional): ")
            campaign_manager.add_campaign(name, objective, start_date, end_date, main_text, multimedia)
            print(f"Campaña '{name}' creada con éxito.")

        elif choice == "2":
            campaign_id = input("ID de la campaña a editar: ")
            new_name = input("Nuevo nombre de la campaña: ")
            new_objective = input("Nuevo objetivo de la campaña: ")
            new_start_date = input("Nueva fecha de inicio: ")
            new_end_date = input("Nueva fecha de finalización: ")
            new_main_text = input("Nuevo texto principal: ")
            new_multimedia = input("Nueva ruta del archivo multimedia (opcional): ")
            campaign_manager.edit_campaign(campaign_id, new_name, new_objective, new_start_date, new_end_date, new_main_text, new_multimedia)
            print("Campaña editada exitosamente.")

        elif choice == "3":
            campaign_id = input("ID de la campaña a eliminar: ")
            campaign_manager.delete_campaign(campaign_id)
            print("Campaña eliminada con éxito.")

        elif choice == "4":
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
