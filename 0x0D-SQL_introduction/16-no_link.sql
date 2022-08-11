-- Lists the number of records with the same score in the table second_table.
-- Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `name`
FROM `second_table`
GROUP BY `score`
ORDER BY `name` DESC;