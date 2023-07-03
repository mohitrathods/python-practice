class CentralGST():
    
    def get_tax(self,cost_of_product):
        """
        :func:It will calculated cgst of any product price given by user (Integer value only)
        :param: cost_of_product (integer value of a cost_price)
        :returns: It will returns calculated cgst to the base class StateGST, and it must return integer/float value.
        """
        self.cgst = (18 * cost_of_product)/100
        return self.cgst
    
    
class StateGST(CentralGST):
    
    def get_tax(self, cost_of_product):
        """
        :func:It will calculated sgst of any product price given by user(Integer value only)
        :param: cost_of_product (integer value of a cost_price)
        :returns: It will returns calculated sgst to the base class Sale, and it must return integer/float value, it uses super keyword to call get_tax() with cost of product, and return value of cgst and sgst. 
        """
        self.calculate_sgst = (12 * cost_of_product)/100
        
        self.cgst = super().get_tax(cost_of_product)
        return self.calculate_sgst

class TaxCalculation(StateGST):
    
    def __init__(self):
        
        self.tax_dict={"goods": {'cgst':18, 'sgst':12}, "services": {'cgst':13, 'sgst':15}}
        
    def get_tax(self, cost_of_product):
        """
        :func:It will calculated cgst of any product price (Integer value only)
        :param: cost_of_product (integer value of a cost_price)
        :returns: It will returns calculated cgst  and calculated sgst and total_tax to sale(), and it must return integer/float value.
        """
        final_sgst = super().get_tax(cost_of_product)
        final_cgst = self.cgst
        total_tax = cost_of_product + self.cgst + self.calculate_sgst
        return  total_tax
    

