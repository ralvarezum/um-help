from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Persona, Automovil

@app.route('/persona/')
def pers():
    #personas = Persona.query.all()
    personas = Persona.get_all()
    return render_template("persona/index.html",
                           personas=personas,
                           titulo='personas')


@app.route("/persona/crear", methods=["GET"])
def pers_crear():
    print('request.args')
    print(request.args)
    print('request.base_url')
    print(request.base_url)
    print('request.data')
    print(request.data)
    print('request.form')
    print(request.form)
    print('request.get_json()')
    print(request.get_json())
    print('request.get_data()')
    print(request.get_data())
    print('request.full_path')
    print(request.full_path)
    print('request.headers')
    print(request.headers)
    print('request.method')
    print(request.method)
    print('request.query_string')
    print(request.query_string)
    print('request.referrer')
    print(request.referrer)
    print('request.user_agent')
    print(request.user_agent)
    return render_template("persona/crear.html")

@app.route("/persona/crear", methods=["POST"])
def pers_agregar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
    if nombre and apellido:
        pers1 = Persona(nombre=nombre, apellido=apellido,
                        creado=dt.now(), activo=True)
        db.session.add(pers1)
        db.session.commit()
    return redirect(url_for('pers'))

@app.route("/persona/crear", methods=["POST"])
def pers_agregar_post():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
    if nombre and apellido:
        pers1 = Persona(nombre=nombre, apellido=apellido,
                        creado=dt.now(), activo=True)
        db.session.add(pers1)
        db.session.commit()
    return redirect(url_for('pers'))

@app.route("/persona/detalle", methods=['GET'])
def pers_detalles():
    persona_id = int(request.args['id'])
    persona = Persona.find_by_id(persona_id)
    return render_template("persona/detalle.html", persona=persona)
