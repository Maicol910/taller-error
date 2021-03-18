import src.config.globals as globals

class productosModel():
    def traerTodos(self):
        cursor = globals.DB.cursor()
        
        cursor.execute('select * from productos')
        
        productos = cursor.fetchall()

        cursor.close()

        return productos

    def crear(self, nombre, descripcion, precio_venta, precio_compra, ganancia, estado):
        cursor = globals.DB.cursor()

        cursor.execute('insert into productos(nombre, descripcion, precio_venta, precio_compra,ganancia, estado) values(?, ?, ?, ?, ?, ?)',(nombre, descripcion, precio_venta, precio_compra, ganancia, estado,))

        cursor.close()

    def editar(self,id,nombre, descripcion, precio_venta, precio_compra,ganancia, estado):
        cursor = globals.DB.cursor()

        cursor.execute('update productos set nombre=?, descripcion=?, precio_venta=?, precio_compra=?, ganancia=?, estado=? where id=?',(nombre, descripcion, precio_venta, precio_compra,ganancia, estado,id,))

        cursor.close()

    def datos(self,id):
        cursor = globals.DB.cursor()

        cursor.execute('select * from productos where id = ?',(id,))
        
        productos = cursor.fetchone()
        
        cursor.close()

        return productos
    
    def eliminar(self,id):
        cursor = globals.DB.cursor()

        cursor.execute('DELETE FROM productos WHERE id=?',(id,))

        cursor.close()

    