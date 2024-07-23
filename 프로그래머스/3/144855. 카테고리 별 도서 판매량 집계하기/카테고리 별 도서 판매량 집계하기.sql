SELECT
    b.category,
    SUM(bs.sales) AS total_sales
FROM book b
INNER JOIN book_sales bs
ON b.book_id = bs.book_id
WHERE TO_CHAR(bs.sales_date, 'YYYY-MM') = '2022-01'
GROUP BY b.category
ORDER BY b.category;