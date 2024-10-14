# services/ProductService.py

from models.product import Product, db
from common.error import generate_error_response

class ProductService:

    @staticmethod
    def create_new_product(data):
        if not data or not data.get('name') or not data.get('price'):
            return generate_error_response(400)
        # Define new product
        new_product = Product(name=data['name'], price=data['price']);
        new_product.stock = data['stock']
        new_product.description = data['description']
        # Add new product to database
        db.session.add(new_product)
        db.session.commit()
        return {
            'message': 'Add product successfully!',
            'product': new_product.to_dict(),
            'status_code': 201
        }

    @staticmethod
    def get_all_product():
        products = Product.query.all()
        if not products:
            return generate_error_response(404)
        products_data = [product.to_dict() for product in products]
        return {'product': products_data, 'status_code': 200}

    @staticmethod
    def get_product_by_id(product_id):
        product = Product.query.get(product_id)
        if not product:
            return generate_error_response(404)
        return {'product': product.to_dict(), 'status_code': 200}