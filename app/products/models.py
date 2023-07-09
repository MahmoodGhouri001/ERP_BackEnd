from app import db

# Database models
class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_name = db.Column(db.String(150), nullable=False)
    product_description = db.Column(db.String(1000))
    product_MRP = db.Column(db.Integer,nullable=False)
    product_sale_price = db.Column(db.Integer,nullable=False)
    product_Tax = db.Column(db.Integer,nullable=False)
    product_quantity = db.Column(db.Integer,nullable=False)

    def __init__(self, product_name,product_MRP ,product_sale_price ,product_Tax,product_quantity,product_description=None):
        self.product_name = product_name
        self.product_description = product_description
        self.product_MRP = product_MRP
        self.product_sale_price = product_sale_price
        self.product_Tax = product_Tax
        self.product_quantity = product_quantity


    def update_product_info(self,product_name,product_MRP,product_sale_price,product_Tax,product_quantity,product_description=None):
        self.product_name = product_name
        self.product_description = product_description
        self.product_MRP = product_MRP
        self.product_sale_price = product_sale_price
        self.product_Tax = product_Tax
        self.product_quantity = product_quantity



