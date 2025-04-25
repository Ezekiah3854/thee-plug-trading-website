-- dbms -> postgresql
createdb crypto_plug;
psql crypto_plug;
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    fname VARCHAR(100),
    lname VARCHAR(100),
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    country VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS class(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
CREATE TABLE IF NOT EXISTS brokers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    refferal_link TEXT,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
-- CREATE USER IF NOT EXISTS 'admin_trader'@'localhost' IDENTIFIED BY '(PlugTrader2025)';
-- GRANT ALL PRIVILEGES ON crypto_plug.* TO 'admin_trader'@'localhost';
-- FLUSH PRIVILEGES;
-- end
