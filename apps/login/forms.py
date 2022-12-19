from flask_wtf import FlaskForm
import wtforms
import wtforms.validators as vt


class LoginForm(FlaskForm):
    username = wtforms.StringField(label='Username',
                                   validators=[
                                       vt.Length(min=4, max=12, message='El campo debe estar entre 4 y 12 caracterres'),
                                       vt.DataRequired(message="Dato es requerido")
                                   ], render_kw={'placeholder': 'Ingrese su userame', 'class': 'form-control'})
    password = wtforms.PasswordField(label='Password',
                                     validators=[vt.DataRequired(message='Dato requerido'), vt.Length(min=4, max=20)],
                                     render_kw={'placeholder': 'Ingrese su password', 'class': 'form-control'})

    remember_me = wtforms.BooleanField(label='Remember Me', default=True)

    enviar = wtforms.SubmitField("Enviar", render_kw={'class': 'btn btn-primary btn-block'})


class RegistroForm(FlaskForm):
    first_name = wtforms.StringField(label="Nombres", validators=[vt.Length(max=100, min=1), vt.DataRequired()],
                                     render_kw={'placeholder': 'Ingrese sus nombres', 'class': 'form-control'})
    last_name = wtforms.StringField(label="Apellidos", validators=[vt.Length(max=100, min=1), vt.DataRequired()],
                                    render_kw={'placeholder': 'Ingrese sus apellidos', 'class': 'form-control'})

    username = wtforms.StringField(label="Username", validators=[vt.Length(max=20, min=4), vt.DataRequired()],
                                   render_kw={'placeholder': 'Ingrese su username', 'class': 'form-control'})

    password = wtforms.PasswordField(label="Password",
                                     validators=[vt.Length(max=30, min=4), vt.DataRequired()],
                                     render_kw={'placeholder': 'Ingrese su password', 'class': 'form-control'})

    email = wtforms.EmailField(label="Correo electronico",
                               validators=[vt.Email(message="Correo no cumple con el formato requerido")],
                               render_kw={'placeholder': 'Ingrese su correo', 'class': 'form-control'})

    register = wtforms.SubmitField('Registrarse', render_kw={'class': 'btn btn-primary btn-block'})

    def validate_password(self, field):
        print("data", field.data)
        password = field.data
        if '123' in password:
            raise vt.ValidationError("La clave no puede contener 123")
