# Write your MySQL query statement below
WITH temp AS 
(
SELECT buyer_id AS bid, COUNT(order_date) AS c
FROM Orders
WHERE YEAR(order_date) = 2019
GROUP BY buyer_id
)

SELECT u.user_id AS buyer_id, u.join_date AS join_date, COALESCE(t.c, 0) AS orders_in_2019
FROM Users u
LEFT JOIN temp t
ON u.user_id = t.bid