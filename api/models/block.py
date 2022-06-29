from api.database import db

class Block(db.Model):
    __table_name__ = 'blocks'

    blocker_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    blocked_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    blocker = db.relationship('User', foreign_keys='Block.blocker_id')
    blocked = db.relationship('User', foreign_keys='Block.blocked_id')
 
    def __repr__(self):
        return f"<Block('{self.blocker_id}', '{self.blocked_id}')>"

    def serialize(self):
        return {'blocker_id': self.blocker_id, 'blocked_id': self.blocked_id}