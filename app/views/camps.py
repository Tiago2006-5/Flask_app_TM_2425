from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
from app.utils import *
import os

camps_bp = Blueprint('camp', __name__, url_prefix = '/camps')

@camps_bp.route('/camps')
def camps():
    db = get_db()

    cursor = db.execute('Select * From Camps')
    g.camps = cursor.fetchall()
    number = []
    for camp in g.camps:
        nb = db.execute("Select Count(*) From Inscriptions Where Id_camp = ?", (camp['Id_camp'],)).fetchone()[0]
        number.append([camp['Id_camp'], nb])
    close_db()
    g.nb = {id_camp: nb for id_camp, nb in number}
    return render_template('camps/camp.html')

@camps_bp.route('/participer/<int:Id_parent>/<int:Id_camp>', methods=('GET', 'POST'))
@login_required
def participer(Id_parent, Id_camp):
        if request.method == 'POST':
            enfants_coches = request.form.getlist('enfant')
            number = len(enfants_coches)
            if number == 0:
                flash("Vous n'avez pas sélectionné d'enfant")
                return redirect(url_for('camp.participer', Id_parent = Id_parent, Id_camp = Id_camp))
            else:
                db = get_db()
                prenoms = ""
                for enfant in enfants_coches:
                    kid = db.execute('SELECT * FROM Inscriptions WHERE Id_enfant = ? AND Id_camp = ?',(enfant, Id_camp)).fetchone()
                    if kid is None:
                        db.execute('INSERT INTO Inscriptions (Id_enfant, Id_camp) VALUES (?, ?)',(enfant, Id_camp))
                        enfant_info = db.execute('SELECT * FROM Personne WHERE Id_personne = ?',(enfant,)).fetchone()
                        prenoms += enfant_info['Prenom'] + ","

                        db.commit()
                close_db()
                print(prenoms)
                if prenoms == "":
                    flash("Vous avez déjà inscrit cet enfant")
                    return redirect(url_for('camp.participer', Id_parent = Id_parent, Id_camp = Id_camp))
                else:
                    return redirect(url_for('home.merci',nombre = number, prenoms = prenoms[:-1]))

        else:
            db = get_db()
            enfants = db.execute('SELECT * FROM Enfants WHERE Id_parent = ?',(Id_parent,)).fetchall()
            if not enfants:
                return redirect(url_for('user.show_profile'))
            enfants_infos = {}
            for enfant in enfants:
                enfant_info = db.execute('SELECT * FROM Personne WHERE Id_personne = ?',(enfant['Id_personne'],)).fetchone()
                if enfant_info:
                    enfants_infos[enfant['Id_personne']] = dict(enfant_info)
            camp = db.execute('Select * From Camps Where Id_camp = ?',(Id_camp,),).fetchone()

            nb_participants = {}
            for row in db.execute("SELECT Id_camp, COUNT(*) FROM Inscriptions GROUP BY Id_camp"):
                nb_participants[row['Id_camp']] = row[1]

            close_db()
            print(enfants_infos)
            return render_template('camps/participer.html', camp = camp, enfants = enfants, enfants_infos = enfants_infos, nb = nb_participants)



    