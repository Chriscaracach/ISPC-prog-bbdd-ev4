CREATE TABLE MaquinasCremallera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    cintas_tejidas INT DEFAULT 0,
    cremalleras INT DEFAULT 0,
    cremalleras_teñidas INT DEFAULT 0,
    cremalleras_empaquetadas INT DEFAULT 0
);

CREATE TABLE HistorialProduccion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    maquina_id INT, 
    cantidad_cintas_tejidas INT,
    cantidad_cremalleras_fabricadas INT,
    color_teñido VARCHAR(50),
    cantidad_cremalleras_teñidas INT,
    cantidad_cremalleras_empaquetadas INT,
    fecha_produccion VARCHAR(30),
    FOREIGN KEY (maquina_id) REFERENCES MaquinasCremallera(id)
);
