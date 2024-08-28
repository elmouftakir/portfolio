class DevConfig(Config):
    # Development configuration: enables debug mode and SQLAlchemy query logging
    DEBUG = config('DEBUG', cast=bool)
    SQLALCHEMY_ECHO = True  # Logs SQL queries to the console for debugging purposes
    # Sets the database URI to use a SQLite database file in the development environment
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

class TestConfig(Config):
    # Testing configuration: enables testing mode and uses an in-memory SQLite database
    TESTING = True
    # Sets the database URI to use an in-memory SQLite database for fast tests
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables tracking modifications for performance
    SQLALCHEMY_ECHO = True  # Logs SQL queries to the console for debugging during tests

class ProdConfig(Config):
    # Production configuration: sets the database URI to use a SQLite database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

# Dictionary to map different environments to their respective configurations
config_dict = {
    'dev': DevConfig,          # Development environment configuration
    'production': ProdConfig,  # Production environment configuration
    'test': TestConfig         # Testing environment configuration
}
