CREATE TABLE IF NOT EXISTS customers(
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS transactions(
    id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    category VARCHAR(50),
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);