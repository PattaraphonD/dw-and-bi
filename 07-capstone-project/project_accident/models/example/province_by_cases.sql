SELECT c.case_province, c.case_district, COUNT(p.acc_case_id) AS num_accidents, EXTRACT(YEAR FROM c.actual_dead_date) AS year
FROM `stalwart-summer-413911.project_accident.personal_info` AS p
INNER JOIN `stalwart-summer-413911.project_accident.case_info` AS c
ON p.acc_case_id = c.acc_case_id
GROUP BY c.case_province, year, c.case_district

