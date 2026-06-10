CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    category VARCHAR(50) NOT NULL,
    amount INT NOT NULL
);