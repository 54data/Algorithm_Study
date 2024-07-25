SELECT DISTINCT(car.car_id)
FROM car_rental_company_car car
INNER JOIN car_rental_company_rental_history rent
ON car.car_id = rent.car_id
WHERE car.car_type = '세단'
AND TO_CHAR(rent.start_date, 'MM') = 10
ORDER BY car.car_id DESC;
