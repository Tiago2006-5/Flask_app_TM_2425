from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

# Routes /...
home_bp = Blueprint('home', __name__)



# Route /
@home_bp.route('/', methods=('GET', 'POST'))
def landing_page():
    # Affichage de la page principale de l'application
    return render_template('home/index.html')

# Gestionnaire d'erreur 404 pour toutes les routes inconnues
@home_bp.route('/<path:text>', methods=['GET', 'POST'])
def not_found_error(text):
    return render_template('home/404.html'), 404

@home_bp.route('/remerciements/<int:nombre>', methods=('GET', 'POST'))
def merci(nombre):
    return render_template('home/remerciements.html', nombre = nombre)

@home_bp.route('/inscrit/<string:nom>', methods=('GET', 'POST'))
def inscrit(nom):
    return render_template('home/inscrit.html', nom = nom)

@home_bp.route('/max_enfant', methods=('GET', 'POST'))
def max_enfant():
    return render_template('home/max_enfant.html')
