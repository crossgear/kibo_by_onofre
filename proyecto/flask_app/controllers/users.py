from flask_app import app
from flask import render_template, request, redirect, session, flash
import os
from pathlib import Path
from werkzeug.utils import secure_filename

from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto
from flask_bcrypt import Bcrypt
from ..models.user import User

bcrypt = Bcrypt(app)

app.secret_key = 'secret_key'

@app.route('/')
def index():
    #Traemos los ultimos productos de la base de datos
    ultimos_db = Producto.get_nuevos()
    #Creamos una lista vacía que contendra lista de productos 
    ultimos_productos=[]
    #lista en la que guardaremos productos y que luego agregaremos a una lista de listas
    lista=[]
    #Contador
    j=1

    if len(ultimos_db)<4:
        ultimos_productos.append(ultimos_productos)
    else:
        for producto in ultimos_db:
            lista.append(producto)
            if (j%4==0):
                ultimos_productos.append(lista)
                lista=[]
            j+=1

    #Traemos los productos con mas descuento de la base de datos
    descuentos_db = Producto.get_descuentos()
    #Lista de lista para listas de como maximo 4 productos 
    descuento_productos=[]
    #lista de productos
    lista=[]
    #contador
    j=1
    
    if len(descuentos_db)<4:
        descuento_productos.append(descuentos_db)
    else:
        for producto in descuentos_db:
            lista.append(producto)
            if (j%4==0):
                descuento_productos.append(lista)
                lista=[]
            j+=1
    return render_template('index.html', lista_ultimos = ultimos_productos, lista_descuentos = descuento_productos,
                             lista_ultimos_2 = ultimos_db, lista_descuentos_2 = descuentos_db)

@app.route('/buscador', methods=['POST'])
def buscador():
    data = {
        'busqueda': request.form['busqueda'],
        'tipo': request.form['tipo']
    }
    print(data)
    if data['busqueda'] == '':
        productos = Producto.get_all()
    elif data['tipo'] == 'id':
        producto = Producto.get_one(data['busqueda'])
        if producto != None:
            return redirect('/producto_seleccionado/'+str(producto['id']))
        else:
            productos = []
    elif data['tipo'] == 'marca':
        productos = Producto.get_busqueda_marca(data)
    elif data['tipo'] == 'categoria':
        productos = Producto.get_busqueda_categoria(data)
    elif data['tipo'] == 'nombre':
        productos = Producto.get_busqueda_nombre(data)
    return render_template('buscador.html', productos = productos, busqueda = data['busqueda'], tipo = data['tipo'])

@app.route('/registrar', methods=['POST', 'GET'])
def registro():
    if request.method=='POST':
        if request.form['contraseña'] == request.form['confi']:
            if User.validar_usuario(request.form):
                pw_hash = bcrypt.generate_password_hash(request.form['contraseña'])
                data = {
                    'nombre' : request.form['nombre'],
                    'apellido' : request.form['apellido'],
                    'correo' : request.form['correo'],
                    'password' : pw_hash,
                    'direccion' : request.form['direccion'],
                    'celular' : request.form['celular']
                }
                usuario = User.save(data)
                flash("Registro Exitoso!!!")
                return redirect('/')
            else:
                return redirect('/')
        else:
            flash("Las Contraseñas no Coinciden!!!")
            return redirect('/')
    else:
        return redirect('/')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        # ver si el correo de usuario proporcionado existe en la base de datos
        data = {
            "correo" : request.form.get("correo")
        }
        user_in_db = User.getbyEmail(data)

        # usuario no está registrado en la base de datos
        if not user_in_db:
            flash("Email no registrado")
            return redirect('/')
        
        if not bcrypt.check_password_hash(user_in_db.password, request.form['contraseña']):
            # si obtenemos False después de verificar la contraseña
            flash("Password incorrecto")
            return redirect('/')
        
        # si las contraseñas coinciden, configuramos el user_id en sesión
        session['user_id'] = user_in_db.id
        if user_in_db.nivel == 1:
            return redirect('/dashboard')
        else:
            return redirect('/')#, user = session["user_id"])

    else:
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect('/')
    else:
        data ={
            "id" : session['user_id']
        }    
        user_in_db = User.getDataUser(data)
        if user_in_db.nivel == 1:
            return render_template('/dashboard/dashboard.html')
        else:
            return redirect('/')
        

@app.route('/dashboard/productos')
def producto_add():
    return render_template('/dashboard/productos.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/dashboard/perfil')
def perfil():
    data = {
        "id" : session['user_id']
    }
    user = User.getDataUser(data)
    return render_template('/dashboard/perfil.html', user=user)

@app.route('/dashboard/user/<int:id>', methods=['POST','GET'])
def update_user(id):
    if request.method == 'POST':
        datos ={
            'id': id,
            'nombre' : request.form['nombre'],
            'apellido' : request.form['apellido'],
            'celular' : request.form['celular'],
            'direccion' : request.form['direccion'],
            'correo' : request.form['correo']
        }
        if User.validar_perfil(request.form):
            User.update(datos)
            flash("Datos Actualizados!!!")
        else:
            return redirect('/dashboard/perfil')

    return redirect('/dashboard')
    
    


@app.route('/dashboard/change_password', methods=['POST','GET'])
def chg_pass():
    if request.method=='POST':

        if request.form['contraseña'] == request.form['confi']:

            pw_hash = bcrypt.generate_password_hash(request.form['contraseña'])

            data = {
                "id" : session['user_id'],
                "contraseña" : pw_hash,
                "confi" : request.form['confi']
            }
            User.ChangePassword(data)
            flash("Contraseña Cambiada")
            return redirect('/dashboard')

        else:
            flash('Atención. Las contraseñas no coinciden!!!')
            render_template('/dashboard/change_pass.html')
    
    return render_template('/dashboard/change_pass.html')

@app.route('/dashboard/logout')
def logout():
    session.clear()
    return redirect('/')
