class TestConfig:
    """Set Flask configuration variables."""

    TESTING = True

    # General Config
    SECRET_KEY = 'secretkey'
    FLASK_ENV = 'development'
    SERVER_NAME = 'localhost.localdomain'

    # Mongo
    MONGODB_SETTINGS = {
        'db': 'testdb',
        'host': 'localhost',
        'port': 27017,
        'mock': True,
    }
