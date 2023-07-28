import obtenerCampos
import obtenerTabla

sql_sentence = "INSERT [dbo].[Adjuntos] ([id], [Solicitudes_id], [nombreArchivo], [envioID], [usuario], [fecha]) VALUES (9978, 1848, 'Observaciones_SES_1848.pdf', 'p1flp5sger16t11mtef3hovj1vr67', 'pku-consultor@aig.gob.pa', CAST('2021-11-30T14:42:58.000' AS DateTime))"

campos = obtenerCampos.getCampos(sql_sentence)
valores = obtenerCampos.getValores(sql_sentence)

if len(campos) != len(valores): exit(0)

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

