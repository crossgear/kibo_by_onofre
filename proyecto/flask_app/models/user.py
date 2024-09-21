from flask import flash
from ..config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
CELL_REGEX = re.compile(r'^((\+595|0)9([6-9][1-6])\d{6})+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.password = data['password']
        self.direccion = data['direccion']
        self.celular = data['celular']
        self.nivel = data['nivel']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getUserId(cls, data):
        query = "SELECT * FROM proyecto_grupal_bd.usuarios where id = %(id)s;"
        results = connectToMySQL('proyecto_grupal_bd').query_db(query,data)
        if len(results) > 0:
            return cls(results[0])
        else:
            return None


    @classmethod
    def save(cls, data):# en principio nivel 0 para todos los clientes
        query = 'INSERT INTO proyecto_grupal_bd.usuarios (nombre, apellido, correo, password, direccion, celular, nivel, created_at, updated_at) VALUES(%(nombre)s, %(apellido)s, %(correo)s, %(password)s, %(direccion)s, %(celular)s, 0, NOW(), NOW());'
        result = connectToMySQL('proyecto_grupal_bd').query_db(query,data)
        print(result)
        data_usuario = {
            'id': result
        }
        return cls.getUserId(data_usuario)

    @classmethod
    def getAllUser(cls):
        query = "SELECT id, nombre, apellido, correo, password, direccion, celular, nivel FROM proyecto_grupal_bd.usuarios;"
        results = connectToMySQL('proyecto_grupal_bd').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def getDataUser(cls, data):
        query = "SELECT id, nombre, apellido, correo, password, direccion, celular, nivel, created_at, updated_at FROM proyecto_grupal_bd.usuarios WHERE id = %(id)s"
        results = connectToMySQL('proyecto_grupal_bd').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE proyecto_grupal_bd.usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, correo=%(correo)s, direccion=%(direccion)s, celular=%(celular)s, updated_at=NOW() WHERE id=%(id)s;"
        print(query)
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)

    @classmethod
    def ChangePassword(cls,data):
        query="UPDATE proyecto_grupal_bd.usuarios SET password=%(contraseña)s WHERE id=%(id)s;"
        print(query)
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)

    @classmethod
    def getbyEmail(cls, data):
        query = "SELECT id, nombre, apellido, correo, password, direccion, celular, nivel, created_at, updated_at FROM proyecto_grupal_bd.usuarios where correo = %(correo)s;"
        results = connectToMySQL('proyecto_grupal_bd').query_db(query,data)
        if len(results) > 0:
            return cls(results[0])
        else:
            return None

    @staticmethod
    def validar_usuario(registro):

        correo={
            "correo":registro['correo']
        }

        celular={
            "celular" : registro['celular']
        }

        is_valid = True
        if len(registro['nombre']) < 3:
            flash("El Nombre debe contener al menos 3 caracteres")
            is_valid = False
        
        if len(registro['apellido']) < 3:
            flash("El Apellido debe contener al menos 3 caracteres")
            is_valid = False

        if len(registro['contraseña']) < 8:
            flash("Password debe tener al menos 8 caracteres")
            is_valid = False

        if not EMAIL_REGEX.match(correo['correo']):
            flash("Email no valido")
            is_valid = False

        if not CELL_REGEX.match(celular['celular']):
            flash("Numero de Celular no válido")
            is_valid = False

        if User.getbyEmail(correo) != None:
            flash("Email ya existente")
            is_valid = False

        return is_valid
    

    @staticmethod
    def validar_perfil(perfil):

        correo={
            "correo" : perfil['correo']
        }

        is_valid = True

        if len(perfil['nombre']) < 3:
            flash("El Nombre debe contener al menos 3 caracteres")
            is_valid = False
    
        if len(perfil['apellido']) < 3:
            flash("El Apellido debe contener al menos 3 caracteres")
            is_valid = False

        if not EMAIL_REGEX.match(perfil['correo']):
            flash("Email no valido")
            is_valid = False

        return is_valid