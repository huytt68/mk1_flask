from flask import Blueprint, request, jsonify
from services.ProductService import ProductService

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.route('/create', methods=['POST'])
def create_product():
    data = request.get_json()
    result = ProductService.create_new_product(data)
    return jsonify(result), result['status_code']

@product_bp.route('', methods=['GET'])
def get_all_product():
    result = ProductService.get_all_product()
    return jsonify(result), result['status_code']

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    result = ProductService.get_product_by_id(product_id)
    return jsonify(result), result['status_code']