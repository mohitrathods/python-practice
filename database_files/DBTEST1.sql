CREATE TABLE production.categories (
	category_id INT SERIAL PRIMARY KEY,
	category_name VARCHAR(255)
)

CREATE TABLE production.brands (
	brand_id INT SERIAL PRIMARY KEY,
	brand_name VARCHAR(255)
)

CREATE TABLE production.products (
	product_id INT SERIAL PRIMARY KEY,
	product_name VARCHAR (255),
	brand_id INT,
	category_id INT,
	model_year INT,
	list_price DECIMAL,
)

CREATE TABLE sales.customers (
	customer_id INT SERIAL PRIMARY KEY,
	first_name VARCHAR (255),
	last_name VARCHAR (255),
	phone VARCHAR (25),
	email VARCHAR (255),
	street VARCHAR (255),
	city VARCHAR (50),
	state VARCHAR (25),
	zip_code VARCHAR (5)
);

CREATE TABLE sales.stores (
	store_id INT SERIAL PRIMARY KEY,
	store_name VARCHAR (255),
	phone VARCHAR (25),
	email VARCHAR (255),
	street VARCHAR (255),
	city VARCHAR (255),
	state VARCHAR (10),
	zip_code VARCHAR (5)
);

CREATE TABLE sales.staffs (
	staff_id INT SERIAL PRIMARY KEY,
	first_name VARCHAR (50),
	last_name VARCHAR (50),
	email VARCHAR (255),
	phone VARCHAR (25),
	active tinyint,
	store_id INT,
	manager_id INT,
);

CREATE TABLE sales.orders (
	order_id INT SERIAL PRIMARY KEY,
	customer_id INT,
	order_status int,
	-- Order status: 1 = Pending; 2 = Processing; 3 = Rejected; 4 = Completed
	order_date DATE,
	required_date DATE,
	shipped_date DATE,
	store_id INT,
	staff_id INT,
);

CREATE TABLE sales.order_items (
	order_id INT,
	item_id INT,
	product_id INT,
	quantity INT,
	list_price DECIMAL,
	discount DECIMAL.
);

CREATE TABLE production.stocks (
	store_id INT,
	product_id INT,
	quantity INT,
);