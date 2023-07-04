'''
inventory management, with py inheritance, import with excel inventory management
'''
"""
-------------- CLASSES
Class : tax calculation 
> gst, cgst, sgst calculates
	
Class : purchase
> add prodcut in master_inventory.xlsx file with all cols name, input product data from col name
> update inventorty_movement.xlsx with incoming type of line (i.e. purchase/sale)
> add purchase line in purchase.xlsx file after purchase
> check if product exists in master file then add quantity and avg price else add product

Class : sales
> add sale line after sale in sales.xlsx
> take ip from user > product, customer_name, quantity

Class : Product
> add products 

------------- exceL FILES
master_inventory.xlsx
Cols : product name, product_sku, vendor name, avg_price, quantity, purchase_price, sale price, avg or purcahse+sale

inventory_movement.xlsx (history)
Cols : product, date , operation type (option : incoming/outgoing), quantity, price, customer, vendor

sales.xlsx
cols : customer, product, price, tax_total, total_amount

purchase.xlsx
xlsx : vendor, prodduct, purchase_price, tax, total_amopunt


"""
