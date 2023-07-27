

import re



#crear arreglos de tabla, y pares de campo/valor para determinar tabla y campos que contienen el texto buscado
def camposValor(lineas):
    #[dbo].[Adjuntos]
    sql_sentence = "INSERT [dbo].[Adjuntos] ([id], [Solicitudes_id], [nombreArchivo], [envioID], [usuario], [fecha]) VALUES (9978, 1848, 'Observaciones_SES_1848.pdf', 'p1flp5sger16t11mtef3hovj1vr67', 'pku-consultor@aig.gob.pa', CAST('2021-11-30T14:42:58.000' AS DateTime))"

    # field_names = re.findall(r'\[([^\]]+)\]', sql_sentence)
    # Extract field names using regex
    field_values = re.findall(r"INSERT.\[dbo\]\.\[Adjuntos\] \((.*?)\)", sql_sentence, re.DOTALL)
    print(field_values)


camposValor(None)

exit(0)

# Extract field values using regex
field_values = re.findall(r"VALUES \((.*?)\)", sql_sentence, re.DOTALL)

# Convert the field values to a list of Python objects (integers, strings, datetime)
field_values = eval('[' + field_values[0] + ']')

print(field_names)
# Create a dictionary to hold the field names and their corresponding values
field_dict = dict(zip(field_names, field_values))

# Print the field names and their values
for field_name, field_value in field_dict.items():
    print(f"{field_name}: {field_value}")
