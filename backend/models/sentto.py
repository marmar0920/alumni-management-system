from backend.utils.db_connect import db

class SentTo(db.Model):
    __tablename__ = 'sentto'

    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'), primary_key=True)
    NID = db.Column(db.Integer, db.ForeignKey('newsletter.NID'), primary_key=True)
    sentDate = db.Column(db.Date)

    # Relationships to Alumni and Newsletter
    alumnus = db.relationship('Alumni', backref=db.backref('sentTo', cascade='all, delete-orphan'))
    newsletter = db.relationship('Newsletter', backref=db.backref('sentToEntries', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<SentTo AlumniID={self.alumniID} NewsletterID={self.NID}>'

