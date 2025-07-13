from backend.utils.db_connect import db
from backend.models.alumni import Alumni
from backend.models.address import Address
from backend.models.degree import Degree
from backend.models.employment import Employment
from backend.models.donation import Donation
from backend.models.skillset import Skillset
import datetime

def seed_all_data():
    if not Alumni.query.first():
        db.session.add_all([
            Alumni(alumniID=201, fName='Corey', lName='Class', email='CClass@yahoo.com', phone='607-722-4969'),
            Alumni(alumniID=202, fName='John', lName='Davis', email='JDavis@yahoo.com', phone='314-524-5336'),
        ])
        print("Seeded Alumni.")

    if not Address.query.first():
        db.session.add_all([
            Address(addressID=100, alumniID=201, address='123 Peachtree St NW', city='Atlanta', state='GA', zipCode='30303', activeYN='Y', primaryYN='Y'),
        ])
        print("Seeded Addresses.")

if not Degree.query.first():
    db.session.add_all([
        Degree(
            degreeID=100,
            alumniID=201,
            major='MIS',
            minor='Cybersecurity',
            graduationDT='2023-05-09',
            university='Kennesaw State University',
            city='Kennesaw',
            state='GA'
        )
    ])
    print("Seeded Degrees.")

    if not Employment.query.first():
        db.session.add_all([
            Employment(EID=100, alumniID=201, company='Tech Solutions', city='Atlanta', state='GA', zipCode='30303', jobTitle='Engineer', startDate='2021-06-14', currentYN='Y'),
        ])
        print("Seeded Employment.")

    if not Donation.query.first():
        db.session.add_all([
            Donation(donationID=100, alumniID=201, donationAmount=500, donationDate='2023-01-08'),
        ])
        print("Seeded Donations.")

    if not Skillset.query.first():
        db.session.add_all([
            Skillset(SID=100, alumniID=201, skillName='Figma', skillProficiency='Beginner'),
        ])
        print("Seeded Skillsets.")

    db.session.commit()
    print("All seed data committed!")
