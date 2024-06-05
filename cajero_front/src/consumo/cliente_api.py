from flask import Flask, jsonify, render_template, url_for, session, request, redirect, Blueprint, make_response
import json
from .cliente_servicio import ClienteServicio
from formularios.tarjeta_forms import TarjetaForm, Nip, Pago

main = Blueprint('cliente_cajero', __name__)


@main.route('/')
def index():
    form = TarjetaForm()
    return render_template("formularios/ingresar.html", form = form)

@main.route('/tarjeta', methods=['GET', 'POST'])
def validar_tarjeta():
    num = None
    trajeta_form = TarjetaForm()
    if request.method == 'POST':
        cl = ClienteServicio()
        mensaje = ""
        num = request.form['num_tarjeta']
        session['num'] = num
        respuesta = cl.valida_terjeta(num)
        if respuesta['verificada']:
                return redirect(url_for('cliente_cajero.formNip'))
        else:
            mensaje = respuesta['mensaje']
            return make_response(render_template("formularios/ingresar.html", form = trajeta_form, mensaje = mensaje,respuesta=num)),404
            
    return jsonify({"respuesta":num})

@main.route('/nip', methods = ['GET'])
def formNip():
    nip_form = Nip()
    intentos = 0
    mensaje = ""
    if 'intentos' in session and 'mensaje'in session:
        intentos = session['intentos']
        intentos = 0
    return render_template("formularios/nip.html", form = nip_form, mensaje = mensaje, intentos = intentos)

@main.route('/cuenta', methods = ['POST'])
def getNip():
    nip_form = Nip()
    cl = ClienteServicio()
    pago_form = Pago()
    respuesta = None
    if request.method == 'POST':        
        mensaje = ""
        mensaje_retiro= ""
        if 'num' in session:
            num = session['num']
            num_nip = request.form['num_nip']
            respuesta = cl.validate_nip(num, num_nip)
            saldo = cl.verifica_saldo(num)
            limite = cl.verifica_limite(num)
            if respuesta['verificada']:
                
                return render_template("formularios/cliente.html", form= pago_form,nombre=saldo['nombre'], saldo = saldo['saldo'], limite = limite['limite'], mensaje = mensaje_retiro) # type: ignore
            else:
                if respuesta['intentos'] > 3:
                    return redirect(url_for("cliente_cajero.index"))
                session['intentos'] = respuesta['intentos']
                mensaje = respuesta['mensaje']
                return render_template("formularios/nip.html", form = nip_form, mensaje = mensaje, intentos=None), 404
        else:
            return redirect(url_for("cliente_cajero.index"))
            
    return render_template("formularios/nip.html", form = nip_form, mensaje = mensaje, intentos=None) # type: ignore


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
            if cantidad <= 1:
                mensaje = "La cantidad debe ser mayor a cero 😒"
            if request.form.get('submit_retirar') == 'Retirar':
                cl.realiza_retiro(num, cantidad)
                saldo = cl.verifica_saldo(num)
                return render_template("formularios/cliente.html", form= pago_form, saldo = saldo['saldo'], limite = limite['limite'], mensaje = mensaje, nombre=saldo['nombre'])
            elif request.form.get('submit_depositar') =='Depositar':
                cl.realizar_deposito(num, cantidad)
                saldo = cl.verifica_saldo(num)
                return render_template("formularios/cliente.html", form= pago_form, saldo = saldo['saldo'], limite = limite['limite'], mensaje = mensaje, nombre=saldo['nombre'])
    return render_template("formularios/cliente.html", form= pago_form, saldo = saldo, limite = limite, mensaje = mensaje)



