
def search_text_in_file(file_path, search_text):
    with open(file_path, 'r', encoding='utf-16le') as file:
        lines = file.readlines()
    found_lines = [line.strip() for line in lines if search_text in line]

    return found_lines

def search_different_text_in_file(file_path, len):
    with open(file_path, 'r', encoding='utf-16le') as file:
        lines = file.readlines()
    string_before = lines[0][0:len]
    found_lines = []
    found_lines.append(string_before)

    for line in lines:
        if string_before in line:
            continue
        string_before = line[0:len]
        found_lines.append(string_before)
    # found_lines = [line.strip() for line in lines if search_text in line]

    return found_lines








def save_text_to_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-16le') as file:
        for line in lines:
            file.write(line + '\n')


file_path = './dump_SES.sql'

search_text = 'pku-consultor@aig.gob.pa'
found_lines = search_text_in_file(file_path, search_text)

for line in found_lines:
    print(line)
    break


file_path_to_save = './dump_SES_selectos.sql'
save_text_to_file(file_path_to_save, found_lines)
found_different_lines = search_different_text_in_file(file_path_to_save, 36)

file_path_to_save_different = './dump_SES_selectos_diferentes.sql'
save_text_to_file(file_path_to_save_different, found_different_lines)
found_lines_insert = search_text_in_file(file_path_to_save_different, "INSERT")
file_path_to_save_insert = './dump_SES_insert.sql'
save_text_to_file(file_path_to_save_insert, found_lines_insert)



