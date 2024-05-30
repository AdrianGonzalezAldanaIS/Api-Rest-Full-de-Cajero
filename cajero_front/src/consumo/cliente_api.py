from flask import Flask, jsonify, render_template, url_for, session, request, redirect, Blueprint
import json
from .cliente_servicio import ClienteServicio
from formularios.tarjeta_forms import TarjetaForm, Nip, Pago

main = Blueprint('cliente_cajero', __name__)

"""app = Flask(__name__)
app.secret_key = "2451456769873"
"""
@main.route('/')
def index():
    form = TarjetaForm()
    return render_template("formularios/ingresar.html", form = form)

@main.route('/tarjeta', methods=['POST'])
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
                return redirect(url_for('cliente_cajero.formNip'))
            else:
                mensaje = respuesta['mensaje']
                return render_template("formularios/ingresar.html", form = trajeta_form, mensaje = mensaje)
    return jsonify({"respuesta":num})

@main.route('/Nip/', methods = ['GET'])
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

@main.route('/Cuenta', methods = ['POST'])
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
                return redirect(url_for("cliente_cajero.index"))
    return render_template("formularios/nip.html", form = nip_form, mensaje = mensaje, intentos=respuesta['intentos'])


@main.route('/retiro_deposito', methods = ['POST'])
def retiro():
    cl = ClienteServicio()
    pago_form = Pago()
    cantidad = float(request.form['pago'])
    mensaje = ""
    if request.method == 'POST':
        if 'num' in session:  
            num = session['num']
            saldo = cl.verifica_saldo(num)
            limite = cl.verifica_limite(num)
            if cantidad <= 0:
                mensaje = "La cantidad debe ser mayor a cero 😒"
            if pago_form.validate_on_submit():
                if pago_form.submit_retirar.data:
                    respuesta = cl.realiza_retiro(num, cantidad)
                    saldo = cl.verifica_saldo(num)
                    return render_template("formularios/cliente.html", form= pago_form, saldo = saldo['saldo'], limite = limite['limite'], mensaje = mensaje, nombre=saldo['nombre'])
                elif pago_form.submit_depositar.data:
                    print("ENtro a depositar")
                    respuesta = cl.realizar_deposito(num, cantidad)
                    saldo = cl.verifica_saldo(num)
                    print("Saldo actual ",saldo['saldo'])
                    return render_template("formularios/cliente.html", form= pago_form, saldo = saldo['saldo'], limite = limite['limite'], mensaje = mensaje, nombre=saldo['nombre'])
            else:
                redirect(url_for("cliente_cajero.formNip"))
    return render_template("formularios/cliente.html", form= pago_form, saldo = saldo, limite = limite, mensaje = mensaje)

"""
if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""