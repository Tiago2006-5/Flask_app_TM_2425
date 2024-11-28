from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
import os

camps_bp = Blueprint('camp', __name__, url_prefix = '/camps')

@camps_bp.route('/camps')
def camps():
    db = get_db()

    cursor = db.execute('Select * From Camps')
    g.camps = cursor.fetchall()
    close_db()
    return render_template('camps/camp.html')