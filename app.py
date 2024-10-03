from flask import Flask, render_template, request, redirect, url_for, flash
from models.user import User
from config import db

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
