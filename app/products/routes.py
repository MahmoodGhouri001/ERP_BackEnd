from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Products, db
from app.schemas.products import product_schema, products_schema

products_bp = Blueprint('products', __name__)

@products_bp.route('/api/products', methods=['POST'])
# @jwt_required()
def add_product():
    product_name = request.json['product_name']
    product_description = request.json['product_description']
    product_MRP = request.json['product_MRP']
    product_sale_price = request.json['product_sale_price']
    product_Tax = request.json['product_Tax']
    product_quantity = request.json['product_quantity']

    new_product = Products(product_name,product_MRP,product_sale_price,product_Tax,product_quantity,product_description)
    db.session.add(new_product)
    db.session.commit()

    return jsonify(message='Resource created successfully'), 201

@products_bp.route('/api/products/<int:product_id>', methods=['PUT'])
# @jwt_required()
def update_product(product_id):
    product = Products.query.get(product_id)
    if product:
        product_name = request.json['product_name']
        product_description = request.json['product_description']
        product_MRP = request.json['product_MRP']
        product_sale_price = request.json['product_sale_price']
        product_Tax = request.json['product_Tax']
        product_quantity = request.json['product_quantity']

        product.update_product_info(product_name,product_MRP,product_sale_price,product_Tax,product_quantity,product_description)
        db.session.commit()
        return jsonify(message='Resource updated successfullys'),200
    else:
        return jsonify(message="product not found!")

@products_bp.route('/api/products', methods=['GET'])
# @jwt_required()
def get_all_products():
    all_products = Products.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result), 200

@products_bp.route('/api/products/<int:product_id>', methods=['GET'])
# @jwt_required()
def get_products(product_id):
    product = Products.query.get(product_id)
    if product:
        result = product_schema.dump(product)
        return jsonify(result), 200
    else:
        return jsonify(message="product not found!")