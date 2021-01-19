SET
  NAMES utf8;
CREATE TABLE Nutriscore(
    id SMALLINT AUTO_INCREMENT NOT NULL,
    nutri_value VARCHAR(200) NOT NULL UNIQUE,
    PRIMARY KEY(id)
  );
CREATE TABLE Product (
    id SMALLINT AUTO_INCREMENT,
    product_name VARCHAR(200) NOT NULL UNIQUE,
    product_description VARCHAR(200) NOT NULL,
    shop VARCHAR(200) NOT NULL,
    substitute SMALLINT,
    nutri_id SMALLINT,
    product_url VARCHAR(200),
    PRIMARY KEY(id),
    FOREIGN KEY (substitute) REFERENCES Product(id),
    FOREIGN KEY (nutri_id) REFERENCES Nutriscore(id)
  );
CREATE TABLE Category (
    id SMALLINT AUTO_INCREMENT,
    cat_name VARCHAR (200) NOT NULL UNIQUE,
    PRIMARY KEY(id)
  );
CREATE TABLE Catprod (
    id_cat SMALLINT NOT NULL,
    id_prod SMALLINT NOT NULL,
    FOREIGN KEY (id_cat) REFERENCES Category(id),
    FOREIGN KEY (id_prod) REFERENCES Product(id)
  );