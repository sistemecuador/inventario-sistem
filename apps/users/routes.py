from flask import request, redirect, url_for, render_template, flash
from flask_login import login_required

from apps.users import users
from apps.users.forms import UserForm
from apps.users.models import User


@users.route('/list', methods=['GET', 'POST'])
@login_required
def list_usuarios():
    query = User.query.filter_by(is_active=True)
    return render_template('usurios/list.html', usuarios=query)


@users.route("/add", methods=['GET', 'POST'])
@login_required
def crear_usuarios():
    form = UserForm()
    card_title = 'Registro de usuarios'
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                print("form.data", form.data)
                first_name = form.first_name.data
                last_name = form.last_name.data
                username = form.username.data
                password = form.password.data
                correo = form.correo.data
                is_admin = form.is_admin.data
                is_super = form.is_superuser.data
                is_active = form.is_active.data
                user = User(first_name=first_name, last_name=last_name, username=username, password=password,
                            correo=correo, is_superuser=is_super, is_admin=is_admin, is_active=is_active)
                user.password = User.set_password(password)
                user.save()
                return redirect(url_for("home.dashboard"))
            except Exception as e:
                print("Error", str(e))
        else:
            print(form.errors)
    return render_template('usurios/add.html', form=form, card_title=card_title)


@users.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_usuarios(id):
    user = User.query.get_or_404(id)
    form = UserForm(obj=user)
    card_title = 'Edición de usuarios'
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                password = form.password.data
                obj_password = user.password
                # if password != obj_password:
                #     if not User.check_password(obj_password, password):
                #         pass
                form.populate_obj(user)
                user.save()
                return redirect(url_for('users.list_usuarios'))
            except Exception as e:
                print("Error", str(e))
        else:
            print(form.errors)
    return render_template("usurios/add.html", form=form, card_title=card_title)


@users.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete_usuarios(id):
    user = User.query.get_or_404(id)
    context = {'title_card': 'Elimininacion de usuarios',
               'message': 'Al eliminar el usuario, se eliminaran todos los regisros que depende del mismo.',
               "redirect": url_for('users.list_usuarios')}
    if request.method == 'POST':
        action = request.form.get("action", None)
        if action == 'delete':
            user.is_active = False
            user.save()
            return redirect(url_for('users.list_usuarios'))
    return render_template('usurios/delete.html', context=context)
