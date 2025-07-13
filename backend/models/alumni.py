from backend.utils.db_connect import db

class Alumni(db.Model):
    __tablename__ = 'alumni'

    alumniID = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String(50), nullable=False)
    lName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    DOB = db.Column(db.Date)
    gender = db.Column(db.String(50))
    ethnicity = db.Column(db.String(50))
    website = db.Column(db.String(255))
    linkedin_link = db.Column(db.String(255))
    twitter_link = db.Column(db.String(255))
    facebook_link = db.Column(db.String(255))
    instagram_link = db.Column(db.String(255))
    guestSpeakerYN = db.Column(db.String(1))
    newsLetterYN = db.Column(db.String(1))
    imageThumb = db.Column(db.String(255))
    imageNormal = db.Column(db.String(255))
    description = db.Column(db.Text)
    deceasedYN = db.Column(db.String(1))
    deceasedDT = db.Column(db.Date)
    deceasedNotes = db.Column(db.Text)

    # Relationships (strings avoid import errors)
    addresses = db.relationship('Address', backref='alumnus', cascade='all, delete-orphan')
    degrees = db.relationship('Degree', backref='alumnus', cascade='all, delete-orphan')
    employments = db.relationship('Employment', backref='alumnus', cascade='all, delete-orphan')
    donations = db.relationship('Donation', backref='alumnus', cascade='all, delete-orphan')
    skills = db.relationship('Skillset', backref='alumnus', cascade='all, delete-orphan')
    sentTo = db.relationship('SentTo', back_populates='alumni')

    def __repr__(self):
        return f"<Alumni {self.alumniID} - {self.fName} {self.lName}>"

