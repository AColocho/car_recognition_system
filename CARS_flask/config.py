import os

class config:
    STATIC_IMAGES = os.getcwd()+'/app/static/images'
    SEND_FILE_MAX_AGE_DEFAULT = 0
    
    @staticmethod
    def init_app(app):
        pass
    
    
class DevelopmentConfig(config):
    DEBUG=True

class ProductionConfig(config):
    DEBUG=False

config = {
    'development': DevelopmentConfig,
    'production':ProductionConfig}
