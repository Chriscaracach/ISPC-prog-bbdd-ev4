-- Insertar datos en la tabla de máquinas
INSERT INTO MaquinasCremallera (nombre) VALUES ('Maquina 1');
INSERT INTO MaquinasCremallera (nombre) VALUES ('Maquina 2');
INSERT INTO MaquinasCremallera (nombre) VALUES ('Maquina Galpon');
INSERT INTO MaquinasCremallera (nombre) VALUES ('Maquina Frente Local');
INSERT INTO MaquinasCremallera (nombre) VALUES ('Maquina Fabrica');

-- Insertar datos en el historial de producción
INSERT INTO HistorialProduccion (
    maquina_id,
    cantidad_cintas_tejidas,
    cantidad_cremalleras_fabricadas,
    color_teñido,
    cantidad_cremalleras_teñidas,
    cantidad_cremalleras_empaquetadas,
    fecha_produccion
) VALUES (1, 100, 100, 'Rojo', 100, 100, CURRENT_DATE);
INSERT INTO HistorialProduccion (
    maquina_id,
    cantidad_cintas_tejidas,
    cantidad_cremalleras_fabricadas,
    color_teñido,
    cantidad_cremalleras_teñidas,
    cantidad_cremalleras_empaquetadas,
    fecha_produccion
) VALUES (3, 15, 12, 'Azul', 12, 12, CURRENT_DATE);
INSERT INTO HistorialProduccion (
    maquina_id,
    cantidad_cintas_tejidas,
    cantidad_cremalleras_fabricadas,
    color_teñido,
    cantidad_cremalleras_teñidas,
    cantidad_cremalleras_empaquetadas,
    fecha_produccion
) VALUES (4, 4, 4, 'Blanco', 4, 4, CURRENT_DATE);
INSERT INTO HistorialProduccion (
    maquina_id,
    cantidad_cintas_tejidas,
    cantidad_cremalleras_fabricadas,
    color_teñido,
    cantidad_cremalleras_teñidas,
    cantidad_cremalleras_empaquetadas,
    fecha_produccion
) VALUES (2, 15000, 15000, 'Verde', 15000, 15000, CURRENT_DATE);
INSERT INTO HistorialProduccion (
    maquina_id,
    cantidad_cintas_tejidas,
    cantidad_cremalleras_fabricadas,
    color_teñido,
    cantidad_cremalleras_teñidas,
    cantidad_cremalleras_empaquetadas,
    fecha_produccion
) VALUES (5, 1, 1, 'Negro', 1, 1, CURRENT_DATE);