from ..utils.db_connect import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    UID                 = db.Column(db.String(20), primary_key=True)
    password_hash       = db.Column('password', db.String(128), nullable=False)
    fName               = db.Column(db.String(20),  nullable=False)
    lName               = db.Column(db.String(20),  nullable=False)
    jobDescription      = db.Column(db.String(50))
    viewPriveledgeYN    = db.Column(db.String(1),   nullable=False)
    insertPriveledgeYN  = db.Column(db.String(1),   nullable=False)
    updatePriveledgeYN  = db.Column(db.String(1),   nullable=False)
    deletePriveledgeYN  = db.Column(db.String(1),   nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is write‐only")

    @password.setter
    def password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)
