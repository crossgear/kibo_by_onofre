from flask_app import app
from flask import render_template, request, redirect, session, flash, jsonify
from flask_mail import Mail, Message
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os
import tempfile

from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto
from ..models.venta_cab import Venta_cab
from ..models.venta_det import Venta_det

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "kibo.ventas02@gmail.com"
app.config['MAIL_PASSWORD'] = "viyfsaiyxdxfomne" 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = "kibo.ventas02@gmail.com"

mail = Mail(app)

@app.route('/pago_exitoso/')
def procesar_venta():
    datos_venta_cab = {
        "usuario_id" : session["user_id"]
    }
    Venta_cab.save(datos_venta_cab)
    ids = []
    for producto_id in session["carrito"]:
        ids.append(producto_id[0])
    faltantes = False
    for idx in range(len(session["carrito"])):
        datos_venta_det = {
            "cantidad" : session["carrito"][idx][1],
            "subtotal" : Producto.obtener_precio(session["carrito"][idx][0]) * session["carrito"][idx][1],
            "producto_id" : session["carrito"][idx][0],
            "venta_cab_id" : Venta_cab.obtener_id_venta(),
        }
        Venta_det.save(datos_venta_det)
        datos_producto = {
            "id" : session["carrito"][idx][0],
            "cantidad" : session["carrito"][idx][1]
        }
        Producto.update_venta(datos_producto)
        #Se comprueba si algun faltante
        if(Producto.stock_minimo_alcanzado(session["carrito"][idx][0])):
            faltantes = True 
    datos_update = {
        "total" : Venta_det.obtener_total(Venta_cab.obtener_id_venta()),
        "id" : Venta_cab.obtener_id_venta()
    }

    if faltantes:
        bajo_stock = Producto.get_stocks_minimos()
        context = {'productos' : bajo_stock}
        template_loader = FileSystemLoader('flask_app/templates')
        template_env = Environment(loader=template_loader)
        template = template_env.get_template('plantilla.html')
        output_text = template.render(context)

        config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
        pdf = pdfkit.from_string(output_text, False, configuration=config, css='flask_app/static/css/style_template.css')
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(pdf)
            tmp.flush()
            tmp.seek(0)
            msg = Message(recipients=["tadeo25.molinas@gmail.com"],
                        body="Este informe detalla los productos que actualmente se encuentran agotados o con cantidades insuficientes en el inventario.",
                        subject="Existencias mínimas alcanzadas",
                    )
            # se agrega el PDF al correo electrónico
            with app.open_resource(tmp.name) as pdf_file:
                msg.attach('reporte_existencias.pdf', 'application/pdf', pdf_file.read())
                mail.send(msg)
                # se elimina el archivo temporal
        os.remove(tmp.name)
    Venta_cab.update(datos_update)
    session.pop('nuevo')
    session.pop('carrito')
    flash("Su pago fue procesado exitosamente.")
    return redirect("/")


@app.route('/pago_cancelado/')
def pago_cancelado():
    flash("Pago cancelado.")
    return redirect("/")

