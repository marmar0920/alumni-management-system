from backend.utils.db_connect import db

class SentTo(db.Model):
    __tablename__ = 'sentto'
    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'), primary_key=True)
    alumnus = db.relationship('Alumni', back_populates='sentTo')
    NID = db.Column(db.Integer, db.ForeignKey('newsletter.NID'), primary_key=True)
    sentDate = db.Column(db.Date, nullable=False)

    newsletter = db.relationship('Newsletter', back_populates='sentTo')

    def __repr__(self):
        return f"<SentTo AlumniID={self.alumniID}, NID={self.NID}, sentDate={self.sentDate}>"
