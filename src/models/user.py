from src.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from src.extensions import login_manager


class User(db.Model):
    __tablename__: str = 'users'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(20))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
