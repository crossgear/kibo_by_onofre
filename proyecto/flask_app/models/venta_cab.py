from ..config.mysqlconnection import connectToMySQL

class Venta_cab:
    def __init__(self,data):
        self.id = data['id']
        self.fecha = data['fecha']
        self.total = data['total']
        self.usuario_id = data['usuario_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ventas_cab (fecha, usuario_id) VALUES (NOW(), %(usuario_id)s);"
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE ventas_cab SET total =  %(total)s WHERE id = %(id)s;"
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)
    
    @staticmethod
    def obtener_id_venta():
        query = "SELECT MAX(id) as id FROM ventas_cab;"
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query)
        if result[0]["id"] != None:
            return result[0]['id']
        else:
            return 1
