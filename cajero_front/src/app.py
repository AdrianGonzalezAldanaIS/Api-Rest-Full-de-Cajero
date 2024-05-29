"""from flask import Flask
from consumo import cliente_api
from config import config



def page_not_found(error):
    return "<h1> Pagina no encontrada</h1>", 404

def create_app():
    app = Flask(__name__)
    app.secret_key = "2451456769873"
    app.register_blueprint(cliente_api.main, url_prefix='/cajero')
    return app

app = create_app()

if __name__ == '__main__':
    
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run(port = 5000)"""

from flask import Flask, jsonify, render_template, url_for, session, request, redirect
import json
from consumo.cliente_servicio import ClienteServicio
from formularios.tarjeta_forms import TarjetaForm, Nip, Pago

app = Flask(__name__)
app.secret_key = "2451456769873"

@app.route('/')
def index():
    form = TarjetaForm()
    return render_template("formularios/ingresar.html", form = form)

@app.route('/tarjeta', methods=['POST'])
def validar_tarjeta():
    trajeta_form = TarjetaForm()
    if request.method == 'POST':
        cl = ClienteServicio()
        mensaje = ""
        num = request.form['num_tarjeta']
        session['num'] = num
        respuesta = cl.valida_terjeta(num)

        if trajeta_form.validate_on_submit():
            if respuesta['verificada']:
                return redirect(url_for("formNip"))
            else:
                mensaje = respuesta['mensaje']
                return render_template("formularios/ingresar.html", form = trajeta_form, mensaje = mensaje)
    return jsonify({"respuesta":num})

@app.route('/Nip/', methods = ['GET'])
def formNip():
    nip_form = Nip()
    intentos = 0
    mensaje = ""
    if 'intentos' in session and 'mensaje'in session:
        intentos = session['intentos']
        intentos = 0
    return render_template("formularios/nip.html", form = nip_form, mensaje = mensaje, intentos = intentos)




if __name__ == '__main__':
    app.run(debug=True, port=5000)
