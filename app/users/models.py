from app.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False, server_default='')
    #email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name
