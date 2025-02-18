from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
import os

info_bp = Blueprint('info', __name__)

@info_bp.route('/informations')
def informations():
    return render_template('informations/info.html')