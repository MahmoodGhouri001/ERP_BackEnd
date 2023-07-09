from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Branch, db
from app.schemas.branch import branchs_schema, branch_schema

branches_bp = Blueprint('branch', __name__)
print("branch __name__ :",__name__)

@branches_bp.route('/api/branch', methods=['POST'])
@jwt_required()
def create_branch():
    brn_name = request.json['brn_name']
    brn_city = request.json['brn_city']
    brn_state = request.json['brn_state']
    brn_country = request.json['brn_country']

    new_branch = Branch(branch_name=brn_name,branch_city=brn_city,branch_state=brn_state,branch_country=brn_country)
    db.session.add(new_branch)
    db.session.commit()

    return jsonify(message='Resource created successfully'), 201

@branches_bp.route('/api/branch/<int:branch_id>', methods=['PUT'])
@jwt_required()
def activate_branch(branch_id):
    branch = Branch.query.get(branch_id)
    if branch:
        branch.activate_branch()
        db.session.commit()
        return jsonify(message='Resource updated successfullys'),200
    else:
        return jsonify(message="Branch not found!")

@branches_bp.route('/api/branch', methods=['GET'])
@jwt_required()
def get_branch():
    all_branches = Branch.query.all()
    result = branchs_schema.dump(all_branches)
    return jsonify(result), 200
