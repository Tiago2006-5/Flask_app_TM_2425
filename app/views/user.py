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

@user_bp.route('/modifier-enfant/<int:Id_personne>', methods=('GET', 'POST'))
@login_required
def modifier_enfant(Id_personne):
    
    db = get_db()
    enfant = db.execute('SELECT * FROM Enfants WHERE Id_personne = ?',(Id_personne,)).fetchone()
    personne = db.execute('SELECT * FROM Personne WHERE Id_personne = ?',(Id_personne,)).fetchone()
    
    close_db()
    if request.method == 'POST':

        nom = request.form['nom']
        prenom = request.form['prenom']
        date = request.form['date-de-naissance']
        sexe = request.form['sexe']
        assurance = request.form['assurance']
        nr_assure = request.form['assure']
        info_cardiaque = request.form.get('cardiaque-info',"")
        info_respiratoire = request.form.get('respiratoire-info',"")
        info_medicament = request.form.get('medicament-info',"")
        info_alimentaire = request.form.get('alimentaire-info',"")


        # On récupère la base de donnée
        db = get_db()

        # Si le nom d'utilisateur et le mot de passe ont bien une valeur
        # on essaie d'insérer l'utilisateur dans la base de données
        if nom and prenom and date and assurance and nr_assure and sexe:
            
            try:

                curseur = db.cursor()
                    
                curseur.execute("UPDATE Personne SET Nom = ?, Prenom = ?, Date_de_naissance = ?, Sexe = ?, Rôle = ? WHERE Id_personne = ?",
                       (nom, prenom, date, sexe, "enfant", Id_personne))

                db.commit()

                last_personne_id = curseur.lastrowid

                curseur.execute("UPDATE Enfants SET Assurance = ?, Numéro_assuré = ?, Régime_alimentaire = ?, Problème_respiratoire = ?, Problème_cardiaque = ?, Médicament = ? WHERE Id_personne = ?",
                       (assurance, nr_assure, info_alimentaire, info_respiratoire, info_cardiaque, info_medicament, Id_personne))
                
                # db.commit() permet de valider une modification de la base de données
                db.commit()
                # On ferme la connexion à la base de données pour éviter les fuites de mémoire
                close_db()
            
                return render_template('user/profile.html')
            
            except Exception as e:
                flash(f'Erreur lors de l\'inscription: {str(e)}')
                return render_template('user/modification.html', enfant = enfant, personne = personne)

        else:
            flash('Veuillez remplir tous les champs obligatoires.')
            return render_template('user/modification.html', enfant = enfant, personne = personne)
        
    else:
        return render_template('user/modification.html', enfant = enfant, personne = personne)