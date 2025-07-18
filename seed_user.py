from run import app
from backend.utils.db_connect import db
from backend.models.user import User

with app.app_context():
    db.create_all()

    existing_user = User.query.filter_by(UID='105386').first()
    if existing_user:
        print("User already exists.")
    else:
        new_user = User(
            UID='105386',
            fName='Admin',
            lName='User',
            jobDescription='Administrator',
            viewPriveledgeYN='Y',
            insertPriveledgeYN='Y',
            updatePriveledgeYN='Y',
            deletePriveledgeYN='Y'
        )
        # Set password **after** object is created to trigger @password.setter
        new_user.password = 'MyDogButch2024'

        db.session.add(new_user)
        db.session.commit()
        print("✅ User created successfully.")
