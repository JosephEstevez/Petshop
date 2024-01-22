# Ecercício 185 leetcode - Department Top Three Salaries (SQL - Difícil)

## Seleciona as tabelas
```
SELECT d.Name AS Department, a.Name AS Employee, a.Salary AS Salary FROM
(
SELECT a.*, DENSE_RANK() over (PARTITION BY DepartmentId ORDER BY Departmentid, Salary DESC) AS DeptPayRank 
FROM Employee a 
) a 
JOIN Department d
ON a.DepartmentId = d.Id 
WHERE DeptPayRank <=3

```
## Cria um rank de todos os pagamentos
```
SELECT a.*, DENSE_RANK() over (PARTITION BY DepartmentId ORDER BY Departmentid, Salary DESC) AS DeptPayRank 
FROM Employee a 
) a 
```
## Limita a busca para que apareçam apenas os 3 maiores pagamentos de cada departamento
```
JOIN Department d
ON a.DepartmentId = d.Id 
WHERE DeptPayRank <=3
```
## Código completo
```
SELECT d.Name AS Department, a.Name AS Employee, a.Salary FROM
(
SELECT a.*, DENSE_RANK() over (PARTITION BY DepartmentId ORDER BY Departmentid, Salary DESC) AS DeptPayRank 
FROM Employee a 
) a 
JOIN Department d
ON a.DepartmentId = d.Id 
WHERE DeptPayRank <=3
```
