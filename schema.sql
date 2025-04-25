-- dbms -> mysql
CREATE DATABASE IF NOT EXISTS crypto_plug;
USE crypto_plug;
CREATE TABLE IF NOT EXISTS user(
    id INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(100),
    lname VARCHAR(100),
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    country VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS class(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);
CREATE TABLE IF NOT EXISTS brokers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    refferal_link TEXT,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);
CREATE USER IF NOT EXISTS 'admin_trader'@'localhost' IDENTIFIED BY '(PlugTrader2025)';
GRANT ALL PRIVILEGES ON crypto_plug.* TO 'admin_trader'@'localhost';
FLUSH PRIVILEGES;
-- end
