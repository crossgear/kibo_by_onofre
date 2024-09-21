from ..config.mysqlconnection import connectToMySQL

class Venta_det:
    def __init__(self,data):
        self.id = data['id']
        self.cantidad = data['cantidad']
        self.subtotal = data['subtotal']
        self.producto_id = data['producto_id']
        self.venta_cab_id = data['venta_cab_id']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO ventas_det (cantidad, subtotal, producto_id, venta_cab_id)
          VALUES (%(cantidad)s, %(subtotal)s, %(producto_id)s, %(venta_cab_id)s);"""
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)

    @staticmethod
    def obtener_total(id):
        query = "SELECT SUM(subtotal) AS total FROM ventas_det WHERE venta_cab_id = %(id)s;"
        data = {
            "id" : id 
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query,data)
        if result[0]["total"] != None:
            return result[0]['total']
        else:
            return 0