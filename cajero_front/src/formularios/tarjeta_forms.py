from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

"""
Clases que que utilizan los archivos HTML para sus input en 
los formularios: ingresar.html, nip.html y cliente.html
"""

class TarjetaForm(FlaskForm):
    num_tarjeta = StringField("Número de tarjeta", validators=[
        DataRequired(),
        Length(min=4, max=4, message='No cumple con el formato: ####')])
    
    submit = SubmitField('Enviar')

class Nip(FlaskForm):
    num_nip = PasswordField("Número de nip ", validators=[
        DataRequired(),
        Length(min=4, max=4, message='No cumple con el formato: ####')])
    submit = SubmitField('Enviar')

class Pago(FlaskForm):
    pago = FloatField("Ingresa el monto a retirar/depositar", validators=[
        DataRequired()
    ])
    submit_retirar = SubmitField('Retirar')
    submit_depositar = SubmitField('Depositar')
