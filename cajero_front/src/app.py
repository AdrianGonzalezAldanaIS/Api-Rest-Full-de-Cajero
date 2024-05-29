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
    print("Entro a Nip")
    print(session)
    if 'intentos' in session and 'mensaje'in session:
        intentos = session['intentos']
        intentos = 0
    return render_template("formularios/nip.html", form = nip_form, mensaje = mensaje, intentos = intentos)

@app.route('/Cuenta', methods = ['POST'])
def getNip():
    nip_form = Nip()
    cl = ClienteServicio()
    pago_form = Pago()
    
    if request.method == 'POST':        
        mensaje = ""
        mensaje_retiro= ""
        if nip_form.validate_on_submit():
            if 'num' in session:
                num = session['num']
                num_nip = request.form['num_nip']
                respuesta = cl.validate_nip(num, num_nip)
                saldo = cl.verifica_saldo(num)
                limite = cl.verifica_limite(num)
                print("liiimite",limite)
                if respuesta['verificada']:
                    
                    return render_template("formularios/cliente.html", form= pago_form,nombre=saldo['nombre'], saldo = saldo['saldo'], limite = limite['limite'], mensaje = mensaje_retiro) # type: ignore
                else:
                    if respuesta['intentos'] >= 3:
                        return redirect(url_for("index"))
                    session['intentos'] = respuesta['intentos']
                    mensaje = respuesta['mensaje']
            else:
                return redirect(url_for("index"))
    return render_template("formularios/nip.html", form = nip_form, mensaje = mensaje, intentos=respuesta['intentos'])


@app.route('/retiro_deposito', methods = ['POST'])
def retiro():
    cl = ClienteServicio()
    pago_form = Pago()
    cantidad = float(request.form['pago'])
    print('Vista retiro/ cantidad -> ', cantidad)
    mensaje = ""
    if request.method == 'POST':
        if 'num' in session:
            print("Entro a sesion")
            num = session['num']
            saldo = cl.verifica_saldo(num)
            limite = cl.verifica_limite(num)
            print("saldo222222",saldo)
            print("limite222222",limite)
            if cantidad <= 0:
                mensaje = "La cantidad debe ser mayor a cero 😒"
                print("Entrooo1111")
            if pago_form.validate_on_submit():
                print("entroaaaaaa ",cantidad)
                respuesta = cl.realiza_retiro(num, cantidad)
                saldo = cl.verifica_saldo(num)
                print("Respuestaaaaaaaaa ", respuesta)
                return render_template("formularios/cliente.html", form= pago_form, saldo = saldo['saldo'], limite = limite['limite'], mensaje = mensaje, nombre=saldo['nombre'])
            else:
                redirect(url_for("formNip"))
    return render_template("formularios/cliente.html", form= pago_form, saldo = saldo, limite = limite, mensaje = mensaje)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
