from flask import Flask, redirect, url_for
from backend.utils.db_connect import db
from backend.utils.config import Config

# Import Blueprints
from backend.app.routes.auth_routes import auth_bp
from backend.app.routes.alumni_routes import alumni_bp
from backend.app.routes.address_routes import address_bp
from backend.app.routes.degree_routes import degree_bp
from backend.app.routes.employment_routes import employment_bp
from backend.app.routes.donation_routes import donation_bp
from backend.app.routes.skillset_routes import skillset_bp
from backend.app.routes.newsletter_routes import newsletter_bp
from backend.app.routes.sentto_routes import sentto_bp

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)
    db.init_app(app)
    # Root route: automatically redirect to alumni list
    @app.route('/')
    def home():
        return redirect(url_for('alumni.list_alumni'))

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(alumni_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(degree_bp)
    app.register_blueprint(employment_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(skillset_bp)
    app.register_blueprint(newsletter_bp)
    app.register_blueprint(sentto_bp)

    # Seed the database automatically if empty
    from backend.utils.seed_data import seed_all_data
    with app.app_context():
        db.create_all()
        seed_all_data()

    return app
