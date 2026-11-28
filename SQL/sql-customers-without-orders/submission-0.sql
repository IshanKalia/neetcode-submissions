-- Write your query below

--Write a query to find all customers who have never placed ann order. Return the customer names

SELECT customers.name FROM customers FULL JOIN orders ON customers.id = orders.customer_id WHERE orders.id is NULL;