from backend.utils.db_connect import db

class Donation(db.Model):
    __tablename__ = 'donation'

    donationID = db.Column(db.Integer, primary_key=True)
    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'))
    donationAmt = db.Column(db.Integer)
    donationDT = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(200))
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<Donation {self.donationAmount}>'

