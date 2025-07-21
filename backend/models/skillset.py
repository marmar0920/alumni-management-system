from backend.utils.db_connect import db

class Skillset(db.Model):
    __tablename__ = 'skillset'

    SID = db.Column(db.Integer, primary_key=True)
    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'))
    skill = db.Column(db.String(50), nullable=False)
    proficiency = db.Column(db.String(10))
    description = db.Column(db.String(100))
    alumni = db.relationship("Alumni", back_populates="skills")
    def __repr__(self):
        return f'<Skillset {self.skill}>'

