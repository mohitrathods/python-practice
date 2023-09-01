-- Retrieve all columns from the "categories" table.
-- SELECT * FROM production.categories

-- Select distinct values from the "brand_name" column in the "brands" table.
-- SELECT DISTINCT brand_name FROM production.brands

-- Calculate the average list price of products.
-- SELECT AVG(list_price) FROM production.products

-- Count the number of customers in the "customers" table.
-- SELECT COUNT(customer_id) FROM sales.customers

-- Filter orders with an order status of "Pending" from the "orders" table. 
-- (here status is in number format 1 to 4) so find for 2
-- SELECT order_status FROM sales.orders WHERE order_status = 1

-- Retrieve the first and last names of customers.
-- SELECT first_name, last_name FROM sales.customers

-- Find the maximum list price among products.
-- SELECT MAX(list_price) FROM production.products

-- Sort the products by model year in ascending order.
-- SELECT product_name, model_year FROM production.products ORDER BY model_year asc

-- Calculate the total quantity of items in the "order_items" table.
-- SELECT COUNT(quantity) FROM sales.order_items

-- Calculate the average discount applied to orders.
-- SELECT AVG(discount) FROM sales.order_items

-- Get the names of staff members who are currently active.
-- select * FROM sales.staffs

-- Count the number of products in each category.
-- select count(product_id) FRom production.products where category_id = 1 --2,3,4,5,6

-- Filter customers by zip code, excluding a specific value. (not including specific value)
-- select distinct(zip_code) from sales.customers

-- -------------------------------------------- JOINS
-- Retrieve the order details including the customer's first name and last name.
-- SELECT first_name, last_name, order_id 
-- FROM sales.customers
-- INNER JOIN sales.orders
-- ON sales.customers.customer_id = sales.orders.order_id

-- Question: Retrieve all stores and their associated staff members, including stores with no staff assigned.
-- SELECT store_name, staff_id, first_name, last_name
-- FROM sales.stores
-- LEFT JOIN
-- sales.staffs
-- ON sales.stores.store_id = sales.staffs.store_id



-- A = staffs B = stores

-- Question: Retrieve all staff members and their associated store names, including staff members with no assigned store.
-- SELECT * from sales.staffs
-- UPDATE sales.staffs
-- SET store_id = NULL
-- WHERE store_id IN (0)
-- SELECT first_name, last_name, store_name, staff_id
-- FROM sales.staffs
-- LEFT JOIN sales.stores
-- ON sales.staffs.store_id = sales.stores.store_id

-- Question: Retrieve the details of staff members and their respective managers.
-- All staff members
-- SELECt bb.manager_id, aa.first_name, bb.staff_id, bb.first_name   
-- from sales.staff_two aa
-- full outer join sales.staff_two bb
-- on bb.manager_id = aa.staff_id
-- where bb.manager_id NOTNULL or aa.manager_id ISNULL 

-- Question: Retrieve all staff members and their associated store names, including staff members and stores with no association.
-- SELECT stf.staff_id, stf.first_name, str.store_name
-- FROM sales.staffs stf
-- LEFT JOIN sales.stores str
-- ON stf.store_id = str.store_id

-- Question: Retrieve the Cartesian product of staff members and products. : CARTESIAN JOIN
-- SELECT sales.staffs.staff_id, sales.staffs.first_name, production.products.product_id, production.products.product_name
-- FROM sales.staffs
-- CROSS JOIN production.products
--------------------------------------------

-- same category products in group CATEGORY NAME
-- SELECT category.category_name, STRING_AGG(product.product_name, ',	') as category_wise_products
-- FROM production.categories category
-- INNER JOIN production.products product
-- ON category.category_id = product.category_id
-- group by (category.category_name)
-- order by category.category_name asc

-- same category same brand products in group [] CATEGORY NAME, count of brand_id <> BRAND NAME
-- SELECT product.product_name, category.category_name, brand.brand_name
-- FROM production.products product
-- LEFT JOIN production.categories category
-- On product.category_id = category.category_id
-- LEFT JOIN production.brands brand
-- On product.brand_id = brand.brand_id
-- WHERE product.brand_id = product.category_id

-- SELECT STRING_AGG(product.brand_id::character varying, ' , ') as row_of_brands, STRING_AGG(product.product_name, ' , ') as row_of_products
-- FROM production.categories category
-- INNER JOIN production.products product
-- ON category.category_id = product.category_id
-- GROUP BY (product.category_id)

-- count of orders for each state 
-- SELECT customer.state as state, COUNT(o.order_id) as total_orders
-- FROM sales.orders o
-- INNER JOIN sales.customers customer
-- ON customer.customer_id = o.customer_id
-- GROUP BY (customer.state)


-- get list of products with 0 quantity
-- SELECT stock.product_id, stock.quantity, product.product_name
-- FROM production.products product
-- INNER JOIN production.stocks stock
-- ON product.product_id = stock.product_id
-- WHERE stock.quantity = 0

-- EXTRa and BF situation query
-- select sum(stock.quantity), product.product_name, product.product_Id
-- from production.products product
-- inner join production.stocks stock
-- On product.product_id = stock.product_id
-- group by (product.product_id)
-- order by product.product_id

-- list of manager from staff
-- SELECT DIStinct(aa.manager_id), bb.first_name
-- FROM sales.staffs aa
-- JOIN sales.staffs bb
-- ON aa.manager_id = bb.staff_id
-- ORDER BY aa.manager_id ASC
-- if aa>manager_id = bb>staff_id > print name from bb table with compared staff_id

-------------------------------------------------------------------------------------------------------

-- CREATE TABLE sale_order (
-- 	id SERIAL,
-- 	customer_id int,
-- 	order_date DATE,
-- 	order_status varchar(20),
-- 	FOREIGN KEY (customer_id) REFERENCES sales.customers(customer_id)
-- )

-- CREATE TABLE sale_order_line (
-- 	id SERIAL PRIMARY KEY,
-- 	order_id int,
-- 	product_id int,
-- 	sale_price int,
-- 	quantity int,
-- 	total int,
-- 	FOREIGN KEY (order_id) REFERENCES sales.orders(order_id),
-- 	FOREIGN KEY (product_id) REFERENCES production.products(product_id)
-- ) 

------------------------------------------ SQL JOINS > w3resource
-- get customername id where customer city = store city
-- SELECT c.customer_id, c.first_name, c.city, s.city
-- from sales.customers c, sales.stores s
-- where c.city = s.city

-- get customer same city count
-- SELECT COUNT(c.customer_id), city 
-- FROM sales.customers c
-- GROUP BY (city)

-- get same name customers count
-- SELECT COUNT(c.customer_id) AS counter, c.first_name
-- FROM sales.customers c
-- GROUP BY(c.first_name)

-- IN ABOVE print only if count is > 2
-- SELECT COUNT(c.customer_id) AS counter, c.first_name
-- FROM sales.customers c
-- GROUP BY(c.first_name)
-- HAVING COUNT(c.customer_id) > 2

-- get orders with same customer_id
-- SELECT COUNT(order_id), customer_id
-- FROM sales.orders
-- GROUP BY (customer_id)

-- IN ABOVE > get customer names, customer phones too
-- SELECT COUNT(o.order_id), o.customer_id, c.first_name,c.phone
-- FROM sales.orders o
-- INNER JOIN sales.customers c
-- ON o.customer_id = c.customer_id
-- WHERE c.phone is	 null
-- GROUP BY (o.customer_id, c.first_name, c.phone)

-- get orders where order amount is between 500 and 0.9k
-- return order_id, amount, customer_name, city of customer
-- order_line_id
-- SELECT so.order_name, so.id, c.first_name, c.city, sol.sale_price
-- FROM sale_order so
-- 	INNER JOIN sales.customers c ON c.customer_id = so.customer_id
-- 	INNER JOIN sale_order_line sol ON so.id = sol.order_id
-- WHERE sol.sale_price > 500 and sol.sale_price < 900

-- get customer id, customer name, where order status is draft
-- SELECT Count(c.customer_id), c.first_name, o.order_status
-- FROM sales.customers c, sale_order o
-- WHERE c.customer_id = o.customer_id and o.order_status = 'conform'
-- group by (c.first_name, o.order_Status)

-- salesmans who recieved commission > 12%
-- return cname, ccity, salesman, commission
-- SELECT a.cust_name, a.city, b.salesman_id, b.name
-- FROM customer a, salesman b
-- WHERE b.commission >= 0.12

-- locate salespeople who dont live in same city where customers live AND recieved commission of > 12%
-- return cname, ccity, salesman, scity, commission
-- SELECT a.cust_name, a.city, b.salesman_id, b.city, b.commission
-- FROM customer a
-- INNER JOIN salesman b
-- ON a.salesman_id = b.salesman_id
-- WHERE a.city != b.city and b.commission>0.12


-- ind the details of an order. Return ord_no, ord_date, purch_amt, Customer Name, grade, Salesman, commission.
-- SELECT o.ord_no, o.ord_date, o.purch_amt, c.cust_name, c.grade, s.salesman, s.commission
-- FROM orders o
-- 	INNER JOIN customer c ON o.customer_id = c.customer_id
-- 	INNER JOIN salesman s ON o.salesman_id = s.salesman_id

-- display the customer name, customer city, grade, salesman, salesman city
-- The results should be sorted by ascending customer_id.
-- SELECT c.cust_name, c.city, c.grade, s.name, s.city
-- FROM customer c
-- LEFT JOIN salesman s
-- ON c.salesman_id = s.salesman_id
-- ORDER by c.customer_id;

-- custoemrs with grade less than 300
-- return cname, ccity, cgrade, salesman, salesmancity > order by asc cus_id
-- SELECT c.cust_name, c.city, c.grade, s.name, s.city
-- FROM customer c
-- LEFT JOIN salesman s
-- ON c.salesman_id = s.salesman_id
-- WHERE c.grade < 300
-- ORDER BY c.customer_id asc

-- MAKE A REPORT : customer_name, city, order no, order date, order amount (in asc order according to order date)
-- in ascending order according to the order date 
-- to determine whether any of the existing customers have placed an order or not.
-- SELEct c.cust_name, c.city, o.order_no, o.ord_date, o.purch_amt
-- FROm customers c 
-- LEFT JOIN orders o
-- On c.customer_id = o.customer_id
-- ORDER BY o.order_date ASC


-- report with cust_name, city, ord_no, ord_date, salesman(name, commission)
-- if any of the existing customers have not placed orders
-- OR >> if they have placed orders through their salesman or by themselves
-- SELECT c.cust_name, c.city, o.ord_no, o.ord_date, s.name, s.commission
-- FROM orders o
-- LEFT JOIN customer c
-- ON c.customer_id = o.customer_id
-- LEFT JOIN salesman s
-- ON o.salesman_id = s.salesman_id
 
--  SOL NO 15
-- get customers who puts one or more orders
-- cname, city, orderno, order date, purchase amount
-- SELECT c.name, c.city, o.ord_no, o.ord_date, o.purch_amt
-- FROM customer c
-- RIGHT JOIN orders o
-- ON c.customer_id = o.customer_id

------------------------------- 9.20. Aggregate Functions --------------------------------------------

-- SELECT * FROM sales.customers;

-- COALESCE
-- SELECT COALESCE(phone,'phone not provided') FROM sales.customers

-- NUllIF()
-- select * from sales.orders
-- SELECT 10 / NULLIF(0,0) as div;
-- SELECT order_id, order_status, NULLIF(order_status, 0) from sales.orders
-- here where order_status is 0 nullif will return null but with colescade return some specific value

-- JSON AND THINGS -----------------------
-- select * from sale_order;
-- CREATE TABLE json_table(
-- 	json_id SERIAL not null PRIMARY KEY,
-- 	info json NOT NULL
-- )
-- SELECT * FROM json_table;
-- INSERT INTO json_table (info)
-- VALUES(
-- 	'{"customer" : "A rajuu....", "items"  : {"product" : "suzuki hayabusa", "quantity" : 1}}'
-- )
-- SELECT * FROM json_table;

-- UPDATE json_table
-- SET info = '{}'
-- WHERE json_id = 8

-- -> and ->> functions -> as string and ->> as text
-- SELECT info -> 'items' -> 'product' FROM json_table

-- ROW_NUMBER
-- select * from sales.customers

-------------------------- *---------- CUSTOM FUNCTIONS ---------*
-- CREATE FUNCTION inc(val integer) RETURNS integer AS $$
-- BEGIN
-- RETURN val + 1;
-- END; $$
-- LANGUAGE PLPGSQL;
-- SELECT inc(10)

-- CREATE FUNCTION sales.netSale(
--     quantity INT,
--     list_price DEC(10,2),
--     discount DEC(4,2)
-- )
-- RETURNS DEC(10,2) AS $$
-- BEGIN
--     RETURN quantity * list_price * (1 - discount);
-- END;
-- $$ LANGUAGE PLPGSQL;
-- SELECT netSale

-----------------------------------------
-- CREATE OR REPLACE FUNCTION func(varchar, integer, integer)
-- RETURNS varchar
-- AS
-- $$
-- DECLARE parameter_one ALIAS FOR $1;
-- DECLARE	param_a ALIAS FOR $2;
-- DECLARE param_b ALIAS FOR $3;
-- BEGIN
-- 	RETURN param_a*param_b;
-- END;
-- $$
-- LANGUAGE PLPGSQL;

-- SELECT func('software',5,4)

-- -----------------------------------------
-- CREATE OR REPLACE FUNCTION fnMakeFull(firstName varchar, lastName varchar)
-- RETURNS varchar
-- AS
-- $$
-- BEGIN
-- 	IF firstName IS NULL AND lastName IS NULL THEN
-- 		RETURN NULL;
-- 	ELSIF firstName IS NULL AND lastName IS NOT NULL THEN
-- 		RETURN lastName;
-- 	ELSIF firstName IS NOT NULL AND lastName IS NULL THEN
-- 		RETURN firstName;
-- 	ELSE
-- 		RETURN concat_ws(firstName, lastName, ' G.O.A.T. ');
-- 	END IF;
-- END;	
-- $$
-- LANGUAGE PLPGSQL;


-- SELECT fnMakeFull('Meet','Rathod')

-------------------------------------- PARAMETER TYPES
-- parameter type{in* | out | inout | VARIADIC**} *default, **variable no of arguments
-- CREATE OR REPLACE FUNCTION swapFun(inout num1 int, inout num2 int)
-- AS
-- $$
-- BEGIN
-- 	SELECT num1,num2 into num2, num1;
-- END;
-- $$
-- LANGUAGE PLPGSQL;

-- SELECT swapFun(1,2)

-- PASS AN ARRAY TO A FUNCTION
CREATE or REPLACE FUNCTION fnArray(numeric[])
RETURNS numeric 
AS
$$
BEGIN
END;
$$
LANGUAGE PLPGSQL;