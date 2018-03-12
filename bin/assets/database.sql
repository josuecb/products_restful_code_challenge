CREATE DATABASE IF NOT EXISTS fluent_city;
USE fluent_city;
CREATE TABLE IF NOT EXISTS products (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250) NOT NULL UNIQUE, price DOUBLE NOT NULL, timestamp TEXT) DEFAULT CHAR SET utf8 ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS category (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250) NOT NULL UNIQUE) DEFAULT CHAR SET utf8 ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS products_by_category (product_id  INT UNSIGNED NOT NULL, category_id INT UNSIGNED NOT NULL, FOREIGN KEY (product_id) REFERENCES products (id), FOREIGN KEY (category_id) REFERENCES category (id)) DEFAULT CHAR SET utf8 ENGINE = InnoDB;