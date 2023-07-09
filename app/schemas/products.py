from app import ma
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('product_id','product_name','product_description','product_MRP','product_sale_price','product_Tax','product_quantity')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)