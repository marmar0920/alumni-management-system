from backend.utils.db_connect import db

class Newsletter(db.Model):
    __tablename__ = 'newsletter'

    NID = db.Column(db.Integer, primary_key=True)
    newsDate = db.Column(db.Date, nullable=False)
    headline = db.Column(db.String(200))
    description = db.Column(db.String(200))
    link = db.Column(db.String(200))
    fileLoc = db.Column(db.String(200))

    # Relationship to sentTo
    sentTo = db.relationship('SentTo', backref='newsletter', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Newsletter {self.NID} - {self.headline}>'

