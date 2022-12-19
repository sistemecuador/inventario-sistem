from flask_login import LoginManager
from flask_migrate import Migrate

from apps.users.models import User
from config.app import create_app
from config.db import db

app = create_app()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.login_message = "Debes iniciar sesion"
migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run()
