class employee_authentication(object):
    def __init__(self):
        self.authentication = False
        self.branch_name = None
        self.emp_id = None

    def login(self,username, password):
        # match username nad password from database and get branch and employee id from db
        # after verification get and set the emp id and branch id
        self.authentication = True
        self.branch_name = "brn_001"
        self.emp_id = "emp_001"

class products(object):
    def __init__(self):
        self.prd_name
        prd_desc
        prd_least_margin
        prd_mrp
        prd_sale_price
        prd_gst_per

    def add_product(self,prd_name,prd_desc,prd_least_margin,prd_mrp,prd_sale_price,prd_gst_per):
        # add product to database
        return "Product added"

    def add_product_availability(self,batch_id,prd_id,brn_id,prd_added_date,prd_exp_date,prd_qty):
        # add product
        return "Added product quantity"

    def view_all_products(self):
        pass
        return list()

class employee(object):
    def __init__(self):
        pass
    def add_employee(self):
        pass
    def remove_employee(self):
        pass

class branch(object):
    def __init__(self):
        self.brn_name = None
        self.brn_city = None
        self.brn_state = None
        self.brn_country = None
        self.brn_status = None

    def add_branch(self,branch_name,branch_city,branch_state,branch_country):
        self.brn_name = branch_name
        self.brn_city = branch_city
        self.brn_state = branch_state
        self.brn_country = branch_country
        self.brn_status = "Inactive"

    def Activate_brach(self,):
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