import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

# Ce décorateur est utilisé dans l'application Flask pour protéger certaines vues (routes)
# afin de s'assurer qu'un utilisateur est connecté avant d'accéder à une route 

def login_required(view):
    
    @functools.wraps(view)
    def wrapped_view(**kwargs):
    
        # Si l'utilisateur n'est pas connecté, il ne peut pas accéder à la route, il faut le rediriger vers la route auth.login
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view

def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        print("Vérification de l'accès admin...")
        # Vérifie si l'utilisateur est connecté
        if g.user is None or g.role is None:
            print("Utilisateur non connecté, redirection vers login")

            return redirect(url_for('auth.login'))

        # Vérifie si l'utilisateur a le rôle "admin"
        if g.role['Rôle'] != "admin":
                flash("Vous n'avez pas les droits d'administrateur.", "danger")
                return redirect(url_for('home.landing_page'))  # Redirige vers une page autorisée
            
        print("Accès autorisé")
        return view(**kwargs)

    return wrapped_view