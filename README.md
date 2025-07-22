# alumni-management-system
IS Capstone Alumni Management System 
# Alumni Management System (Backend)

This is a back-end content management system (CMS) for managing alumni data, built using Flask, SQLAlchemy, and WTForms. It provides user authentication, role-based permissions, and full CRUD support for alumni-related data.

---

## Features

- User authentication with hashed passwords
- Session and permission management
- CRUD operations for:
  - Alumni
  - Addresses
  - Degrees
  - Employment
  - Donations
  - Skills
- Modular Blueprint structure
- Flash messages for user feedback
- Search and filtering in list views
- Error handling pages (403, 404, etc.)

---

## Project Structure

```
alumni-management-system/
├── run.py
├── requirements.txt
├── /backend/
│   ├── __init__.py
│   ├── /utils/
│   │   ├── config.py
│   │   └── db_connect.py
│   ├── /models/
│   └── /app/
│       ├── /forms/
│       └── /routes/
└── /templates/
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip
- Git (optional)
- MySQL 

---

### Clone the Repository

```bash
git clone https://github.com/marmar0920/alumni-management-system.git
cd alumni-management-system
```

---

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### backend/utils/config.py

Create a configuration file like this:

```python
class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mardnie@localhost/alumnidb"  # Replace with your MySQL URI if needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

## Database Setup

### Option A: Using SQLite (default)

```bash
export FLASK_APP=run.py       # Windows: set FLASK_APP=run.py
flask shell
```

Then run:

```python
from run import app
from backend.utils.db_connect import db
with app.app_context():
    db.create_all()
```

---

### Option B: Using MySQL

Run the following commands in the MySQL CLI:

```sql
CREATE DATABASE alumnidb;
USE alumnidb;

SOURCE path/to/alumnidb_alumni.sql;
SOURCE path/to/alumnidb_users.sql;
SOURCE path/to/alumnidb_address.sql;
SOURCE path/to/alumnidb_degrees.sql;
SOURCE path/to/alumnidb_employment.sql;
SOURCE path/to/alumnidb_donations.sql;
SOURCE path/to/alumnidb_skills.sql;
SOURCE path/to/alumnidb_newsletter.sql;
SOURCE path/to/alumnidb_sentto.sql;
```

Refer to the full setup guide for resolving any foreign key or data-related errors.

---

## Running the Application

```bash
export FLASK_APP=run.py
flask run
```

Application runs at: http://127.0.0.1:5000

---

## Application Routes

| Module     | URL                  |
|------------|----------------------|
| Alumni     | /alumni/list         |
| Address    | /address/list        |
| Degree     | /degree/list         |
| Employment | /employment/list     |
| Donations  | /donation/list       |
| Skills     | /skills/list         |
| Login      | /login               |
| Logout     | /logout              |

---

## Testing

- Use provided `.sql` scripts to load sample data
- Login with test users
- Verify:
  - CRUD operations
  - Session handling and permission restrictions
  - Flash messages
  - Error pages
- Capture and document test results

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Template not found | Ensure correct path and file name in `/templates` |
| Password issues | Use `generate_password_hash()` and `check_password_hash()` |
| Column too short | Use `VARCHAR(255)` for password fields |
| Import errors | Use absolute imports from the `backend` module |

---

## Full Requirements List

```
attrs==25.3.0
blinker==1.9.0
certifi==2025.7.9
cffi==1.17.1
click==8.2.1
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
Flask==2.3.2
Flask-Login==0.6.3
Flask-SQLAlchemy==3.0.5
Flask-WTF==1.2.2
greenlet==3.2.3
gunicorn==23.0.0
h11==0.16.0
idna==3.10
iniconfig==2.1.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
numpy==2.3.1
outcome==1.3.0.post0
packaging==25.0
pandas==2.3.0
pluggy==1.6.0
pycparser==2.22
Pygments==2.19.2
PyMySQL==1.1.0
PySocks==1.7.1
pytest==8.4.1
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2025.2
selenium==4.34.2
six==1.17.0
sniffio==1.3.1
sortedcontainers==2.4.0
SQLAlchemy==2.0.41
trio==0.30.0
trio-websocket==0.12.2
typing_extensions==4.14.1
tzdata==2025.2
urllib3==2.5.0
websocket-client==1.8.0
Werkzeug==3.1.3
wsproto==1.2.0
WTForms==3.2.1
```

---

## License

This project is licensed under the MIT License.
