from flask import render_template
from apps.home import home
from flask_login import login_required

@home.route("/home")
def inicio():
    contexto = {
        'usuarios': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
    return render_template('home/index.html', context=contexto, title='Home')


@home.route("/dashboard")
@login_required
def dashboard():
    contexto = {'message': 'Hola desde dashboard'}
    # contexto = {}
    return render_template('home/dashboard.html', context=contexto, title='dashboard')
