-- avg sales price, average total
-- SELECT ROUND(AVG(sale_price),3) from sale_order_line
-- SELECT ROUND(AVG(total),2) FROM sale_order_line

-- get product id where orderstatus = done --
-- SELECT b.product_id, a.order_name
-- FROM sale_order a
-- inner JOIN sale_order_line b
-- ON a.id = b.order_id
-- WHERE a.order_status = 'done'

-- same order count on order_id --
-- SELECT b.order_id, a.order_name, ROUND(avg(b.total),2) as "Avg total", ROUND(avg(b.quantity)) as avg_quantity
-- FROM sale_order a
-- INNER JOIN sale_order_line b
-- ON a.id = b.order_id
-- -- where b.order_id = 111
-- group by (b.order_id, a.order_name)
-- order by b.order_id
SELECT * FROM sales.customers;
-- 



SELECT first_name, COUNT(customer_id) as counter
FROM sales.customers
group by (first_name)