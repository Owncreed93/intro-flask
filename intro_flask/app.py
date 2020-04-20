import json


from flask import (
    Flask, 
    redirect, 
    render_template, 
    request, 
    url_for
)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/images')
def hello_images():
    div = '<h1> Probando páginas pues bandido </h1>'
    return div


@app.route('/datos')
def datos(nombre = "invitado"):
    #nombre = request.args.get('nombre', nombre)
    #edad = request.args.get('edad', edad)
    #return f"<p>Hola {nombre} tu edad es de {edad}</p>"
    
    try:
        data = json.loads(request.cookies.get('data'))
    except TypeError:
        data = {}
    else:
        nombre = data.get('nombre')
        edad = data.get('edad')
        correo = data.get('email')
        comentario = data.get('comentario')
    

    context = {'nombre': nombre, 'edad': edad, 'correo': correo, 'comentario': comentario}
    return render_template('index.html', **context)


@app.route('/suma/<int:num1>/<int:num2>')
@app.route('/suma/<int:num1>/<float:num2>')
@app.route('/suma/<float:num1>/<int:num2>')
@app.route('/suma/<float:num1>/<float:num2>')
def suma(num1 = 0, num2 = 0):
    resultado = num1 + num2
    context = {'num1':num1, 'num2':num2, 'resultado':resultado}
    return render_template('suma.html', **context)

@app.route('/resta/<int:num1>/<int:num2>')
@app.route('/resta/<int:num1>/<float:num2>')
@app.route('/resta/<float:num1>/<int:num2>')
@app.route('/resta/<float:num1>/<float:num2>')
def resta(num1 = 0, num2 = 0):
    resultado = num1 - num2
    context = {'num1':num1, 'num2':num2, 'resultado':resultado}
    return render_template('resta.html', **context)

@app.route('/multiplicacion/<int:num1>/<int:num2>')
@app.route('/multiplicacion/<int:num1>/<float:num2>')
@app.route('/multiplicacion/<float:num1>/<int:num2>')
@app.route('/multiplicacion/<float:num1>/<float:num2>')
def multiplicacion(num1 = 0, num2 = 0):
    resultado = num1 * num2
    context = {'num1':num1, 'num2':num2, 'resultado':resultado}
    return render_template('multiplicacion.html', **context)

@app.route('/division/<int:num1>/<int:num2>')
@app.route('/division/<int:num1>/<float:num2>')
@app.route('/division/<float:num1>/<int:num2>')
@app.route('/division/<float:num1>/<float:num2>')
def division(num1 = 0, num2 = 0):
    resultado = num1 / num2
    context = {'num1':num1, 'num2':num2, 'resultado':resultado}
    return render_template('division.html', **context)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    response = redirect(url_for('datos'))
    response.set_cookie('data', json.dumps(dict(request.form.items())))
    return response

if __name__ == "__main__":
    app.run(debug=True)

