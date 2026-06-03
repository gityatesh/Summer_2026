CREATE TABLE employees(
    id INT PRIMARY KEY,
    name VARCHAR(15),
    salary INT,
    department VARCHAR(10)
);

INSERT INTO employees
(id, name, salary, department)
VALUES
(1, 'Rahul', 50000, 'IT'),
(2, 'Aman', 70000, 'HR'),
(3, 'Neha', 60000, 'IT'),
(4, 'Priya', 80000, 'Finance'),
(5, 'Rohit', 65000, 'HR'),
(6, 'Karan', 55000, 'IT'),
(7, 'Simran', 90000, 'Finance'),
(8, 'Arjun', 72000, 'Sales'),
(9, 'Mehak', 68000, 'HR'),
(10, 'Varun', 75000, 'Sales');

-- ques13
SELECT * FROM employees
WHERE salary BETWEEN 50000 and 70000;

--ques14
SELECT * FROM employees
WHERE department NOT IN ('IT');

--ques15
SELECT * FROM employees
ORDER BY name;

--ques16
SELECT count(id) FROM employees;

--ques17
SELECT department, count(id) FROM employees
GROUP BY department;

--ques18
SELECT * FROM employees
ORDER BY salary in DESC
LIMIT 1 OFFSET 1;

--ques19
SELECT department, avg(salary) AS avg_salary FROM employees
GROUP BY department;

--ques20
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 3;
