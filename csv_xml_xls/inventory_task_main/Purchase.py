# import Product
from xlutils.copy import copy
import xlrd
import xlwt

class Purchase():

    # --------------------------------------------- UPDATE PURCHASE FILE
    def updatePurchase(self):
        pass

    # -----------------------------------------------  SELL FUNC ---------------------------

    def sellll(self):
        workbook = xlrd.open_workbook(
            "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
        worksheet = workbook.sheet_by_index(0)
        nth_row = worksheet.nrows
        nth_col = worksheet.ncols

        copy_wb = copy(workbook)
        copy_sheet = copy_wb.get_sheet(0)

        # take ip for customer from user
        # customer_name, quantity, sku
        # ---------------------------------- CHECK SKU
        sku = str(input("Enter sku : "))
        flag = False
        j = 0
        row = None
        for i in range(nth_row):
            eachrow = worksheet.row(i)
            if eachrow[1].value == sku:
                flag = True
                j = i
                row = eachrow
                break

        if flag:
            # get qty
            qty = int(input("Enter qty : "))
            # get customer name
            c_name = str(input("Enter customer name : "))

            # minus qty in master_inventory
            old_qty = row[2].value  # old qty
            new_qty = old_qty - qty  # new qty update to master
            new_total = row[6].value * new_qty

            copy_sheet.write(2, j, new_qty)
            copy_sheet.write(4, j, new_total)
            copy_wb.save(
                "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")

            workbook_sell = xlrd.open_workbook(
                "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/sales.xlsx")
            worksheet_cell = workbook_sell.sheet_by_index(0)
            copy_wb_sell = copy(workbook_sell)
            copy_sheet_sell = copy_wb_sell.get_sheet(0)
            nth_row = worksheet_cell.nrows
            nth_col = worksheet_cell.ncols

            # to add data in sell
            product_name = row[0].value
            sku = row[1].value
            purchase_price = row[6].value
            total_amount = purchase_price * qty
            type = 'sell'
            sell_arr_row = [product_name, sku, qty, purchase_price, total_amount]
            c = 0
            for each in range(nth_row):
                copy_sheet_sell.write(nth_row, c, each)
                c += 1

    def excel_func(self):
        # 3 workbooks to open
        # get sheet by index each of those
        # get nth row and col each
        # copy workbook of each
        # copy sheet of each

        workbooks = [
            "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx",
            "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/sales.xlsx",
            "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/inventory_movement.xlsx",
            "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/purchase.xlsx"
        ]

        excel_functions = []
        # open each workbook
        for each_workbook in workbooks:
            workbook = xlrd.open_workbook(each_workbook)  # open each workbook
            worksheet = workbook.sheet_by_index(0)  # get sheet from sheet no
            nth_row = worksheet.nrows  # get nth row
            nth_col = worksheet.ncols  # get nth col
            copy_workbook = copy(workbook)  # copy each workbook : FOR SAVE OPERATION
            copy_worksheet = copy_workbook.get_sheet(0)  # copy each worksheet : FOR WRITING OPERATION
            l = [workbook, worksheet, nth_row, nth_col, copy_workbook, copy_worksheet]
            excel_functions.append(l)

        return excel_functions

    def sell(self):
        excel_functions = self.excel_func()

        sku = str(input("Enter sku : "))
        flag = False
        j = 0
        cell = None
        for i in range(excel_functions[0][2]):
            each = excel_functions[0][1].row(i)
            if each[1].value == sku:
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
            excel_functions[0][5].write(j,2,remining_qty)
            excel_functions[0][5].write(j,4,final_total)
            excel_functions[0][4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")

            # --------------------------------- UPDATE SELL.XLSX FILE
            # --------------------------------- add data to SELL.XLSX file
            # pname, psku, quantity, purchaseprice = sell p from invenrot, total amounb = sellp * qty
            sell_arr = [cell[0].value, sku, qty, cell[6].value, qty * cell[6].value, 0]
            c = 0
            for s in sell_arr:
                excel_functions[1][5].write(excel_functions[1][2],c,s)
                c += 1
            excel_functions[1][4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/sales.xlsx")

            # --------------------------------- UPDATE SELL.XLSX FILE
            # 'product_name', 'date_of_changes', 'quantity_changes', 'price : at which sold', 'customer_name', 'vendor','purchase_or_cell'
            customer_name = str(input("Enter name of customer : "))
            movement_arr = [cell[0].value, "05-07-2023", qty, cell[6].value, customer_name, cell[5].value, 'Sell']
            a = 0
            for o in movement_arr:
                excel_functions[2][5].write(excel_functions[2][2],a,o)
                a += 1
            excel_functions[2][4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/inventory_movement.xlsx")

        if not flag:
            print(False)
    # -----------------------------------------------  SELL FUNC ---------------------------


    # -----------------------------------------------  PURCHASE UPDATE DATA FUNC ---------------------------
    def update_purchase(self):
        excel_functions = self.excel_func()

        print("inside")
        obj = Product()
        x = obj.getInput()
        # print(x)
        # update in 2 files : purchase.xls and movement.xls
        # PURCHASE : product_name, sku, quantity, purchase_price(for inventory), total = purchase_price * quantity, tax = 0
        # MOVEMENT : # 'product_name', 'date_of_changes', 'quantity_changes', 'price : at which sold', 'customer_name', 'vendor','purchase_or_cell'
        purchase_arr = [x[0],x[1],x[2],x[3],x[2]*x[3],0]
        movement_arr = [x[0],'05-07-2023',x[2], x[6], 'Inventory manager',x[5],'Purchase']
        count = 0
        for each in purchase_arr:
            excel_functions[3][5].write(excel_functions[3][2],count,each)
            count += 1
        excel_functions[3][4].save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/purchase.xlsx")

        counter = 0
        for each_item in movement_arr:
            excel_functions[2][5].write(excel_functions[2][2], counter, each_item)
            counter += 1
        excel_functions[2][4].save(
            "/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/inventory_movement.xlsx")



    # -----------------------------------------------  PURCHASE UPDATE DATA FUNC ---------------------------


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