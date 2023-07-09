from app import db

# Database models
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
