from backend.utils.db_connect import db

class Address(db.Model):
    __tablename__ = 'address'

    addressID = db.Column(db.Integer, primary_key=True)
    alumniID = db.Column(db.Integer, db.ForeignKey('alumni.alumniID'))
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipCode = db.Column(db.String(10), nullable=False)
    activeYN = db.Column(db.String(1), default='Y')
    primaryYN = db.Column(db.String(1), default='N')
    
    alumnus = db.relationship('Alumni', back_populates='addresses')
    # alumni = relationship comes from Alumni.backref('alumnus')

    def __repr__(self):
        return f'<Address {self.address}, {self.city}, {self.state}>'

        return f'<Address {self.address}>'

