

import re
import obtenerTabla



#crear arreglos de tabla, y pares de campo/valor para determinar tabla y campos que contienen el texto buscado
def getCampos(sql_sentence):
    # Extract field names using regex
    field_names = re.findall(r"INSERT.\[dbo\]\.\[Adjuntos\] \((.*?)\)", sql_sentence, re.DOTALL)
    print(field_names)
    if len(field_names) == 0: exit(0)
    fields_string = field_names[0]
    print(fields_string)
    fields = re.findall(r"\[(.*?)\]", fields_string, re.DOTALL)
    print(fields)
    return fields

#obtener valores de la sentencia SQL:
def getValores(sql_sentence):
    # Extract field VALUES using regex
    field_names = re.findall(r"VALUES.\((.*?)\)", sql_sentence, re.DOTALL)
    print(field_names)
    if len(field_names) == 0: exit(0)
    fields_string = field_names[0]
    print(fields_string)
    fields = fields_string.split(',')
    for field in fields:
        field = field.strip()
        print(field)
    return fields

sql_sentence = "INSERT [dbo].[Adjuntos] ([id], [Solicitudes_id], [nombreArchivo], [envioID], [usuario], [fecha]) VALUES (9978, 1848, 'Observaciones_SES_1848.pdf', 'p1flp5sger16t11mtef3hovj1vr67', 'pku-consultor@aig.gob.pa', CAST('2021-11-30T14:42:58.000' AS DateTime))"

campos = getCampos(sql_sentence)
valores = getValores(sql_sentence)

if len(campos) != len(valores): exit(0)

size = len(valores)
for i in range(0, size):
    valores[i] = valores[i].strip()
    valores[i] = valores[i].strip("'")

print('Tenemos pares campo/valor')
# Create a dictionary to hold the field names and their corresponding values
field_dict = dict(zip(campos, valores))

print(field_dict)


