CREATE DATABASE db_part;

USE db_apart;

CREATE TABLE apartamentos (
    id integer not null auto_increment,
    edificio varchar(100),
    statutos varchar(100),
    valor_aluguel varchar(100),
    locador varchar(100),
    PRIMARY KEY (id)
);


INSERT INTO apartamentos (edificio,statutos,valor_aluguel,locador) VALUES ('Rosas','disponivel','1500,00','Ana Moura');
INSERT INTO apartamentos (edificio,statutos,valor_aluguel,locador) VALUES ('Rosas','alugado','1200,00','Paulo da Rosa');
INSERT INTO apartamentos (edificio,statutos,valor_aluguel,locador) VALUES ('Rosas','disponivel','2300,00','Biopark');
INSERT INTO apartamentos (edificio,statutos,valor_aluguel,locador) VALUES ('Rosas','alugado','1300,00','Tatiana Gonçalves');
INSERT INTO apartamentos (edificio,statutos,valor_aluguel,locador) VALUES ('Rosas','disponivel','1500,00','Vivian Mares');

