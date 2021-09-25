UPDATE rdata_with_constraint
set moment = '2020-03-01'
WHERE id = 1 or id = 2;

SELECT * FROM rdata_with_constraint;