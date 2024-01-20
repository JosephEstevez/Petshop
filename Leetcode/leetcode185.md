# Ecercício 185 leetcode (SQL - Difícil)

## Seleciona as tabelas

SELECT
d.name AS Department,
e.name AS Employee,
e.salary
FROM
Employee e
JOIN Department d ON e.departmentId = d.id

## Seleciona os funcionários com salários iguais ou maiores aos 3 maiores salários em cada departamento

WHERE
e.salary >= (
SELECT DISTINCT MAX(salary)
FROM Employee e2
WHERE e2.departmentId = e.departmentId
)
OR e.salary >= (
SELECT DISTINCT MAX(salary)
FROM Employee e3
WHERE e3.departmentId = e.departmentId
AND e3.salary < (
SELECT DISTINCT MAX(salary)
FROM Employee e4
WHERE e4.departmentId = e.departmentId
)
)
OR e.salary >= (
SELECT DISTINCT MAX(salary)
FROM Employee e5
WHERE e5.departmentId = e.departmentId
AND e5.salary < (
SELECT DISTINCT MAX(salary)
FROM Employee e6
WHERE e6.departmentId = e.departmentId
AND e6.salary < (
SELECT DISTINCT MAX(salary)
FROM Employee e7
WHERE e7.departmentId = e.departmentId
)
)
)
