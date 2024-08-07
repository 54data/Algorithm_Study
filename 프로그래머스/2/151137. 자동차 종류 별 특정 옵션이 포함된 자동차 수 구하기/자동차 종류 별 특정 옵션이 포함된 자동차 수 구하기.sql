SELECT 
    car_type, 
    count(*) AS cars
FROM car_rental_company_car
WHERE REGEXP_LIKE(options, '통풍시트|열선시트|가죽시트')
GROUP BY car_type
ORDER BY 1;