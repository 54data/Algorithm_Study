SELECT 
    count(user_id) AS users
FROM 
    user_info
WHERE
    age BETWEEN 20 AND 29
    AND YEAR(joined) = 2021