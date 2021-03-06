from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class Admin(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    ################################################################

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash, password)

class NewLead(db.Model):

    # Create a table in the db
    __tablename__ = 'newlead'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    fullname = db.Column(db.String(64), index=True)
    mobile = db.Column(db.String(64), index=True)
    leadfrom = db.Column(db.String(64))
    handleby = db.Column(db.String(64))

    def __init__(self, email, fullname, mobile, leadfrom, handleby):
        self.email = email
        self.fullname = fullname
        self.mobile = mobile
        self.leadfrom = leadfrom
        self.handleby = handleby
