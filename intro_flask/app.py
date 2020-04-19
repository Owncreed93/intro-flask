from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/images')
def hello_images():
    div = '<h1> Probando páginas pues bandido </h1>'
    return div


@app.route('/datos')
def datos(nombre = "invitado", edad = 27):
    nombre = request.args.get('nombre', nombre)
    edad = request.args.get('edad', edad)
    return f"<p>Hola {nombre} tu edad es de {edad}</p>"

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1 = 0, num2 = 0):
    resultado = num1 + num2
    return f"{num1} más {num2} igual a {resultado}"

if __name__ == "__main__":
    app.run(debug=True)

