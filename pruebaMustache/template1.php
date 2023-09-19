{{=<< >>=}}
SET @ultimo_despliegue=(SELECT MAX(v.fecha_despliegue) FROM bitacora_pmasolidario.version v);
SET @ultima_fase=(SELECT MAX(v.fase) FROM bitacora_pmasolidario.version v);
SET @etiqueta='REINCORPORACION_MOD_v2';

SELECT @ultimo_despliegue;
SELECT @ultima_fase;

DROP TABLE IF EXISTS tmpTot, tmpFilt;

CREATE TEMPORARY TABLE IF NOT EXISTS tmpTot
#SELECT r.cedula, GROUP_CONCAT(m.motivo SEPARATOR ';') AS 'motivo' FROM test.amelia_denis r
SELECT r.cedula, GROUP_CONCAT(m.motivo SEPARATOR ';') AS 'motivo_exclusion_inicial', 
null AS 'motivo_exclusion_actual',
0 AS 'vd_ultima_fase',
0 AS 'beneficiario'
FROM reconsideracion.reincorporacion_modulo_2023_08 r
INNER JOIN bitacora_pmasolidario.v_categorias v
ON v.cedula=r.cedula
LEFT JOIN bitacora_pmasolidario.mes_excluido m
ON m.cedula=r.cedula
#WHERE r.motivo IS NULL AND vd='No'
#WHERE r.cedula NOT IN (SELECT cedula FROM test.reincorporacion_2022_10_27)
GROUP BY r.cedula
;

ALTER TABLE tmpTot MODIFY COLUMN motivo_exclusion_actual VARCHAR(100);

#YA SE LE DIÓ PREVIAMENTE / EN ESTA FASE
UPDATE tmpTot 
SET vd_ultima_fase=1
WHERE 
 cedula IN (SELECT cedula FROM bitacora_pmasolidario.beneficiario b
 INNER JOIN bitacora_pmasolidario.version v
 ON b.version=v.id WHERE fase=@ultima_fase)
 ;


CREATE TEMPORARY TABLE IF NOT EXISTS tmpFilt
SELECT * FROM tmpTot;

#PRINT ALL
SELECT cedula FROM tmpFilt;

UPDATE tmpFilt t
INNER JOIN pmasolidario.v_planilla_estatal v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - FUNCIONARIO')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.v_planilla_estatal);

UPDATE tmpFilt t
INNER JOIN pmasolidario.v_planilla v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - PLANILLA PRIV')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.v_planilla);

UPDATE tmpFilt t
INNER JOIN pmasolidario.v_css_pensionados v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - JUBILADOS/PENSIONADOS')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.v_css_pensionados);

UPDATE tmpFilt t
INNER JOIN pmasolidario.dgi_2023_agosto_q1 v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - DGI > 11K')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.dgi_2023_julio_q1);

UPDATE tmpFilt t
INNER JOIN pmasolidario.mides_programas_transferencia_2023_08 v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - PROGRAMAS TRANSFERENCIA MONETARIA')
WHERE v.programa!='ÁNGEL GUARDIÁN'
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.mides_programas_transferencia_2022_10_q2);


UPDATE tmpFilt t
INNER JOIN pmasolidario.registro_publico_2023_agosto_q1 v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - PROPIEDAD MAYOR A 180K')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.registro_publico_2023_enero_q1);

UPDATE tmpFilt t
INNER JOIN pmasolidario.attt_infracciones_2023_agosto_q1 v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - ATTT - BEBIDAS ALCOHOLICAS O SUSTANCIAS ILICITAS')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.attt_infracciones_2023_enero_q1);

UPDATE tmpFilt t
INNER JOIN pmasolidario.sistema_penitenciario_2023_agosto_q1 v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - sist_penitenciario')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.sistema_penitenciario_2023_enero_q1);

UPDATE tmpFilt t
INNER JOIN tribunal_electoral.padron_defuncion v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', 'DEFUNCION')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM tribunal_electoral.padron_defuncion);

UPDATE tmpFilt t
INNER JOIN pmasolidario.ampyme_cap_semilla_2023_agosto_q1 v
ON v.cedula=t.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - CAPITAL SEMILLA')
;
#DELETE FROM tmpFilt WHERE cedula IN (SELECT cedula FROM pmasolidario.ampyme_cap_semilla_2022_diciembre_q1);

UPDATE tmpFilt t 
INNER JOIN pmasolidario.v_familiar_funcionario ff
ON t.cedula=ff.cedula
SET motivo_exclusion_actual=CONCAT_WS(';', '3 - FAMILIAR FUNCIONARIO')
;



#PRINT THOSE WHO HAVE TODAY AN EXCLUSION
UPDATE tmpFilt
SET beneficiario=0
WHERE motivo_exclusion_actual IS NOT NULL
AND vd_ultima_fase=0
;

#PRINT THOSE WHO WILL HAVE THE BENEFIT
UPDATE tmpFilt
SET beneficiario=1
WHERE motivo_exclusion_actual IS NULL
AND vd_ultima_fase=0
;


UPDATE tmpFilt
SET   beneficiario=1
WHERE motivo_exclusion_inicial = motivo_exclusion_actual
AND motivo_exclusion_inicial IN (
'3 - ELEGIBILIDAD FICHA MIDES'
)
AND beneficiario=0
;

#Si salió por sist. penintenciario
UPDATE tmpFilt t
SET beneficiario=0
WHERE t.motivo_exclusion_inicial LIKE '%sist_pen%';

#Si salió por ATTT
UPDATE tmpFilt t
SET beneficiario=0
WHERE t.motivo_exclusion_inicial LIKE '%ATTT%';

SELECT * FROM tmpFilt;
SELECT * FROM tmpFilt WHERE vd_ultima_fase=1;
SELECT * FROM tmpFilt WHERE beneficiario=0 AND vd_ultima_fase=0; 
SELECT * FROM tmpFilt WHERE beneficiario=1 AND vd_ultima_fase=0; 

/**************************/

CREATE TABLE IF NOT EXISTS reconsideracion.reincorp_mod_2023_08 LIKE tmpFilt;
TRUNCATE TABLE reconsideracion.reincorp_mod_2023_08;
INSERT INTO reconsideracion.reincorp_mod_2023_08
SELECT * FROM tmpFilt; 

SELECT * FROM reconsideracion.reincorp_mod_2023_08;

INSERT IGNORE INTO pmasolidario.recarga_efectiva_reincorporacion
SELECT r.cedula, v.VERSION, 120.00, @etiqueta FROM reconsideracion.reincorp_mod_2023_08 r
INNER JOIN bitacora_pmasolidario.v_categorias v
ON v.cedula=r.cedula
WHERE beneficiario=1 AND vd_ultima_fase=0
;

SELECT 
te.cedula, primer_nombre, segundo_nombre, apellido_paterno,
apellido_materno,  
COALESCE(te.fecha_nacimiento, DATE('2000-01-01')) AS 'fecha_nacimiento',
COALESCE(CONCAT(DATE_FORMAT(te.fecha_vencimiento, '%d/%m/%Y'), ' 12:00:00 a. m.'), '01/01/2050 12:00:00 a. m.') AS 'fecha_vencimiento_cedula',
'120.00' AS monto,
'E' AS flag
FROM pmasolidario.recarga_efectiva_reincorporacion v 
INNER JOIN tribunal_electoral.ciudadanos te
ON te.cedula=v.cedula
WHERE v.observacion=@etiqueta
;