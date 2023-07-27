

import re



#crear arreglos de tabla, y pares de campo/valor para determinar tabla y campos que contienen el texto buscado
def getCampos(lineas):
    #[dbo].[Adjuntos]
    sql_sentence = "INSERT [dbo].[Adjuntos] ([id], [Solicitudes_id], [nombreArchivo], [envioID], [usuario], [fecha]) VALUES (9978, 1848, 'Observaciones_SES_1848.pdf', 'p1flp5sger16t11mtef3hovj1vr67', 'pku-consultor@aig.gob.pa', CAST('2021-11-30T14:42:58.000' AS DateTime))"

    # field_names = re.findall(r'\[([^\]]+)\]', sql_sentence)
    # Extract field names using regex
    field_names = re.findall(r"INSERT.\[dbo\]\.\[Adjuntos\] \((.*?)\)", sql_sentence, re.DOTALL)
    print(field_names)
    if len(field_names) == 0: exit(0)
    fields_string = field_names[0]
    print(fields_string)
    #[id], [Solicitudes_id], [nombreArchivo], [envioID], [usuario], [fecha]
    fields = re.findall(r"\[(.*?)\]", fields_string, re.DOTALL)
# .\[dbo\]\. 
    print(fields)


getCampos(None)

exit(0)

