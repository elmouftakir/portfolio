# Define an error handler for 404 Not Found errors
@api.errorhandler(NotFound)
def not_found(error):
    # Return a JSON response with an error message and a 404 status code
    return {"error": "Not Found"}, 404

# Define an error handler for 405 Method Not Allowed errors
@api.errorhandler(MethodNotAllowed)
def method_not_allowed(error):
    # Return a JSON response with an error message and a 405 status code
    return {"error": "Method Not Allowed"}, 405

# Add the 'order_namespace' to the API
api.add_namespace(order_namespace)

# Add the 'auth_namespace' to the API with a specified path '/auth'
api.add_namespace(auth_namespace, path='/auth')

# Define a shell context processor function for the Flask shell
@app.shell_context_processor
def make_shell_context():
    # Return a dictionary with the database and model instances
    return {
        'db': db,
        'User': User,
        'Order': Order
    }

# Return the Flask application instance
return app
