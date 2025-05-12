import os
from flask_bootstrap import Bootstrap5
from flask import Flask
from app.utils import *

# Importation des blueprints de l'application
# Chaque blueprint contient des routes pour l'application
from app.views.home import home_bp
from app.views.auth import auth_bp
from app.views.user import user_bp
from app.views.camps import camps_bp
from app.views.informations import info_bp
from app.views.a_propos import a_propos_bp
from app.views.admin import admin_bp
from app.views.inscription import inscr_bp
from app.config import Config
from flask import Flask
from flask_mail import Mail

mail = Mail()

# Fonction automatiquement appelée par le framework Flask lors de l'exécution de la commande python -m flask run permettant de lancer le projet
# La fonction retourne une instance de l'application créée
def create_app():

    # Crée l'application Flask
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    mail.init_app(app)


    bootstrap = Bootstrap5(app)

    # Chargement des variables de configuration stockées dans le fichier config.py
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), "config.py"))
    app.config.from_object(Config)
    # Enreigstrement des blueprints de l'application.
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(camps_bp)
    app.register_blueprint(info_bp)
    app.register_blueprint(a_propos_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(inscr_bp)

    # On retourne l'instance de l'application Flask
    return app