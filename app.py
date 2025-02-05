from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

productos = [
    {'id': 1, 'nombre': 'Producto 1', 'precio': 10.0, 'imagen': 'producto1.jpg'},
    {'id': 2, 'nombre': 'Producto 2', 'precio': 20.0, 'imagen': 'producto2.jpg'},
    {'id': 3, 'nombre': 'Producto 3', 'precio': 30.0, 'imagen': 'producto3.jpg'}
]

carrito_c = []

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar/<int:producto_id>')
def agregar(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    
    if producto:
        carrito_c.append(producto) 
    return redirect(url_for('index'))

@app.route('/carrito')
def carrito():
    if not isinstance(carrito_c, list):
        carrito_c = []
        
    total = sum(item['precio'] for item in carrito_c)  
    return render_template('carrito.html', carrito=carrito_c, total=total)

if __name__ == '__main__':
    app.run(debug=True)
