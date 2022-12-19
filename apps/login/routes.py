from flask import redirect, url_for, request, flash, render_template
from flask_login import current_user, login_user, logout_user
from apps.login import login as lg
from apps.login.forms import LoginForm
from apps.login.forms import RegistroForm
from apps.users.models import User


@lg.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home.dashboard"))
    method = request.method
    form = LoginForm()
    if method == 'POST':
        if form.validate_on_submit():
            username = request.form.get("username", None)
            password = request.form.get("password", None)
            remember_me = request.form.get("remember_me", None)
            user = User.query.filter_by(username=username).first()  # Si es qeu no existe devulve None
            if user:
                if user.is_active:
                    if user.check_password(user.password, password):
                        login_user(user=user, remember=remember_me)
                        return redirect(url_for("home.dashboard"))
                    else:
                        flash("Las clave es incorrecta", category='warning')
                else:
                    flash("El usuario esta desactivado,contactese con el administrador del sistema", category='warning')
            else:
                flash("El usuario no existe", category='danger')
        else:
            print(form.errors)
    return render_template("login.html", form=form)


@lg.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login.login'))


@lg.route('/registro', methods=['GET', 'POST'])
def registro():
    method = request.method
    form = RegistroForm()
    if method == 'POST':
        try:
            if form.validate_on_submit():
                print(form.data)
                username = form.username.data
                password = form.password.data
                first_name = form.first_name.data
                last_name = form.last_name.data
                email = request.form.get("email")
                try:
                    query = User.query.filter_by(username=username).first()
                    if not query:
                        user = User(username=username, password=password, first_name=first_name, last_name=last_name,
                                    correo=email)
                        user.password = User.set_password(password)
                        user.save()
                        return redirect(url_for("login.login"))
                    else:
                        flash("El usuario ingresado ya existe")

                except Exception as e:
                    print("Error ", str(e))
                    flash(str(e))
            else:
                print("errores", form.errors)
        except Exception as e:
            print("Error", str(e))
    return render_template("registro/registro.html", form=form)
