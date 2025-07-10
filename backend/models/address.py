from backend.utils.db_connect import db

class Address(db.Model):
    __tablename__ = 'address'

    addressID = db.Column(db.Integer, primary_key=True)
    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'))
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipCode = db.Column(db.String(10))
    activeYN = db.Column(db.String(1))
    primaryYN = db.Column(db.String(1))

    def __repr__(self):
        return f'<Address {self.address}>'

