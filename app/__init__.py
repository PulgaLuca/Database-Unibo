from flask import Flask
from .extensions import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints registrations.
    from .blueprints.mission import mission_bp
    from .blueprints.rocket import rocket_bp
    from .blueprints.sensor import sensor_bp
    # from .blueprints.auth import auth_bp
    from .blueprints.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(mission_bp, url_prefix='/mission')
    app.register_blueprint(rocket_bp, url_prefix='/rocket')
    app.register_blueprint(sensor_bp, url_prefix='/sensor')
    
    return app
