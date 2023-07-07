import datetime
# import Product
from xlutils.copy import copy
import xlrd
import xlwt

class Purchase():

    def testing(self):
        wb = xlrd.open_workbook("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/testing/inventory_movement.xls")
        ws = wb.sheet_by_name('Sheet1') #w1

        nth_row = ws.nrows
        nth_col = ws.ncols

        copy_wb = copy(wb) # make writable copy of opened excel file
        copy_sh = copy_wb.get_sheet(0) # read the first sheet to withe within writable copy

    def excel_func(self,workbook):
        workbook = xlrd.open_workbook(workbook)  # open each workbook
        worksheet = workbook.sheet_by_index(0)  # get sheet from sheet no
        nth_row = worksheet.nrows  # get nth row
        nth_col = worksheet.ncols  # get nth col
        copy_workbook = copy(workbook)  # copy each workbook : FOR SAVE OPERATION
        copy_worksheet = copy_workbook.get_sheet(0)  # copy each worksheet : FOR WRITING OPERATION
        l = [workbook, worksheet, nth_row, nth_col, copy_workbook, copy_worksheet]

        return l

    def sell(self):
        excel_open_close_master = self.excel_func("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xls")

        sku = str(input("Enter sku : "))
        flag = False
        j = 0
        cell = None
        for i in range(excel_open_close_master[2]):
            each = excel_open_close_master[1].row(i)
            if each[1].value == sku:
                flag = True
                flag = True
                j = i
                cell = each
                break

        if flag:
            print(True)

            # ------------------------------ UPDATE MASTER INVENTORY
            # enter quantity to sell, minus into master dict, change total amount in master dict
            qty = int(input("Enter quantity : "))
            remining_qty = cell[2].value - qty
            final_total = remining_qty * cell[3].value
            excel_open_close_master[5].write(j,2,remining_qty)
            excel_open_close_master[5].write(j,2,remining_qty)
            excel_open_close_master[5].write(j,4,final_total)
            excel_open_close_master[4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xls")


            # --------------------------------- UPDATE SELL.XLSX FILE
            # --------------------------------- add data to SELL.XLSX file
            # pname, psku, quantity, purchaseprice = sell p from invenrot, total amounb = sellp * qty, cgst, S, I, total
            excel_open_close_sales = self.excel_func(
                "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/sales.xls")

            cgst = (qty * cell[3].value * 6)/100
            igst = (qty * cell[3].value * 18)/100
            total_tax = (2*cgst) + igst
            sell_arr = [cell[0].value, sku, qty, cell[6].value, qty * cell[6].value, cgst,cgst,igst,total_tax]
            c = 0
            for s in sell_arr:
                excel_open_close_sales[5].write(excel_open_close_sales[2],c,s)
                c += 1
            excel_open_close_sales[4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/sales.xls")


            # --------------------------------- UPDATE SELL.XLSX FILE
            # 'product_name', 'date_of_changes', 'quantity_changes', 'price : at which sold', 'customer_name', 'vendor','purchase_or_cell'
            excel_open_close_movement = self.excel_func(
                "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/inventory_movement.xls")

            customer_name = str(input("Enter name of customer : "))
            movement_arr = [cell[0].value, datetime.date.today().strftime("%d-%m-%Y"), qty, cell[6].value, customer_name, cell[5].value, 'Sell']
            a = 0
            for o in movement_arr:
                excel_open_close_movement[5].write(excel_open_close_movement[2],a,o)
                a += 1
            excel_open_close_movement[4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/inventory_movement.xls")


        if not flag:
            print(False)


    # -----------------------------------------------  PURCHASE UPDATE DATA FUNC ---------------------------
    def update_purchase(self):
        print("inside")
        obj = Product()
        x = obj.getInput()
        # update in 2 files : purchase.xlsx and movement.xlsx
        # PURCHASE : product_name, sku, quantity, purchase_price(for inventory), total = purchase_price * quantity, tax = 0
        # MOVEMENT : # 'product_name', 'date_of_changes', 'quantity_changes', 'price : at which sold', 'customer_name', 'vendor','purchase_or_cell'
        excel_open_close_purchase = self.excel_func("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/purchase.xls")

        cgst = (x[2]*x[3]*6)/100
        igst = (x[2]*x[3]*18)/100
        total_tax = (2*cgst) + igst

        purchase_arr = [x[0],x[1],x[2],x[3],x[2]*x[3],cgst,cgst,igst,total_tax]
        movement_arr = [x[0],datetime.date.today().strftime("%d-%m-%Y"),x[2], x[4], 'Inventory manager',x[5],'Purchase']
        count = 0
        for each in purchase_arr:
            excel_open_close_purchase[5].write(excel_open_close_purchase[2],count,each)
            count += 1
        excel_open_close_purchase[4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/purchase.xls")


        excel_open_close_movement = self.excel_func("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/inventory_movement.xls")
        counter = 0
        for each_item in movement_arr:
            excel_open_close_movement[5].write(excel_open_close_movement[2], counter, each_item)
            counter += 1
        excel_open_close_movement[4].save(
            "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/inventory_movement.xls")


purchase = Purchase()
ip = int(input("Enter 1 to add stock in master inventory\nEnter 2 to sell products\nPress enter to break\nenter 4 to add data manually : "))
if ip == 1:
    from Product import Product
    purchase.update_purchase()
elif ip == 2:
    purchase.sell()
elif ip == 3:
    purchase.excel_func()
elif ip == 4:
    from Product import Product
    obj = Product()
    obj.getInput()
# elif ip == 5:
#     purchase.testing()