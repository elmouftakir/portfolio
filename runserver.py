from api import create_app
from api.config.config import config_dict

# Create a Flask application instance using the production configuration
app = create_app(config=config_dict['production'])

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run()

