from flask import Flask, render_template, request, redirect, url_for, flash
from models.user import User
from config import db
from forms import ProductoForm  
from database import db_session, init_db
from models.campaign import Campaign  
from forms import CampaignForm

app = Flask(__name__)
app.secret_key = 'secret_key'  # Para las sesiones y los mensajes flash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validar si el usuario existe en la base de datos
        user = User.query.filter_by(username=username).first()
        
        if user and user.verify_password(password):
            # Redirigir al menú principal
            return redirect(url_for('main_menu'))
        else:
            flash('Credenciales incorrectas')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/main_menu')
def main_menu():
    return "Bienvenido al menú principal"

if __name__ == '__main__':
    app.run(debug=True)

# Ruta para añadir productos al inventario
@app.route('/productos', methods=['GET', 'POST'])
def crear_producto():
    form = ProductoForm(request.form)

    if request.method == 'POST' and form.validate():
        # Verifica si el producto ya existe por su código
        producto_existente = Producto.query.filter_by(codigo=form.codigo.data).first()
        if producto_existente:
            flash('Producto existente', 'error')
            return redirect(url_for('crear_producto'))

        # Crear nuevo producto
        nuevo_producto = Producto(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            codigo=form.codigo.data,
            cantidad=form.cantidad.data,
            precio=form.precio.data
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        flash('Producto añadido correctamente', 'success')
        return redirect(url_for('crear_producto'))

    return render_template('productos.html', form=form)

from models.product import Producto

# Ruta para crear una nueva campaña publicitaria
@app.route('/campanas', methods=['GET', 'POST'])
def crear_campana():
    form = CampaignForm(request.form)

    if request.method == 'POST' and form.validate():
        # Verifica si la campaña ya existe por nombre
        campana_existente = Campaign.query.filter_by(nombre=form.nombre.data).first()
        if campana_existente:
            flash('Campaña existente', 'error')
            return redirect(url_for('crear_campana'))

        # Crear nueva campaña
        nueva_campana = Campaign(
            nombre=form.nombre.data,
            objetivo=form.objetivo.data,
            fecha_inicio=form.fecha_inicio.data,
            fecha_fin=form.fecha_fin.data,
            texto_principal=form.texto_principal.data,
            multimedia=form.multimedia.data.filename if form.multimedia.data else None  # Manejo opcional de multimedia
        )
        db_session.add(nueva_campana)
        db_session.commit()
        flash('Campaña añadida correctamente', 'success')
        return redirect(url_for('crear_campana'))

    return render_template('crear_campana.html', form=form)

# Ruta para eliminar una campaña
@app.route('/eliminar_campana/<int:id>', methods=['POST'])
def eliminar_campana(id):
    campana = Campaign.query.get(id)
    if campana:
        db_session.delete(campana)
        db_session.commit()
        flash('Campaña eliminada correctamente', 'success')
    else:
        flash('Campaña no encontrada', 'error')
    return redirect(url_for('crear_campana'))
