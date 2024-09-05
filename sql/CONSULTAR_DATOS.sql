
-- Obtener todas las Máquinas
SELECT * FROM MaquinasCremallera;

-- Obtener la Máquina con un id especifico
SELECT * FROM MaquinasCremallera WHERE id = 1;

-- Obtener el historial de producción de una Máquina
SELECT * FROM HistorialProduccion WHERE maquina_id = 1;

-- Obtener el último registro de producción de una Máquina
SELECT * 
FROM HistorialProduccion 
WHERE maquina_id = 1 
ORDER BY fecha_produccion DESC 
LIMIT 1;
