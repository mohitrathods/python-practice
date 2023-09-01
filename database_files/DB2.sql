-- CREATE TABLE socialdata(
-- 	personid int,
-- 	affairs int,
-- 	xender varchar(255),
-- 	age int,
-- 	marriedyears varchar(255),
-- 	children varchar(255),
-- 	religious int,
-- 	education int,
-- 	occupation int,
-- 	rating int
-- )

-- copy socialdata from '/home/setu/Downloads/9cols_Affairs.csv' with csv header

-- ALTER TABLE socialdata
-- ALTER COLUMN marriedyears type float using (marriedyears::float)

-- TOTAL 601 RECORDS
select * from socialdata

