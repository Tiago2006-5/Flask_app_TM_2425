from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.utils import *

# Routes /user/...
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/admin', methods=('GET', 'POST'))
@login_required 
def show_admin():
    # Affichage de la page principale de l'application
    return render_template('admin/admin.html')