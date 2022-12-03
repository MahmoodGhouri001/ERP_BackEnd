class product(object):
    def __init__(self):
        pass
    def add_product(self):
        pass
    def add_product_availability(self):
        pass

class employee(object):
    def __init__(self):
        pass
    def add_employee(self):
        pass
    def remove_employee(self):
        pass

class branch(object):
    def __init__(self):
        pass
    def add_branch(self):
        pass
    def remove_brach(self):
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
        self.brn_id = None
        self.emp_id = None
        self.cust_id = None
        pass

    def get_emp_brn_cust_details(self):
        return emp_id,brn_id,cust_id


#place an order
po = place_order()


