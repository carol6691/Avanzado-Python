from flask import Flask, render_template, redirect, url_for
from werkzeug.utils import redirect

from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave_secreta_123S'

titulo_app = 'Zona Fit (GYM)'

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') #url: http://localhost:5000/index.html
def inicio():
    app.logger.debug(('Entramos al path de inicio'))
    #recuperamos los clientes de la db
    clientes_db = ClienteDAO.listar_cliente()
    #creamos un objeto de cliente form vacio
    cliente1 = Cliente()
    cliente_forma = ClienteForma(obj=cliente1)
    return render_template('index.html', titulo=titulo_app,
                           clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    #creamos los objetos de clientes inicialmente vacios
    cliente1 = Cliente()
    cliente_forma = ClienteForma(obj=cliente1)
    #validar si lo que hemos agregado son valores requeridos,
    # también si es un valor de tipo entero,
    # y también se aprovecha para validar el tipo de metodo
    if cliente_forma.validate_on_submit():
        #llenamos el objeto cliente con los valores del formulario
        # (incluido el valor oculto de id)
        cliente_forma.populate_obj(cliente1)
        if not cliente1.id:
            ClienteDAO.agregar_cliente(cliente1)
        else:
            ClienteDAO.actualizar_cliente(cliente1)
    #redireccionar a la pagina de inicio (def inicio()), no a la plantilla (index.html)
    #para que nos vuelva a cargar todos los datos en la tabla
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>') #procesamos peticiones de localhost:5000/editar/1
def editar(id):
    cliente = ClienteDAO.listar_cliente_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    # recuperar el listado de clientes para mostrarlo
    clientes_db = ClienteDAO.listar_cliente()
    return render_template('index.html', titulo=titulo_app,
                            clientes=clientes_db, forma=cliente_forma)

@app.route('/eliminar/<int:id>') #procesamos peticiones de localhost:5000/eliminar/1
def eliminar(id):
    cliente1 = Cliente(id=id)
    ClienteDAO.eliminar_cliente(cliente1)
    return redirect(url_for('inicio'))

if __name__ =='__main__':
    app.run(debug=True)