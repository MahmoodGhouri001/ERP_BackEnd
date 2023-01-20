import uuid
class employee_authentication(object):
    def __init__(self):
        self.authentication = False
        self.branch_name = None
        self.emp_id = None


    def login(self,username, password):
        # match username nad password from database and get branch and employee id from db
        # after verification get and set the emp id and branch id
        if True:
            self.authentication = True
            self.branch_name = "brn_001"
            self.emp_id = "emp_001"

class products(object):
    def __init__(self):
        self.prd_name = None
        self.prd_desc = None
        self.prd_least_margin = None
        self.prd_mrp = None
        self.prd_sale_price = None
        self.prd_gst_per = None

    def add_product(self,prd_name,prd_desc,prd_least_margin,prd_mrp,prd_sale_price,prd_gst_per):
        # add product to database
        return "Product added"

    def add_product_availability(self,batch_id,prd_id,brn_id,prd_added_date,prd_exp_date,prd_qty):
        # add product availability to already available product
        return "Added product quantity"

    def view_all_products(self):
        # Write a logic for viewing all products
        return list()
    def search_product(self):
        # write a logic if product search made and return list of search product.
        return list()

class employee(object):
    def __init__(self):
        self.emp_id = None
        self.brn_id = None
        self.emp_name = None
        self.emp_password = None
        self.emp_dob = None
        self.emp_phone = None
        self.emp_email = None
        self.emp_doj = None
        self.emp_pic = None
        self.emp_dept = None
        self.business_unit = None
        self.emp_status = None
    def add_employee(self,emp_id,brn_id,emp_name,emp_password,emp_dob,emp_phone,emp_email,emp_doj,emp_pic,emp_dept,business_unit,emp_status):
        pass
    def remove_employee(self):
        pass

def create_db_connection():
    try:
        import pymysql
        connection = pymysql.connect(host='localhost',user='root',password='admin',database='record')
        cursor = connection.cursor()
        if connection:
            return connection,cursor
        else:
            print("Connection failed")
    except Exception as e:
        print("Exception while creating connection with DB",e)
class branch(object):
    def __init__(self):
        self.brn_name = None
        self.brn_city = None
        self.brn_state = None
        self.brn_country = None
        self.brn_status = 'Inactive'

    def add_branch(self,request_data):

        self.brn_name = request_data['branch_name']
        self.brn_city = request_data['branch_city']
        self.brn_state = request_data['branch_state']
        self.brn_country = request_data['branch_country']

        connection, cursor = create_db_connection()
        id = uuid.uuid4()
        sql_query = "insert into branch_details values(NULL,'{}','{}','{}','{}','INACTIVE');".format(self.brn_name,self.brn_city,self.brn_state,self.brn_country)
        cursor.execute(sql_query)
        connection.commit()

        return id

    def activate_brach(self):
        pass
    def deactivate_branch(self):
        pass

class orders(object):
    def __init__(self):
        self.ord_id = None
        self.prd_id = None
        self.qty = None
        self.amount = None


class place_order(object):
    def __init__(self,):
        self.ord_detail_id = None
        self.ord_id = None
        self.ord_date = None
        self.brn_id = self.get_brn_id()
        self.emp_id = self.get_emp_id()
        self.cust_id = self.get_cust_id()
        pass

    def get_emp_id(self):
        pass
        return emp_id

    def get_brn_id(self):
        pass
        return brn_id

    def get_cust_id(self):
        pass
        return cust_id

    def add_products_to_basket(self):
        pass

        return []

class add_items_to_basket(object):
    def __init__(self):
        self.products = list()
        self.product_qty_amount = tuple()

    def add_products_to_basket(self):
        self.product_qty_amount


if __name__=="__main__":
    # Authentication

    pass