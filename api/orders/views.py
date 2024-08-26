from flask_restx import Resource,Namespace


order_namespace=Namespace('orders',description="Namespace for orders")


@order_namespace.route('/orders')
class OrderGetCreate(Resource):
    
    def get(self):
        
        """
            get all orders
        
        """
        pass
    
    def post(self):
        
        """
            place a new orders
        
        """
        pass
    
@order_namespace.route('/order/<int:order_id>')

class GetUpdateDelete(Resource):
    
    def get(self,order_id):
        
        """
            Retrieve an order by its id
        """
        
        pass
    
    def put(self,order_id):
        
        """
            update an order by its id
        """
        
        pass
    
    def delete(self,order_id):
        
        """
            delete an order by its id
        """
        
        pass
@order_namespace.route('/user/<int:user_id>/order/<int:order_id>/')
class GetSpecificOrderByUser(Resource):
    def get(self,user_id,order_id):

        """
            Get a user's specific order
        """
        pass
    
@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
     def get(self,user_id):
        """
            Get all orders by a specific user
        """
@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
    def patch(self,order_id):
        """
            Update an order's status
        """