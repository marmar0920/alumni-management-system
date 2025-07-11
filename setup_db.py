from run import app
from backend.utils.db_connect import db
from backend.models.user import User

with app.app_context():
    print("Creating all database tables (if not exist)...")
    db.create_all()

    print("Checking for existing test user...")
    existing_user = User.query.filter_by(UID='testuser').first()
    if existing_user:
        print("Test user already exists!")
    else:
        new_user = User(
            UID='testuser',
            password='testpass',fName='Test',
            lName='User',
            jobDescription='Admin',
            viewPriveledgeYN='Y',
            insertPriveledgeYN='Y',
            updatePriveledgeYN='Y',
            deletePriveledgeYN='Y'
        )
        db.session.add(new_user)
        db.session.commit()
    print("Test user created successfully!")
