from backend.utils.db_connect import db

class Employment(db.Model):
    __tablename__ = 'employment'

    EID = db.Column(db.Integer, primary_key=True)
    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'))
    company = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(10))
    jobTitle = db.Column(db.String(100))
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)
    currentYN = db.Column(db.String(100))
    
    alumni = db.relationship("Alumni", back_populates="employments")
    def __repr__(self):
        return f'<Employment {self.company} - {self.jobTitle}>'

