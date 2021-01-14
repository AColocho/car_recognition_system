from flask import Flask
from config import config
 

def createAPP(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    from .main import main as mainBlueprints
    app.register_blueprint(mainBlueprints)
    
    return app