from flask import Flask
from .config import Config
from .utils.db_connect import db
from .routes.auth import auth_bp
from .routes.alumni import alumni_bp
from .routes.address import address_bp
from .routes.degree import degree_bp
from .routes.employment import employment_bp
from .routes.donation import donation_bp
from .routes.skillset import skillset_bp
from .routes.newsletter import newsletter_bp
from .routes.sentto import sentto_bp

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)
    db.init_app(app)

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
