from werkzeug.security import generate_password_hash, check_password_hash
from app import db


# Database models
class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True, nullable=False)
    emp_name = db.Column(db.String, nullable=False)
    emp_pass = db.Column(db.String, nullable=False)
    emp_DOB = db.Column(db.Date, nullable=False)
    emp_number = db.Column(db.String, nullable=False, unique=True)
    emp_email = db.Column(db.String, nullable=False, unique=True)
    emp_DOJ = db.Column(db.Date,nullable=False)
    emp_dept = db.Column(db.String, nullable=False)
    emp_status = db.Column(db.String, nullable=False)
    emp_access = db.Column(db.String, nullable=False)

    from datetime import datetime
    current_date = datetime.today().strftime('%Y-%m-%d')
    def __init__(self, emp_name, emp_pass=None,emp_DOB=None,emp_number=None,emp_email=None,emp_DOJ=current_date,emp_dept="Bench",emp_status="Inactive",emp_access="general"):
        self.emp_name = emp_name
        self.emp_pass = emp_pass
        self.emp_DOB = emp_DOB
        self.emp_number = emp_number
        self.emp_email = emp_email
        self.emp_DOJ = emp_DOJ
        self.emp_dept = emp_dept
        self.emp_status = emp_status
        self.emp_access = emp_access

    def activate_employee(self):
        self.emp_status = "Active"

    def update_emp_access(self,emp_access):
        self.emp_access = emp_access

    def set_password(self,emp_pass):
        self.emp_pass = generate_password_hash(emp_pass)
        print(self.emp_pass)

    def check_password(self, password):
        return check_password_hash(self.password, password)


