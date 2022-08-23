from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import User, domo_cliente, domo_reserva, domo_restaurante
from flask import render_template, request, url_for, redirect, session
from sqlalchemy import func

db = models.db

#### Caso de Uso 2 - Ernesto Opazo ####

@app.route('/valorar/<id_rsv>', methods=['GET','POST'])
def add_valoracion(id_rsv):
    
    return render_template("valorar/valorar.html")

def update_valoracion():
    
    
    
    pass

def delete_valoracion():
    pass

def view_valoraciones():
    pass

#### Fin de Caso de uso ###