# requirements.py
# Este archivo incluye las dependencias necesarias para el proyecto
dependencies = [
    "Flask",
    "Flask-SQLAlchemy",
    "Werkzeug"
]

# Guardar dependencias en un archivo requirements.txt
if __name__ == "__main__":
    with open("requirements.txt", "w") as f:
        for dep in dependencies:
            f.write(dep + "\n")
