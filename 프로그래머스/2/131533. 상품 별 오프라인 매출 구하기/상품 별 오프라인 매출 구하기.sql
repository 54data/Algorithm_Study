WITH sales AS (
    SELECT 
        product_code, 
        SUM(sales_amount) AS total
    FROM product p
    INNER JOIN offline_sale os
    ON p.product_id = os.product_id
    GROUP BY product_code
)

SELECT
    s.product_code, 
    s.total * p.price AS sales
FROM sales s
INNER JOIN product p
ON s.product_code = p.product_code
ORDER BY sales DESC, product_code;
