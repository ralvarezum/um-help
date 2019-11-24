from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Persona, Automovil

@app.route('/automovil/')
def automovil():
    automoviles = Automovil.get_all()
    return render_template("automovil/index.html",
                           automoviles=automoviles,
                           titulo='automoviles')

@app.route("/automovil/crear", methods=["GET"])
def auto_crear():
    personas = Persona.get_all()
    return render_template("automovil/crear.html",
                           personas=personas,
                           titulo='Crear nuevo')

@app.route("/automovil/crear", methods=["POST"])
def auto_agregar():
    if request.method == 'POST':
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        personas = request.form.getlist('personas')
    if modelo and marca:
        auto = Automovil(marca=marca, modelo=modelo,
                        creado=dt.now(), activo=True)
        auto.save()
        for persona_id in personas:
            persona = Persona.find_by_id(persona_id)
            persona.automoviles.append(auto)
            persona.update()

    return redirect(url_for('automovil'))
