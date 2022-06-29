from api.database import db
from datetime import datetime

class Post(db.Model):
    __table_name__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref='user')

    def update(self, title, content):
        if title:
            self.title = title
        if content:
            self.content = content
        self.updatedAt = datetime.now()
        return self

    def __repr__(self):
        return f"<Post('{self.id}', '{self.author_id}', '{self.title}', '{self.content}')>"
    
    def serialize(self):
        return {
            'id': self.id,
            'author': self.author_id,
            'title': self.title,
            'content': self.content,
            'createdAt': self.createdAt.strftime('%y-%m-%d %H:%M'),
            'updatedAt': self.updatedAt.strftime('%y-%m-%d %H:%M')
        }