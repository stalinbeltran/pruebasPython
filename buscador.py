ENCODING = 'utf-16le'



def search_text_in_file(file_path, search_text):
    with open(file_path, 'r', encoding=ENCODING) as file:
        lines = file.readlines()
    found_lines = [line.strip() for line in lines if search_text in line]

    return found_lines

def search_different_text_in_file(file_path, longitud):
    with open(file_path, 'r', encoding=ENCODING) as file:
        lines = file.readlines()
    primeralinea = lines[0]
    string_before = primeralinea[0:longitud]
    found_lines = []
    found_lines.append(primeralinea)

    for line in lines:
        if string_before in line:
            continue
        string_before = line[0:longitud]
        found_lines.append(line)

    size = len(found_lines)
    for i in range(0, size):
        print(len(found_lines[i]))
    return found_lines


def save_text_to_file(file_path, lines):
    with open(file_path, 'w', encoding=ENCODING) as file:
        for line in lines:
            file.write(line + '\n')



#Proceso:
file_path = './dump_SES.sql'

#buscamos lineas de texto en el archivo Dump de base de datos
search_text = 'pku-consultor@aig.gob.pa'
found_lines = search_text_in_file(file_path, search_text)

# for line in found_lines:
#     print(line)
#     break

#Guardamos lineas halladas en archivo
file_path_to_save = './dump_SES_selectos.sql'
save_text_to_file(file_path_to_save, found_lines)
# Buscamos lineas distintas (porque salen muchas repetidas, sólo queremos conocer las tablas)
found_different_lines = search_different_text_in_file(file_path_to_save, 36)
file_path_to_save_different = './dump_SES_selectos_diferentes.sql'
save_text_to_file(file_path_to_save_different, found_different_lines)
# Buscamos lineas que contengan INSERT (necesario para eliminar otra basura)
found_lines_insert = search_text_in_file(file_path_to_save_different, "INSERT")
file_path_to_save_insert = './dump_SES_insert.sql'
save_text_to_file(file_path_to_save_insert, found_lines_insert)
# Filtramos lineas distintas (para eliminar Inserts repetidos)
found_different_lines_insert = search_different_text_in_file(file_path_to_save_insert, 36)
file_path_to_save_insert_diferentes = './dump_SES_insert_diferentes.sql'
save_text_to_file(file_path_to_save_insert_diferentes, found_different_lines_insert)


