SET
  NAMES utf8;
DROP DATABASE IF EXISTS product;
CREATE DATABASE product;
USE product;
CREATE TABLE Product (
    id SMALLINT AUTO_INCREMENT,
    product_name VARCHAR(200) NOT NULL,
    shop VARCHAR(200) NOT NULL,
    origin VARCHAR(200) NOT NULL,
    substitute SMALLINT,
    PRIMARY KEY(id),
    FOREIGN KEY (substitute) REFERENCES Product(id)
  );
CREATE TABLE Category (
    id SMALLINT AUTO_INCREMENT,
    cat_name VARCHAR (200) NOT NULL,
    PRIMARY KEY(id)
  );
CREATE TABLE Catprod (
    id_cat SMALLINT NOT NULL,
    id_prod SMALLINT NOT NULL,
    FOREIGN KEY (id_cat) REFERENCES Category(id),
    FOREIGN KEY (id_prod) REFERENCES Product(id)
  );
CREATE TABLE Nutriscore(
    id SMALLINT AUTO_INCREMENT NOT NULL,
    nutri_value VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
  );