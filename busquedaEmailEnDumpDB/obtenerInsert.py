import obtenerCampos
import obtenerTabla

sql_sentence = "INSERT [dbo].[Solicitudes] ([id], [tipo_id], [monto], [descripcion], [adjuntos_id], [prioridad], [relacion], [estado_id], [entidad_id], [documentos_id], [aprobaciones_id], [usuario], [FechaCreacion], [titulo], [usuarioAsignado], [asignadoPor], [sla], [envioID], [proyecto], [reemplaza], [rolAsignado], [aprobadoPor], [FechaAprobacion], [avanze], [T0], [T1], [T2], [idGrupo], [AIG], [Solicitante], [ahorrar], [Categoria]) VALUES (1896, 2, CAST(297371.15 AS Decimal(18, 2)), N'El servicio de soporte y mantenimiento podrá asegurar el buen funcionamiento de la Red de Comunicaciones DWDM de ETESA (cuya inversión de equipos distribuidos en nueve sitios de ETESA supera los 2.5 millones de balboas), y ante alguna falla en los equipos se podrá dar una respuesta oportuna y solucionar los inconvenientes en el menor tiempo posible, por medio de la asistencia técnica de los especialistas de la fábrica.', 0, 1, N'0', 7, 90, 0, 0, N'ipaz@etesa.com.pa', CAST(N'2022-01-17T08:09:41.000' AS DateTime), N'Contrato de Soporte técnico para la Red DWDM', N'pku-consultor@aig.gob.pa', N'loliva@aig.gob.pa', 0, N'', NULL, 0, N'', N'loliva@aig.gob.pa', CAST(N'2022-01-24T10:09:45.000' AS DateTime), 100, CAST(N'2022-01-25T16:00:00.000' AS DateTime), CAST(N'2022-01-27T16:00:00.000' AS DateTime), CAST(N'2022-02-01T16:00:00.000' AS DateTime), 0, 5, 1, NULL, 2)"

campos = obtenerCampos.getCampos(sql_sentence)
valores = obtenerCampos.getValores(sql_sentence)

ncampos = len(campos)
nvalores = len(valores)
if ncampos != nvalores:
    print('No coinciden logitudes de arreglos campos y valores:' + str(ncampos) + '-' + str(nvalores))
    exit(0)

size = len(valores)
atributos = []
for i in range(0, size):
    valores[i] = valores[i].strip()
    valores[i] = valores[i].strip("'")
    atributo = {}
    atributo["campo"] = campos[i]
    atributo["valor"] = valores[i]
    atributos.append(atributo)

print('Tenemos pares campo/valor')

tabla = obtenerTabla.obtenerTabla(sql_sentence)
insert = {"tabla": tabla}
insert["campos"] = atributos

print('----------------------')
print(insert)

print('----------------------')

search_text = 'pku-consultor@aig.gob.pa'

for campo in insert["campos"]:
    if campo["valor"] == search_text:
        print(campo)

