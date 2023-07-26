
def search_text_in_file(file_path, search_text):
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    found_lines = []
    for line in lines:
        if search_text in line:
            found_lines.append(line)
            break
    # found_lines = [line.strip() for line in lines if search_text in line]

    return found_lines
    # return lines




def save_text_to_file(file_path, lines):
    with open(file_path, 'w', encoding="utf-8") as file:
        for line in lines:
            file.write(line + '\n')



# lines_to_save = ['This is line 1.', 'This is line 2.', 'And this is line 3.']

file_path = './dump_SES.sql'
# file_path = './pruebabuscar.sql'

# search_text = 'pku-consultor@aig.gob.pa'
search_text = 'a'
found_lines = search_text_in_file(file_path, search_text)

for line in found_lines:
    print(line)
    break

# exit(0)

file_path_to_save = './dump_SES_selectos.sql'
save_text_to_file(file_path_to_save, found_lines)


# Example usage:

