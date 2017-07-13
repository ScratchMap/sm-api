from app.utils import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    geo_lat = db.Column(db.Float, nullable=False)
    geo_lng = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)

    def __repr__(self):
        return '<Post %d %r>' % (self.id, self.title)

    @property
    def get_id_title(self):
        return {
            'id' : self.id,
            'title' : self.title
        }

    @property
    def get_all_data(self):
        return {
            'id' : self.id,
            'datetime' : self.datetime.isoformat(),
            'data' : {
                'title' : self.title,
                'body' : self.description
            },
            'geo' : {
                'lat' : self.geo_lat,
                'lng' : self.geo_lng
            }
        }
