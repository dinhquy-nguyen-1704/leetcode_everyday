# Write your MySQL query statement below
WITH max_de AS 
(
SELECT DISTINCT d.id AS de, d.name AS name, MAX(e.salary) OVER(PARTITION BY d.id) AS m
FROM Employee e JOIN Department d
ON e.departmentId = d.id
)

SELECT m.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e JOIN max_de m
ON e.departmentId = m.de
WHERE e.departmentId = m.de AND e.salary = m.m
