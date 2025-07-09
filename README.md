# alumni-management-system
IS Capstone Alumni Management System 
# Alumni Management System (Backend)

A Flask-based Content Management System for managing alumni data, with session-based login and CRUD permissions.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Database](#database)
- [How to Contribute](#how-to-contribute)
- [License](#license)

---

## ✅ Overview

This is the back-end service for the Alumni Management System. It manages:

- Alumni records
- Addresses
- Degrees
- Employment
- Donations
- Skillsets
- Newsletters
- SentTo mappings

Includes user authentication with permission flags for View/Insert/Update/Delete.

---

## ✅ Features

- Secure login with hashed passwords
- Session-based permissions
- Full CRUD for all entities
- JSON API endpoints
- MySQL database integration
- WTForms validation
- Jinja2 templates with Bootstrap
- GitHub Actions CI

---

## ✅ Tech Stack

- Python 3.9+
- Flask
- Flask-SQLAlchemy
- PyMySQL
- Flask-WTF
- WTForms
- MySQL 8+
- GitHub Actions

---

## ✅ Folder Structure

alumni-management-system/
├── backend/
│ ├── run.py
│ └── app/
│ ├── init.py
│ ├── config.py
│ ├── utils/
│ │ └── db_connect.py
│ ├── models/
│ ├── forms/
│ ├── routes/
│ ├── templates/
│ └── static/
├── database/
│ ├── create_tables.sql
│ └── seed_data.sql
├── docs/
│ ├── functional-requirements.md
│ ├── technical-design.md
│ ├── test-plan.md
│ ├── checklist.md
│ └── master-guide.md
├── .github/
│ └── workflows/ci.yml
├── .env (ignored)
├── requirements.txt
└── README.md

## ✅ Setup

### 1 Clone the Repo

```bash
git clone https://github.com/your-username/alumni-management-system.git
cd alumni-management-system

### 2️ Create Virtual Environment
powershell
python -m venv .venv
.venv\Scripts\activate

### 3 Install Requirements
pip install -r requirements.txt
