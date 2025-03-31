from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.utils import *
from app.db.db import get_db, close_db
import os


# Routes /user/...
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/admin', methods=('GET', 'POST'))
@admin_required
def show_admin():
    # Affichage de la page principale de l'application
    return render_template('admin/admin.html')


@admin_bp.route('/publish', methods=('GET', 'POST'))
@admin_required
def publish():

    if request.method == 'POST':

        print("Salut")

        lieu = request.form['Lieu']
        adresse = request.form['Adresse']
        date = request.form['Date']
        prix = request.form['Prix']

        start = adresse.find('src="') + 5
        end = adresse.find('"', start)
        url = adresse[start:end]

        


        db = get_db()


        if lieu and url and date and prix:
            try:
                curseur = db.cursor()

                curseur.execute("INSERT INTO Camps (Lieu, Date_, Prix, Adresse) VALUES (?, ?, ?, ?)", (lieu, date, prix, url))

                db.commit()
              
                close_db()

            except db.IntegrityError:

                error = "Error"
                flash(error)
                return redirect(url_for("admin.publish"))
            return redirect(url_for("camp.camps"))
        else:
            error = "error"
            flash(error)
            return redirect(url_for("admin/publish"))

    else:
        return render_template('admin/publish.html')
    
@admin_bp.route('/modifier/<int:Id_camp>', methods=('GET', 'POST'))
@admin_required
def modifier(Id_camp):
    db = get_db()
    camp = db.execute('SELECT * FROM Camps WHERE Id_camp = ?',(Id_camp,)).fetchone()
    close_db()
    if request.method == 'POST':

        lieu = request.form['Lieu']
        adresse = request.form['Adresse']
        date = request.form['Date']
        prix = request.form['Prix']
        if adresse[0:5] != "https":
            start = adresse.find('src="') + 5
            end = adresse.find('"', start)
            url = adresse[start:end]
        else:
            url = adresse
        db = get_db()

        if lieu and url and date and prix:
            try:
                curseur = db.cursor()
                    
                curseur.execute("UPDATE Camps SET Lieu = ?, Date_ = ?, Prix = ?, Adresse = ? WHERE Id_camp = ?",
                       (lieu, date, prix, url, Id_camp))

                db.commit()

                close_db()
                return redirect(url_for("camp.camps"))
            except Exception as e:
                flash(f'Erreur lors de la modification: {str(e)}')
                return redirect(url_for("admin.modifier", Id_camp = Id_camp))
        else:
            error = "error"
            flash(error)
            return redirect(url_for("admin/modifier", Id_camp = Id_camp))
    else:
        return render_template('admin/modifier.html', camp = camp)
    
@admin_bp.route('/supprimer/<int:Id_camp>', methods=('POST',))
@admin_required
def supprimer(Id_camp):
    db = get_db()
    db.execute("DELETE FROM Camps WHERE Id_camp = ?", (Id_camp,))
    db.commit()
    close_db()
    
    return redirect(url_for("camp.camps"))