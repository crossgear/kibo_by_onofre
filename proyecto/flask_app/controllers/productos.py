from flask_app import app
from flask import render_template, request, redirect, session, flash, jsonify
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message

from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto
from ..models.user import User
from ..models.venta_cab import Venta_cab

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "kibo.ventas02@gmail.com"
app.config['MAIL_PASSWORD'] = "viyfsaiyxdxfomne" 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = "kibo.ventas02@gmail.com"

mail = Mail(app)

@app.route('/dashboard/productos')
def producto():
    return render_template('/dashboard/productos.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/process_producto', methods=['POST'])
def registrar_producto():
    if request.method == 'POST':
        path_database = None
        if request.files["imagen"].filename != "":
            EXTENSIONES_PERMITIDAS = set([".png", ".jpg", ".jpeg"])
            file     = request.files['imagen']
            basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
            direccion = Path(basepath)

            filename = secure_filename(file.filename) #Nombre original del archivo
            
            #capturando extension del archivo ejemplo: (.png, .jpg)
            extension = os.path.splitext(filename)[1]
            #validando la extension
            if not extension in EXTENSIONES_PERMITIDAS:
                return jsonify(mensaje = "Imagen no válida, las extensiones permitidas son .png, .jpg, .jpeg")

            nuevoNombreFile     = str(Producto.obtener_id_siguiente()) + extension
            #direccion.parents[0] retrocede una carpeta
            upload_path = os.path.join (direccion.parents[0], 'static/files', nuevoNombreFile) 
            file.save(upload_path)
            path_database = f"/static/files/{nuevoNombreFile}"

        data = {
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "precio": request.form["precio"],
            "imagen": path_database,
            "stock_ideal": request.form["stock_ideal"],
            "stock_disponible": request.form["stock_disponible"],
            "stock_minimo": request.form["stock_minimo"],
            "marca_id": request.form["marca"],
            "categoria_id": request.form["categoria"]
        }
        Producto.save(data)
        return redirect('/dashboard/productos')
    else:
        return redirect('/dashboard/productos')

@app.route('/process_categoria', methods=['POST'])
def registrar_categoria():
    if request.method == 'POST':
        data = {
            "nombre":request.form['nombre'],
        }
        Categoria.save(data)
        return redirect('/dashboard/productos')
    else:
        return redirect('/dashboard/productos')
    
@app.route('/process_marca', methods=['POST'])
def registrar_marca():
    if request.method == 'POST':
        data = {
            "nombre":request.form['nombre'],
        }
        Marca.save(data)
        return redirect('/dashboard/productos')
    else:
        return redirect('/dashboard/productos')
    
@app.route('/dashboard/modificar_producto')
def actualizar_producto():
    return render_template('/dashboard/actualizar_producto.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/dashboard/reporte')
def mostrar_reporte():
    return render_template('/dashboard/reporte_stock.html', productos = Producto.get_stocks_minimos())

@app.route('/reponer_stock/<int:id>')
def reponer_stock(id):
    if Producto.get_stock(id) == 0:
        clientes = Producto.get_correos_alerta(id)
        if clientes != None:
                producto = Producto.get_one(id)
                msg = Message(recipients=clientes,
                                subject="¡El producto que buscabas está de vuelta en stock! ¡No te lo pierdas!"
                            )
                # Define el contenido del mensaje
                msg.html = f"""<h3>¡Estimado cliente!</h3>
                <p>¡Grandes noticias! El producto, {producto['nombre']}, que tanto buscabas ya se encuentra disponible nuevamente. ¡No dejes pasar esta oportunidad única para hacerte con él!</p>
                <img src='cid:image1' style='max-width: 400px; height: auto;'>
                <p>No pierdas más tiempo y haz tu compra ahora mismo. ¡Estamos seguros de que te encantará!</p>
                <p>Gracias por confiar en Kibo como tu tienda de preferencia.</p>"""

                with app.open_resource(producto['imagen'][1:]) as fp:
                        msg.attach("image.jpg", "image/jpeg", fp.read(), "inline", headers=[['Content-ID','<image1>']])
                mail.send(msg)
                Producto.delete_producto_lista(id)
    Producto.update_stock(id)
    return redirect("/dashboard/modificar_producto")


@app.route('/obtener_producto/<int:id>')
def obtener_producto(id):
    producto = Producto.get_one(id)
    return jsonify(producto)

@app.route('/process_actualizar_producto', methods=['POST'])
def proceso_actualizar_producto():
    if request.method == 'POST':
        path_database = None
        data = {}
        if request.files["imagen"].filename != "":
            EXTENSIONES_PERMITIDAS = set([".png", ".jpg", ".jpeg"])
            file     = request.files['imagen']
            basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
            direccion = Path(basepath)

            filename = secure_filename(file.filename) #Nombre original del archivo
            
            #capturando extension del archivo ejemplo: (.png, .jpg)
            extension = os.path.splitext(filename)[1]
            #validando la extension
            if not extension in EXTENSIONES_PERMITIDAS:
                flash("Imagen no válida, las extensiones permitidas son .png, .jpg, .jpeg")
                return ("/dashboard/productos")

            nuevoNombreFile     = str(request.form["id"]) + extension
            #direccion.parents[0] retrocede una carpeta
            upload_path = os.path.join (direccion.parents[0], 'static/files', nuevoNombreFile) 
            file.save(upload_path)
            path_database = f"/static/files/{nuevoNombreFile}"
            data = {
                "id": request.form["id"],
                "nombre": request.form["nombre"],
                "descripcion": request.form["descripcion"],
                "precio": request.form["precio"],
                "imagen": path_database,
                "stock_ideal": request.form["stock_ideal"],
                "stock_disponible": request.form["stock_disponible"],
                "stock_minimo": request.form["stock_minimo"],
                "descuento": request.form["descuento"],
                "marca_id": request.form["marca"],
                "categoria_id": request.form["categoria"]
            }
        else:
            data = {
                "id": request.form["id"],
                "nombre": request.form["nombre"],
                "descripcion": request.form["descripcion"],
                "precio": request.form["precio"],
                "stock_ideal": request.form["stock_ideal"],
                "stock_disponible": request.form["stock_disponible"],
                "stock_minimo": request.form["stock_minimo"],
                "descuento": request.form["descuento"],
                "marca_id": request.form["marca"],
                "categoria_id": request.form["categoria"]
            }
        Producto.update_producto(data)
        return redirect('/dashboard/modificar_producto')
    else:
        return redirect('/dashboard/modificar_producto')

@app.route('/producto_seleccionado/<int:id>')
def producto_seleccinado(id):
    producto = Producto.get_one(id)
    if producto != None:
        return render_template('producto_seleccionado.html', producto = producto, funciones = Producto)
    else:
        return redirect("/")
    
@app.route("/process_notificaciones")
def obtener_lista_productos():
    bajo_stock = Producto.get_stocks_minimos()
    return jsonify(bajo_stock)

@app.route('/lista_deseo_add', methods=['POST'])
def agregar_lista_deseo():
    if request.method == 'POST':
        if "user_id" in session:
            data = {
                "usuario_id": session['user_id'],
                "producto_id": request.form["id"]
            }
            Producto.save_lista(data)
            flash("Producto agregado correctamente")
            return redirect('/')
        else:
            flash("Inicia sesión para poder agregar productos a tu lista de deseos")
            return redirect('/producto_seleccionado/'+request.form["id"])
    else:
        return redirect('/')

@app.route('/carrito_add', methods=['POST'])
def agregar_carrito():
    listaNueva = []
    if request.method == 'POST':
        id = request.form.get("id")
        if "user_id" in session:
            if request.form.get("cantidad") != "" and int(request.form.get("cantidad")) > 0:
                cantidad = int(request.form.get("cantidad"))
                stock = Producto.get_stock(id)
                if stock >= cantidad:
                    if not "carrito" in session:
                        session["carrito"] = []
                        session["carrito"].append([id, cantidad])
                        listaNueva = session["carrito"].copy()
                    else:
                        #Consula si el articulo se habia agregado previamente
                        existe = False
                        cantidad_anterior = 0
                        indice = None
                        for idx, articulo in enumerate(session["carrito"]):
                            if id == articulo[0]:
                                existe = True
                                cantidad_anterior = articulo[1]
                                indice = idx
                                break
                        #si se habia agregado previamente consulta si hay stock suficiente
                        if existe:
                            if stock >= (cantidad + cantidad_anterior):
                                #si hay stock se actualiza la cantidad
                                session["carrito"][indice][1] = cantidad + cantidad_anterior
                                listaNueva = session["carrito"].copy()
                            else:
                                flash(f"Stock Insuficiente solo quedan {stock - cantidad_anterior} en existencia")
                                return redirect('/producto_seleccionado/'+id)
                        else:
                            session["carrito"].append([id, cantidad])
                            listaNueva = session["carrito"].copy()
                    session["nuevo"] = listaNueva
                    return redirect('/carrito')
                else:
                    flash(f"Stock Insuficiente solo quedan {stock} en existencia")
                    return redirect('/producto_seleccionado/'+id)
            else:
                flash("Completa la cantidad de artículos que deseas comprar")
                return redirect('/producto_seleccionado/'+id)
        else:
            flash("Inicia sesión para poder agregar productos")
            return redirect('/producto_seleccionado/'+id)
    else:
        return redirect('/')
    
@app.route('/carrito_delete/<int:id>')
def eliminar_carrito(id):
    if "user_id" in session:
        listaNueva = session["carrito"].copy()
        for idx, articulo in enumerate(session["carrito"]):
            if id == int(articulo[0]):
                session["carrito"].pop(idx)
                listaNueva = session["carrito"].copy()
                break
        session["carrito"] = listaNueva
        return redirect('/carrito')
    else:
        return redirect('/carrito')
    
#TODO: Cambiar el modo de retorno, es decir en ves que devuelva a la pagina principal que devuelva solo el mensaje
@app.route('/carrito')
def mostrar_carrito():
    if "user_id" in session:
        if "carrito" in session and len(session["carrito"]) > 0:
            ids = []
            for producto in session["carrito"]:
                ids.append(producto[0]) 
            data_usuario = {
                "id" : session["user_id"]
            }
            return render_template("finalizar_pedido.html", productos = Producto.get_carrito(ids), usuario = User.getUserId(data_usuario), ventas = Venta_cab)
        else:
            flash("No tienes elementos agregados")
            return redirect("/")
    else:
        flash("Inicia sesión para poder acceder al carrito")
        return redirect("/")