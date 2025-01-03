from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.utils import *
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
import os

# Routes /user/...
user_bp = Blueprint('user', __name__, url_prefix='/user')

# Route /user/profile accessible uniquement à un utilisateur connecté grâce au décorateur @login_required
@user_bp.route('/profile', methods=('GET', 'POST'))
@login_required 
def show_profile():
    personnes = []
    db = get_db()
    enfants = db.execute('SELECT * FROM Enfants WHERE Id_parent = ?',(g.user['Id_parent'],)).fetchall()
    for enfant in enfants:
        personnes.append(dict(db.execute('SELECT * FROM Personne WHERE Id_personne = ?',(enfant['Id_personne'],)).fetchone()))
    close_db()
 
    




    # Affichage de la page principale de l'application
    return render_template('user/profile.html', enfants = enfants, personnes = personnes)


