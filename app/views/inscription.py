from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
from app.utils import *
import os

inscr_bp = Blueprint('inscr', __name__)

@inscr_bp.route('/enfant',   methods=('GET', 'POST'))
@login_required
def enfant():
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
        number = db.execute("SELECT COUNT(*) FROM Enfants WHERE Id_parent = ?", (g.user['Id_parent'],)).fetchone()[0]
        
        if number >= 12:
            flash('Vous avez atteint le nombre maximum d\'enfants inscrits.')
            return render_template('home/max_enfant.html')
        else:

            # Si le nom d'utilisateur et le mot de passe ont bien une valeur
            # on essaie d'insérer l'utilisateur dans la base de données
            if nom and prenom and date and assurance and nr_assure and sexe:
                
                try:

                    curseur = db.cursor()
                    # Utiliser une transaction pour regrouper les opérations
                    with db:
                        curseur.execute("INSERT INTO Personne (Nom, Prenom, Date_de_naissance, Sexe, Rôle) VALUES (?, ?, ?, ?, ?)", (nom, prenom, date, sexe, "enfant"))
                        last_personne_id = curseur.lastrowid
                        curseur.execute("INSERT INTO Enfants (Assurance, Numéro_assuré, Régime_alimentaire, Problème_respiratoire, Problème_cardiaque, Médicament, Id_parent, Id_personne) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (assurance, nr_assure, info_alimentaire, info_respiratoire, info_cardiaque, info_medicament, g.user['Id_parent'], last_personne_id))

                    # On ferme la connexion à la base de données pour éviter les fuites de mémoire
                    close_db()
                
                    return render_template('home/inscrit.html', nom = prenom)
                
                except Exception as e:
                    flash(f'Erreur lors de l\'inscription: {str(e)}')
                    return render_template('user/inscription.html')

            else:
                flash('Veuillez remplir tous les champs obligatoires.')
                return render_template('user/inscription.html')
        
    else:
        return render_template('user/inscription.html')