from backend.utils.db_connect import db

class Newsletter(db.Model):
    __tablename__ = 'newsletter'
    NID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    publishDate = db.Column(db.Date)

    # Relationship to SentTo
    sentTo = db.relationship('SentTo', back_populates='newsletter')

    def __repr__(self):
        return f"<Newsletter {self.NID} - {self.title}>"
