# Write your MySQL query statement below
WITH first_login AS
    (
        SELECT player_id AS player_id, MIN(event_date) AS first
        FROM Activity 
        GROUP BY player_id
    )


SELECT ROUND(COUNT(f.player_id)/(SELECT COUNT(player_id) FROM first_login), 2) AS fraction
FROM Activity a, first_login f
WHERE DATEDIFF(a.event_date, f.first) = 1 AND a.player_id = f.player_id