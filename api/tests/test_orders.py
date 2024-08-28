import unittest
from .. import create_app
from ..config.config import config_dict
from ..models.orders import Order
from ..utils import db
from flask_jwt_extended import create_access_token

class OrderTestCase(unittest.TestCase):
    # Setup method to initialize the test environment
    def setUp(self):
        # Create the Flask app instance with the test configuration
        self.app = create_app(config=config_dict['test'])
        # Establish an application context for the test
        self.appctx = self.app.app_context()
        
        # Push the app context to make it active
        self.appctx.push()
        
        # Create a test client to simulate HTTP requests to the app
        self.client = self.app.test_client()
        
        # Create all database tables before each test
        db.create_all()

    # Teardown method to clean up after each test
    def tearDown(self):
        # Drop all tables in the database to ensure a clean state for the next test
        db.drop_all()
