# Exercício 184 leetcode (SQL - Médio)

## Seleciona as tabelas

SELECT Department.name AS 'Department', Employee.name AS 'Employee', Employee.salary as 'Salary'
FROM Employee JOIN Department ON Employee.departmentId = Department.id

## encontra o funcionário com salário e departamento compatíveis ao maior salário de cada departamento

WHERE (Employee.departmentId, Employee.salary) IN
(

## seleciona o maior salário de cada departamento

SELECT departmentId, MAX(salary)
FROM Employee
GROUP BY departmentId
);
