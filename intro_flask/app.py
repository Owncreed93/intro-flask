from flask import Flask
#from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/images')
def hello_images():
    div = '<h1> Probando páginas pues bandido </h1>'
    return div


@app.route('/datos')
@app.route('/datos/<nombre>/<int:edad>')
def datos(nombre = "invitado", edad = 27):
    #nombre = request.args.get('nombre', nombre)
    #edad = request.args.get('edad', edad)
    #return f"<p>Hola {nombre} tu edad es de {edad}</p>"
    context = {'nombre':nombre, 'edad':edad}
    return render_template('index.html', **context)


@app.route('/suma/<int:num1>/<int:num2>')
@app.route('/suma/<int:num1>/<float:num2>')
@app.route('/suma/<float:num1>/<int:num2>')
@app.route('/suma/<float:num1>/<float:num2>')
def suma(num1 = 0, num2 = 0):
    resultado = num1 + num2
    context = {'num1':num1, 'num2':num2, 'resultado':resultado}
    return render_template('suma.html', **context)

if __name__ == "__main__":
    app.run(debug=True)

