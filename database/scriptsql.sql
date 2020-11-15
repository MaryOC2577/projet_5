SET
  NAMES utf8;
CREATE TABLE Aliment (
    id SMALLINT AUTO_INCREMENT,
    nom VARCHAR,
    magasin VARCHAR,
    provenance VARCHAR,
    substitut SMALLINT,
    CONSTRAINT fk_substitut FOREIGN KEY REFERENCES Aliment(id),
    CONSTRAINT fk_categorie FOREIGN KEY REFERENCES Categorie(id),
    CONSTRAINT fk_nutri_score FOREIGN KEY REFERENCES Nutri_score(id),
    PRIMARY KEY(id),
  );
CREATE TABLE Categorie (
    id SMALLINT AUTO_INCREMENT,
    nom varchar,
    PRIMARY KEY(id),
  );
CREATE TABLE Nutri_score(
    id SMALLINT AUTO_INCREMENT,
    valeur VARCHAR,
    PRIMARY KEY(id),
  );