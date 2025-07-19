from backend.utils.db_connect import db

class Newsletter(db.Model):
    NID = db.Column(db.Integer, primary_key=True)
    newsDate = db.Column(db.Date, nullable=False)
    headline = db.Column(db.String(200))
    description = db.Column(db.String(200))
    link = db.Column(db.String(200))
    fileLoc = db.Column(db.String(200))

    # Relationship to SentTo
    sentTo = db.relationship('SentTo', back_populates='newsletter')

    def __repr__(self):
        return f"<Newsletter {self.NID} - {self.title}>"
