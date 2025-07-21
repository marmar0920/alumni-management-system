from backend.utils.db_connect import db

class Degree(db.Model):
    __tablename__ = 'degree'

    degreeID = db.Column(db.Integer, primary_key=True)
    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'))
    major = db.Column(db.String(50), nullable=False)
    minor = db.Column(db.String(50))
    graduationDT = db.Column(db.Date)
    university = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    alumnus = db.relationship('Alumni', back_populates='degrees')
    def __repr__(self):
        return f'<Degree {self.major}>'

