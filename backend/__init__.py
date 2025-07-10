from flask import Flask
from backend.utils.config import Config
from backend.utils.db_connect import db

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
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    # Register Blueprints here
    app.register_blueprint(auth_bp)
    app.register_blueprint(alumni_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(degree_bp)
    app.register_blueprint(employment_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(skillset_bp)
    app.register_blueprint(newsletter_bp)
    app.register_blueprint(sentto_bp)
    return app