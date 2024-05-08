SELECT p.acc_case_id, psn_age, EXTRACT(YEAR FROM c.actual_dead_date) AS year, c.case_vehicle
FROM `stalwart-summer-413911.project_accident.personal_info` AS p
INNER JOIN `stalwart-summer-413911.project_accident.case_info` AS c
ON p.acc_case_id = c.acc_case_id
GROUP BY p.acc_case_id, psn_age, year, c.case_vehicle
