-- SENTENCIAS CRUD - CREATE(INSERT) - READ(SELECT) - UPDATE - DELETE
SELECT * FROM personas;
INSERT INTO personas(nombre, apellido, edad) VALUES ('Carmen', 'Requesens', 61);
INSERT INTO personas(nombre, apellido, edad) VALUES ('Ruben', 'Lliberos', 36);
UPDATE personas SET nombre = 'Carmen2', apellido = 'Requesens2' WHERE id = 1;
DELETE FROM personas WHERE id = 6;