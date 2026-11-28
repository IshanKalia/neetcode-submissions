-- Write your query below

--Write a query to find all customers who had positive revenue in the year 2020. Return only the customer_id column. 

SELECT customer_id FROM customers WHERE (revenue > 0) AND (year = 2020);