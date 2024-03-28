SELECT
    pt_name,
    pt_no,
    gend_cd,
    age,
    CASE
        WHEN tlno IS NULL THEN 'NONE'
        ELSE tlno
    END AS tlno
FROM 
    patient
WHERE 
    gend_cd = 'W'
    AND age <= 12
ORDER BY
    age DESC,
    pt_name ASC