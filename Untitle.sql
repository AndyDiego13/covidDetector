CREATE VIEW nivel_oxigeno AS 
SELECT idPersona, nivelOxigeno, hora
FROM controlOximetro;

CREATE VIEW nivel_pulso AS
SELECT idPersona, pulso, hora
FROM controlPulso;

CREATE VIEW historial AS
SELECT idPersona, idHistorial, edadRiesgo, dificultadRespiracion
FROM historial;

CREATE VIEW personas AS
SELECT idPersona, edad, nombre
FROM persona;