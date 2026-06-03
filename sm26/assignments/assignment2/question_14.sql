CREATE TABLE IF NOT EXISTS employees(
    id INT PRIMARY KEY,
    name VARCHAR(20),
    salary INT,
    dept VARCHAR(10)
);

INSERT INTO employees
(id, name, salary, dept)
VALUES
(1, 'A', 50000, 'IT'),
(2, 'B', 70000, 'HR'),
(3, 'C', 60000, 'IT'),
(4, 'D', 80000, 'Sales');

SELECT dept, avg(salary)
FROM employees
GROUP BY dept;
