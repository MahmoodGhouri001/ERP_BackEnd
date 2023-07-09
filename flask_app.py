from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

# AWS Hosted database
#username = "admin"
#password = "Root1234"
#Database_name = "ERP_SYSTEM"
#aws_end_point = "erp-database.cd17exehpjhk.us-west-2.rds.amazonaws.com"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Root1234@erp-database.cd17exehpjhk.us-west-2.rds.amazonaws.com/ERP_SYSTEM'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ae9e9de7906d0f1fd417c1ea75c02c70'


db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Database models
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self,password):
        self.password = generate_password_hash(password)
        print(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Branch(db.Model):
    branch_id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String, nullable=False)
    branch_city = db.Column(db.String, nullable=False)
    branch_state = db.Column(db.String, nullable=False)
    branch_country = db.Column(db.String, nullable=False)
    branch_status = db.Column(db.String, nullable=False)

    def __init__(self,branch_name=None,branch_city=None,branch_state=None,branch_country=None,branch_status="Inactive"):
        self.branch_name = branch_name
        self.branch_city = branch_city
        self.branch_state = branch_state
        self.branch_country = branch_country
        self.branch_status = branch_status

    def activate_branch(self):
        self.branch_status = "Active"

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Schemas for serialization/deserialization
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username')

class ResourceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
class branchSchema(ma.Schema):
    class Meta:
        fields = ('branch_id','branch_name','branch_city','branch_state','branch_country','branch_status')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)
branch_schema = branchSchema()
branchs_schema = branchSchema(many=True)

# Routes for the REST API
@app.route('/api/users', methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']

    existing_user = Users.query.filter_by(username=username).first()

    if existing_user:
        return jsonify(message='Username already exists'), 409

    new_user = Users(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='User created successfully'), 201

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    users = Users.query.filter_by(username=username).first()

    if users and users.check_password(password):
        access_token = create_access_token(identity=users.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid username or password'), 401


@app.route('/api/branch', methods=['POST'])
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

@app.route('/api/branch/<int:branch_id>', methods=['PUT'])
@jwt_required()
def activate_branch(branch_id):
    branch = Branch.query.get(branch_id)
    if branch:
        branch.activate_branch()
        db.session.commit()
        return jsonify(message='Resource updated successfullys'),200
    else:
        return jsonify(message="Branch not found!")

@app.route('/api/branch', methods=['GET'])
@jwt_required()
def get_branch():
    all_branches = Branch.query.all()
    result = branchs_schema.dump(all_branches)
    return jsonify(result), 200


@app.route('/api/resources', methods=['GET'])
@jwt_required()
def get_resources():
    resources = Resource.query.all()
    result = resources_schema.dump(resources)
    return jsonify(result), 200

@app.route('/api/resources', methods=['POST'])
@jwt_required()
def create_resource():
    name = request.json['name']
    description = request.json['description']

    new_resource = Resource(name=name, description=description)
    db.session.add(new_resource)
    db.session.commit()

    return jsonify(message='Resource created successfully'), 201

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
@jwt_required()
def get_resource(resource_id):
    resource = Resource.query.get(resource_id)

    if resource:
        result = resource_schema.dump(resource)
        return jsonify(result), 200
    else:
        return jsonify(message='Resource not found'), 404

@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
@jwt_required()
def update_resource(resource_id):
    resource = Resource.query.get(resource_id)

    if resource:
        resource.name = request.json['name']
        resource.description = request.json['description']
        db.session.commit()
        return jsonify(message='Resource updated successfullys'),200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)