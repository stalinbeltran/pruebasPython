import re

sentence = "INSERT [dbo].[nombre Tabla esperado] ([id], [Solicitudes_id], [nombreArchivo], [envioID], [usuario], [fecha]) VALUES (9978, 1848, 'Observaciones_SES_1848.pdf', 'p1flp5sger16t11mtef3hovj1vr67', 'pku-consultor@aig.gob.pa', CAST('2021-11-30T14:42:58.000' AS DateTime))"

def obtenerTabla(sentence):
    # Extract the dynamic text between "[dbo].[" and "]"
    match = re.search(r'\[dbo\]\.\[([^]]+)\]', sentence)

    return match.group(1)

print(obtenerTabla(sentence))
