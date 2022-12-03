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
        self.products = None
        self.qty = None
        self.amount = None

    def add_products_to_basket(self):
        self.products =
        pass

#place an order
po = place_order()
po.add_products_to_basket()


