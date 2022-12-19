import wtforms
from flask_wtf import FlaskForm
from wtforms import validators as vt
from wtforms.widgets import PasswordInput


class UserForm(FlaskForm):
    first_name = wtforms.StringField(label="Nombres", validators=[vt.Length(max=100, min=1), vt.DataRequired()],
                                     render_kw={'placeholder': 'Ingrese sus nombres', 'class': 'form-control'})
    last_name = wtforms.StringField(label="Apellidos", validators=[vt.Length(max=100, min=1), vt.DataRequired()],
                                    render_kw={'placeholder': 'Ingrese sus apellidos', 'class': 'form-control'})

    username = wtforms.StringField(label="Username", validators=[vt.Length(max=20, min=4), vt.DataRequired()],
                                   render_kw={'placeholder': 'Ingrese su username', 'class': 'form-control'})

    password = wtforms.PasswordField(label="Password",
                                     validators=[vt.Length(max=256, min=4)],
                                     render_kw={'placeholder': 'Ingrese su password', 'class': 'form-control'},
                                     widget=PasswordInput(hide_value=False))

    correo = wtforms.EmailField(label="Correo electronico",
                                validators=[vt.Email(message="Correo no cumple con el formato requerido")],
                                render_kw={'placeholder': 'Ingrese su correo', 'class': 'form-control'})

    is_admin = wtforms.BooleanField(default=False)
    is_superuser = wtforms.BooleanField(default=False)
    is_active = wtforms.BooleanField(default=True)
    #
    # def validate_password(self, field):
    #     pw = field.data
    #     if len(pw) == 0:
    #         raise vt.ValidationError("El campo no puede estar vacio")
