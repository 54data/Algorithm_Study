SELECT
    count(user_id) AS users
FROM 
    user_info
WHERE 
    age IS NULL