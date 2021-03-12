from flask import render_template, request, redirect, url_for, flash
from src import app
from src.models.productos import productosModel
from src.config.db import DB

@app.route('/productos')
def productos():

    ProductosModel = productosModel() 

    productos = ProductosModel.traerTodos()
    
    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    # esta funcion sirve para mostral el formulario
    # y para crear un nuevo producto 
    # estos pasos se identifican con los metodos

    if request.method == 'GET':
        # mostrar el formulario de creacion
        return render_template ('productos/crear.html')
    
    # la creacion del producto 
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_venta = request.form.get('precio_venta')
    precio_compra = request.form.get('precio_compra')
    ganancia = request.form.get ('ganancia')
    estado = request.form.get('estado')
    
    ProductosModel = productosModel()

    ProductosModel.crear(nombre, descripcion, precio_venta, precio_compra, ganancia, estado)

    return redirect(url_for('productos'))

@app.route('/productos/editar/<int:id>', methods=['GET','POST'])
def editar_produc(id):
    if request.method == 'GET':
        # mostrar el formulario de edicion
        return render_template('productos/editar.html')

    #id = request.form.get('Id')
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_venta = request.form.get('precio_venta')
    precio_compra = request.form.get('precio_compra')
    ganancia = request.form.get ('ganancia')
    estado = request.form.get('estado')

    ProductosModel = productosModel()

    ProductosModel.editar(id,nombre, descripcion, precio_venta, precio_compra,ganancia, estado)
        
    return redirect(url_for('productos'))