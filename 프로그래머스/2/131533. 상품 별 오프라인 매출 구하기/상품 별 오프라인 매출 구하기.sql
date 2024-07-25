SELECT
    p.product_code, 
    SUM(os.sales_amount * p.price) AS sales
FROM product p
INNER JOIN offline_sale os
ON p.product_id = os.product_id
GROUP BY p.product_code
ORDER BY sales DESC, product_code;