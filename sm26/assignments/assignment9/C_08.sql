CREATE TABLE IF NOT EXISTS customers(
    id int primary key,
    name varchar(20)
);

CREATE TABLE IF NOT EXISTS transactions(
    id int primary key,
    customer_id int,
    amount int,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO customers
(id, name)
VALUES
(1,'rahul'),
(2,'aman'),
(3,'neha'),
(4,'karan');

INSERT INTO transactions
(id, customer_id, amount)
VALUES
(1,1,500),
(2,1,300),
(3,2,400),
(4,3,700);

select c.id, c.name, t.id, t.amount
from customers c
left join transactions t
on c.id = t.customer_id;


select c.id, c.name, t.id, sum(t.amount)
from customers c
join transactions t
on c.id = t.customer_id
GROUP BY c.id, c.name
HAVING sum(t.amount) > (SELECT avg(t.amount) from transactions)
;