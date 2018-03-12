# Creates the database for our project
# Our project needs a database for products
#   in our database we will have categories for our products
#   and prices for each product
#   so our costumer can see and buy maybe in the future.
#   costumer will not be added in this database but products only
CREATE DATABASE fluent_city;

CREATE TABLE IF NOT EXISTS products (
  # id will be unique for each product, it will be auto incrementing
  #   according we add more products to the table
  id        INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  # name also must be unique
  name      VARCHAR(250) NOT NULL UNIQUE,
  # price must be not null
  price     DOUBLE       NOT NULL,
  # time in case we need to know about it or registration of products
  timestamp TEXT
)
  DEFAULT CHAR SET utf8
  ENGINE = InnoDB;

# category is a table to hold different types of products,
# e.i: food, electronics, handmade, luxury, kitchen, etc.
CREATE TABLE IF NOT EXISTS category (
  id   INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL UNIQUE
)
  DEFAULT CHAR SET utf8
  ENGINE = InnoDB;

# relation table of products and categories
CREATE TABLE IF NOT EXISTS products_by_category (
  product_id  INT UNSIGNED NOT NULL,
  category_id INT UNSIGNED NOT NULL,
  FOREIGN KEY (product_id) REFERENCES products (id),
  FOREIGN KEY (category_id) REFERENCES category (id)
)
  DEFAULT CHAR SET utf8
  ENGINE = InnoDB;

