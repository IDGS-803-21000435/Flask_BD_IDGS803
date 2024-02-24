from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators


class UserForm(Form):
    nombre = StringField('nombre',[
        validators.DataRequired(message='elcampo es requerido'),
        validators.length(min=4, max=10, message='ingresa nombre valido')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='elcampo es requerido'),
        validators.length(min=4, max=10, message='ingresa un apellido valido')
    ])
    amaterno = StringField('amaterno', [
        validators.DataRequired(message='elcampo es requerido'),
        validators.length(min=4, max=10, message='ingresa un apellido valido')
    ])
    edad = IntegerField('edad', [
        validators.number_range(min=1, max=20, message='valor no valido')
    ])
    correo = EmailField('correo', [
        validators.Email(message='Ingrese un correo valido'),
    ])
    
