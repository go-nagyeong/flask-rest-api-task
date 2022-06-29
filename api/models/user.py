from api.database import db

class User(db.Model):
    __table_name__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(100))
 
    def __repr__(self):
        return f"<User('{self.id}', '{self.email}', '{self.phone_number}')>"

    def serialize(self):
        return {'id': self.id, 'email': self.email, 'phone_number': self.phone_number}