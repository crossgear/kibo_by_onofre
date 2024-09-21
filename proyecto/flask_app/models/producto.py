from ..config.mysqlconnection import connectToMySQL

class Producto:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.precio = data['precio']
        self.descuento = data['descuento']
        self.imagen = data['imagen']
        self.stock_ideal = data['stock_ideal']
        self.stock_disponible = data['stock_disponible']
        self.stock_minimo = data['stock_minimo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.marca_id = data['marca_id']
        self.categoria_id = data['categoria_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM productos;"
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        productos = []
        for row in results:
            productos.append(cls(row))
        return productos
    
    @classmethod
    def get_nuevos(cls):
        query = """ SELECT * FROM productos  WHERE stock_disponible > 0 
                    ORDER BY created_at desc LIMIT 12; """
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        productos = []
        for row in results:
            productos.append(cls(row))
        return productos
    
    @classmethod
    def get_descuentos(cls):
        query = """ SELECT * FROM productos  WHERE stock_disponible > 0 AND descuento > 0
                    ORDER BY descuento desc LIMIT 12; """
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        productos = []
        for row in results:
            productos.append(cls(row))
        return productos
    
    @classmethod
    def get_carrito(cls, ids):
        productos = []
        for id in ids:
            query = f"SELECT * FROM productos WHERE id = {id};"
            mysql = connectToMySQL('proyecto_grupal_bd')
            result = mysql.query_db(query)
            productos.append(cls(result[0]))
        return productos

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM productos WHERE id = %(id)s;"
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
    def get_busqueda_nombre(cls, data):
        query = "SELECT * FROM productos WHERE nombre LIKE '%{}%';".format(data['busqueda'])
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        productos = []
        for row in results:
            productos.append(cls(row))
        return productos

    @classmethod
    def get_busqueda_marca(cls, data):
        query = """ SELECT * FROM productos 
                    left join marcas on productos.marca_id = marcas.id
                    where marcas.nombre LIKE '%{}%';""".format(data['busqueda'])
        print(query)
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        productos = []
        for row in results:
            productos.append(cls(row))
        return productos
    
    @classmethod
    def get_busqueda_categoria(cls, data):
        query = """ SELECT * FROM productos 
                    left join categorias on productos.categoria_id = categorias.id
                    where categorias.nombre LIKE '%{}%';""".format(data['busqueda'])
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        productos = []
        for row in results:
            productos.append(cls(row))
        return productos

    @classmethod
    def get_stock(cls, id):
        query = "SELECT stock_disponible FROM productos WHERE id = %(id)s;"
        data = {
            "id" : id
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query,data)
        if len(result) > 0:
            return result[0]['stock_disponible']
        else:
            return None
        
    @classmethod
    def getProducto(cls,data):
        query = "SELECT * FROM productos WHERE nombre LIKE '' OR descripcion LIKE '';"
        results = connectToMySQL('proyecto_grupal_bd').query_db(query,data)
        if len(results) > 0:
            return results
        else:
            return None

    @classmethod
    def get_stocks_minimos(cls):
        query = "SELECT * FROM productos  WHERE stock_disponible <= stock_minimo"
        mysql = connectToMySQL('proyecto_grupal_bd')
        results = mysql.query_db(query)
        productos = []
        for row in results:
            productos.append(row)
        return productos

    @classmethod
    def save(cls,data):
        query = """INSERT INTO productos (nombre, descripcion, precio, descuento, imagen, stock_ideal, stock_disponible, stock_minimo, created_at, 
        updated_at, marca_id, categoria_id) VALUES (%(nombre)s, %(descripcion)s, %(precio)s, 0, %(imagen)s, 
        %(stock_ideal)s, %(stock_disponible)s, %(stock_minimo)s, NOW(), NOW(), %(marca_id)s, %(categoria_id)s);"""
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)
    
    @classmethod
    def save_lista(cls,data):
        query = """INSERT INTO productos_favoritos (created_at, usuario_id, producto_id) VALUES (NOW(), %(usuario_id)s, %(producto_id)s);"""
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)

    @classmethod
    def update_producto(cls, data):
        if 'imagen' in data:
            query = """UPDATE productos SET nombre = %(nombre)s, descripcion = %(descripcion)s, precio = %(precio)s, 
            stock_ideal = %(stock_ideal)s, stock_disponible = %(stock_disponible)s, stock_minimo = %(stock_minimo)s, updated_at = NOW(),
            marca_id = %(marca_id)s, descuento= %(descuento)s, imagen = %(imagen)s, categoria_id = %(categoria_id)s WHERE id = %(id)s"""
        else:
            query = """UPDATE productos SET nombre = %(nombre)s, descripcion = %(descripcion)s, precio = %(precio)s, 
            stock_ideal = %(stock_ideal)s, stock_disponible = %(stock_disponible)s, stock_minimo = %(stock_minimo)s, updated_at = NOW(),
            marca_id = %(marca_id)s, descuento= %(descuento)s, categoria_id = %(categoria_id)s WHERE id = %(id)s"""
        return connectToMySQL('proyecto_grupal_bd').query_db(query, data)

    @classmethod
    def update_stock(cls, id):
        query = "UPDATE productos SET stock_disponible = stock_ideal WHERE id = %(id)s"
        data = {
            "id" : id
        }
        return connectToMySQL('proyecto_grupal_bd').query_db(query, data)
    
    @classmethod
    def delete_producto_lista(cls, id):
        query = "DELETE FROM productos_favoritos WHERE producto_id = %(id)s"
        data = {
            "id" : id
        }
        return connectToMySQL('proyecto_grupal_bd').query_db(query, data)

    @classmethod
    def update_venta(cls, data):
        query = "UPDATE productos SET stock_disponible = stock_disponible - %(cantidad)s WHERE id = %(id)s"
        return connectToMySQL('proyecto_grupal_bd').query_db(query, data)
    
    @staticmethod
    def obtener_id_siguiente():
        query = "SELECT MAX(id) as siguiente FROM productos;"
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query)
        if result[0]["siguiente"] != None:
            return result[0]['siguiente'] + 1
        else:
            return 1
        
    @staticmethod
    def stock_minimo_alcanzado(id):
        query = "SELECT * FROM productos WHERE stock_disponible <= stock_minimo AND id = %(id)s;"
        data = {
            "id" : id
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query, data)
        if result:
            return True
        else:
            return False

    @staticmethod
    def obtener_precio(id):
        query = "SELECT precio, descuento FROM productos WHERE id = %(id)s;"
        data = {
            "id" : id
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query,data)
        if result[0]["descuento"] == 0:
            return result[0]['precio']
        else:
            precio = result[0]['precio'] -  result[0]['precio'] * result[0]['descuento'] / 100
            return int(precio)

    @staticmethod
    def obtener_marca(id):
        query = "SELECT nombre FROM marcas WHERE id = %(id)s;"
        data = {
            "id" : id
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query,data)
        if len(result) > 0:
            return result[0]['nombre']
        else:
            return "Marca indeterminada"

    @staticmethod
    def obtener_categoria(id):
        query = "SELECT nombre FROM categorias WHERE id = %(id)s;"
        data = {
            "id" : id
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        result = mysql.query_db(query,data)
        if len(result) > 0:
            return result[0]['nombre']
        else:
            return "Categoria indeterminada"


    @staticmethod
    def get_correos_alerta(id):
        query = """SELECT correo FROM USUARIOS INNER JOIN productos_favoritos ON 
        usuarios.id = productos_favoritos.usuario_id WHERE productos_favoritos.producto_id = %(id)s;"""
        data = {
            "id" : id
        }
        mysql = connectToMySQL('proyecto_grupal_bd')
        lista = []
        correos = mysql.query_db(query,data)
        for correo in correos:
            lista.append(correo["correo"])
        return lista


