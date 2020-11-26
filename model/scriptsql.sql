SET
  NAMES utf8;
CREATE TABLE Product (
    id SMALLINT AUTO_INCREMENT,
    product_name VARCHAR NOT NULL,
    shop VARCHAR NOT NULL,
    origin VARCHAR NOT NULL,
    substitute SMALLINT,
    PRIMARY KEY(id),
    FOREIGN KEY (substitute) REFERENCES Product(id)
  );
CREATE TABLE Category (
    id SMALLINT AUTO_INCREMENT NOT NULL,
    cat_name varchar NOT NULL,
    PRIMARY KEY(id),
  );
CREATE TABLE Catprod (
    id_cat SMALLINT NOT NULL,
    id_prod SMALLINT NOT NULL,
    FOREIGN KEY (id_cat) REFERENCES Category(id)
  ) FOREIGN KEY (id_prod) REFERENCES Product(id)
);
CREATE TABLE Nutriscore(
  id SMALLINT AUTO_INCREMENT NOT NULL,
  nutri_value VARCHAR NOT NULL,
  PRIMARY KEY(id),
);