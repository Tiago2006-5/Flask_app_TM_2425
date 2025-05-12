from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask import current_app
from app.db.db import get_db, close_db
from flask_mail import Message
from flask import Flask
from flask_mail import Mail

mail = Mail()

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

@home_bp.route('/remerciements/<int:nombre>/<string:prenoms>', methods=('GET', 'POST'))
def merci(nombre,prenoms):
    #if nombre > 1:
     #   liste_prenoms = prenoms.split(",")
    #else:
     #   liste_prenoms = [prenoms]

    #def format_noms(liste_prenoms):
     #   if len(liste_prenoms) == 1:
      #      return liste_prenoms[0]
       # elif len(liste_prenoms) == 2:
        #    return f"{liste_prenoms[0]} et {liste_prenoms[1]}"
        #else:
         #   return f"{', '.join(liste_prenoms[:-1])} et {liste_prenoms[-1]}"
    
    #db = get_db()
    #destinataire = db.execute("SELECT Email FROM Parents WHERE Id_parent = ?", (g.user['Id_parent'],)).fetchone()[0]
    #close_db() 
    #sujet = "Confirmation d'inscription"
    #corps = f"""Merci pour l'inscription de {format_noms(liste_prenoms)}.\n\n
#Starkids se réjouit de vous voir sur le terrain et de partager ensemble de super moments pendant le camp !\n\n

#À bientôt,\n
#L'équipe Starkids.
#"""
 #   msg = Message(subject=sujet,
  #                sender=current_app.config['EMAIL_ADDRESS'],
   #               recipients=[destinataire],
    #              body=corps)  
    #mail.send(msg)
    return render_template('home/remerciements.html', nombre = nombre)

@home_bp.route('/inscrit/<string:nom>', methods=('GET', 'POST'))
def inscrit(nom):
    return render_template('home/inscrit.html', nom = nom)

@home_bp.route('/max_enfant', methods=('GET', 'POST'))
def max_enfant():
    return render_template('home/max_enfant.html')
