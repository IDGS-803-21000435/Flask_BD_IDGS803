from flask import Flask, render_template, request, flash, Response, redirect
from flask_wtf.csrf import CSRFProtect
import forms
from flask import g

from models import db
from models import Alumnos

app = Flask(__name__)
app.secret_key = 'clave_secreta'

csrf = CSRFProtect()


@app.route("/index", methods=["GET","POST"])
def index():
    alum_form = forms.UserForm2(request.form)
    if request.method == 'POST':#and alum_form.validate()
         alum = Alumnos(
             nombre = alum_form.nombre.data,
             apaterno = alum_form.apaterno.data,
             email = alum_form.email.data
         )
         db.session.add(alum)
         db.session.comit()
         
    
    return render_template("index.html")


@app.route("/ABC_Completo", methods=["GET","POST"])
def ABC_Completo():
    alumno = Alumnos.query.all()
    
    return render_template("ABC_Completo.html", alumno = alumno)


@app.route("/alumnos", methods=["GET","POST"])
def alumno():
    g.nombre = 'Daniel'
    print('dentro alumnos')
    nom = ''
    apa = ''
    ama = ''
    correo = ''
    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print(f'hola: {g.nombre}')
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        correo = alum_form.correo.data
        mensaje = f'Bienvenido {nom}'
        flash(mensaje)
        print("nombre: {x}, apaterno: {y}, amaterno: {t}, correo: {w}".format(x = nom, y = apa, t = ama, w = correo))
        
    
    return render_template("alumnos.html", form = alum_form )

# realizado 20/02/2024 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre = 'Daniel'
    print('before_request')
    
    
@app.after_request
def after_request(response):
    print('ultimo')
    if 'Daniel' not in g.nombre and request.endpoint not in['/index']:
        return redirect('index.html')
    return response
    
# ------------------------------------------------------------
if __name__ =="__main__":
    csrf, init_app(app)  #se utiliza debug = True para ctivar "actualizaciones en caliente" similar liveServer
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
#   para tumbar el servidor es con el comando ctrl + c
#   para activarlo se ejecuta el archivo, escribir en la terminal "py nombre.py"
#   nombre, correo, Telefono, Direccion, Sueldo
