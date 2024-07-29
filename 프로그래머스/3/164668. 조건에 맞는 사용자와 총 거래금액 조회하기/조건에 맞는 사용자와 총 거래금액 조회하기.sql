SELECT
    user_id,
    nickname,
    SUM(price) AS total_sales
FROM used_goods_board ugb
JOIN used_goods_user ugu
ON ugb.writer_id = ugu.user_id
WHERE status = 'DONE'
GROUP BY user_id
HAVING SUM(price) >= 700000
ORDER BY total_sales;