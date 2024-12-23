# Medicamentos
Este projeto buscar selecionar o medicamento mais adequado, com base na maximização da eficácia, analisando todos os sintomas do paciente.


## Passo


1. Deve perguntar ao cliente todos os sintomas, e realizar uma analise mais profunda através de equipamentos
2. Pesquisar o medicamento, que maximiza a "cura" dos sintomas


## Banco de dados

medicamento
+ id
+ nome


sintomas
+ id
+ nome

medicamento_eficacia_sintoma
+ id
+ porcentagem


## SQL

```sql

CREATE TABLE medicamento(
    id long AUTO INCREMENT PRIMARY KEY,
    nome varchar(180)
);

CREATE TABLE sintoma(
    id long AUTO INCREMENT PRIMARY KEY,
    nome varchar(180)
);

CREATE TABLE medicamento_eficacia_sintoma(
    id long AUTO INCREMENT PRIMARY KEY,
    idMedicamento long,
    idSintoma long,
    porcentagem decimal,
  	FOREIGN KEY (idMedicamento) REFERENCES medicamento(id) ON DELETE CASCADE,
  	FOREIGN KEY (idSintoma) REFERENCES sintoma(id) ON DELETE CASCADE
);

```

Dados de teste

```sql
-- Tabela medicamento
INSERT INTO medicamento (id, nome) VALUES (1, 'Paracetamol');
INSERT INTO medicamento (id, nome) VALUES (2, 'Ibuprofeno');
INSERT INTO medicamento (id, nome) VALUES (3, 'Amoxicilina');

-- Tabela sintoma
INSERT INTO sintoma (id, nome) VALUES (1, 'Dor de Cabeça');
INSERT INTO sintoma (id, nome) VALUES (2, 'Febre');
INSERT INTO sintoma (id, nome) VALUES (3, 'Tosse');

-- Tabela medicamento_eficacia_sintoma
INSERT INTO medicamento_eficacia_sintoma (id, idMedicamento, idSintoma, porcentagem) VALUES (1, 1, 1, 0.95);
INSERT INTO medicamento_eficacia_sintoma (id, idMedicamento, idSintoma, porcentagem) VALUES (2, 1, 2, 0.80);
INSERT INTO medicamento_eficacia_sintoma (id, idMedicamento, idSintoma, porcentagem) VALUES (3, 2, 1, 0.85);
INSERT INTO medicamento_eficacia_sintoma (id, idMedicamento, idSintoma, porcentagem) VALUES (4, 2, 2, 0.90);
INSERT INTO medicamento_eficacia_sintoma (id, idMedicamento, idSintoma, porcentagem) VALUES (5, 3, 3, 0.75);

```

Busca pelos medicamentos que tratam o sintoma

```sql

SELECT id, nome FROM sintoma;

-- IN(1, 2)
SELECT id, idMedicamento, idSintoma, porcentagem
    FROM medicamento_eficacia_sintoma
    WHERE idSintoma IN :idSintoma;
```