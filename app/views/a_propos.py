from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
import os

a_propos_bp = Blueprint('a_propos', __name__)

@a_propos_bp.route('/a_propos')
def propos():
    return render_template('a_propos/propos.html')