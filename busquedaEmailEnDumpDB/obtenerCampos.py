

import re
import obtenerTabla



#obtener campos de la sentencia SQL:
def getCampos(sql_sentence):
    print('-----------getCampos')
    # Extract field names using regex
    field_names = re.findall(r"INSERT.\[dbo\]\.\[Solicitudes\] \((.*?)\)", sql_sentence, re.DOTALL)
    print(field_names)
    if len(field_names) == 0: return None
    fields_string = field_names[0]
    print(fields_string)
    fields = re.findall(r"\[(.*?)\]", fields_string, re.DOTALL)
    print(fields)
    return fields

#obtener valores de la sentencia SQL:
def getValores(sql_sentence):
    print('-----------getValores')
    # Extract field VALUES using regex
    field_names = re.findall(r"VALUES (\((?:.)+\))", sql_sentence, re.DOTALL)
    print(field_names)
    if len(field_names) == 0: exit(0)
    fields_string = field_names[0]
    print(fields_string)
    fields = fields_string.split(',')
    for field in fields:
        field = field.strip()
        print(field)
    return fields
