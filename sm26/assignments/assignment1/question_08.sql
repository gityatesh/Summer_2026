CREATE TABLE employees(
    id INT PRIMARY KEY,
    name VARCHAR(20),
    salary INT,
    department VARCHAR(10)
);

INSERT INTO employees
(id, name, salary, department)
VALUES
(1,'a',50000,'it'),
(2,'b',70000, 'hr'),
(3,'c',60000, 'it');

SELECT*FROM employees;
SELECT max(salary) FROM employees;
SELECT department, count(id)
FROM employees
GROUP BY department;
