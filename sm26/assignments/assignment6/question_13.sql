CREATE TABLE departments (
    id INT primary key,
    department_name VARCHAR(50)
);

INSERT INTO departments (id, department_name) VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');


CREATE TABLE employees (
    id INT primary key,
    name VARCHAR(50),
    department_id INT,
    foreign key (department_id) references departments(id)
);

INSERT INTO employees (id, name, department_id) VALUES
(1, 'Rahul', 1),
(2, 'Aman', 2),
(3, 'Neha', 1),
(4, 'Priya', 3),
(5, 'Karan', 1);


--question13
select e.id, e.name, e.department_id, d.department_name from employees e
join departments d
ON e.department_id = d.id;

--question14
select d.department_name, count(e.id) as employee_count from employees e
join departments d
on e.department_id = d.id
group by d.id;

--question15
select d.department_name, count(e.id) as employee_count from employees e
join departments d
on e.department_id = d.id
group by d.id
limit 1;