-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;