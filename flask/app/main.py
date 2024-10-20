from flask import Flask, render_template, request, redirect, url_for
from cliente import Cliente
from cotizacion import Cotizacion
from ventana import Ventana
from nave import Nave

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar la cotización
@app.route('/cotizar', methods=['POST'])
def cotizar():
    # Obtener datos del formulario
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    direccion = request.form['direccion']
    cantidad_ventanas = int(request.form['cantidad_ventanas'])

    # Crear el cliente
    cliente = Cliente(nombre=nombre, cedula=cedula, direccion=direccion)

    # Crear la cotización
    cotizacion = Cotizacion(cliente)

    # Procesar cada ventana
    for i in range(cantidad_ventanas):
        alto = float(request.form[f"alto_{i}"])
        ancho = float(request.form[f"ancho_{i}"])
        estilo = request.form[f"estilo_{i}"].upper()
        acabado = request.form[f"acabado_{i}"]
        vidrio = request.form[f"vidrio_{i}"]
        esmerilado = request.form[f"esmerilado_{i}"] == 'sí'

        # Crear una nueva nave
        nave = Nave(tipo_de_acabado=acabado, tipo_de_vidrio=vidrio, esmerilado=esmerilado, alto=alto, ancho_ventana=ancho, cantidad_naves=len(estilo), estilo=estilo)
        precio_nave = nave.calcular_precio_nave()

        # Crear la ventana y agregarla a la cotización
        ventana = Ventana(estilo=estilo, alto=alto, ancho=ancho, valor_nave=precio_nave, nave=nave)
        cotizacion.agregar_ventana(ventana)

    # Calcular el total
    total = cotizacion.calcular_total()

    # Redirigir a una página para mostrar la cotización
    return render_template('cotizacion.html', cliente=cliente, ventanas=cotizacion.ventanas, total=total)

if __name__ == '__main__':
    app.run(debug=True)
