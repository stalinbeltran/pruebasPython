
def search_text_in_file(file_path, search_text):
    with open(file_path, 'r', encoding='utf-16le') as file:
        lines = file.readlines()
    found_lines = []
    for line in lines:
        if search_text in line:
            found_lines.append(line)
            break
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

