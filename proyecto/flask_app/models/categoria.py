from ..config.mysqlconnection import connectToMySQL

class Categoria:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM categorias;"
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        marcas = []
        for row in results:
            marcas.append(cls(row))
        return marcas

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM categorias WHERE id = %(id)s;"
        data = {
            "id" : id
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return result[0]
        else:
            return None

    @classmethod
    def save(cls,data):
        query = "INSERT INTO categorias (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"""
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)
    
    @classmethod
    def updated(cls, data):
        query = "UPDATE categorias SET nombre = %(nombre)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)



