chunk_size = 40000
csvfile = "C:\\Users\\sbeltran-consultor\\Downloads\\cedulad.csv"
# csvfile = "C:\\Users\\sbeltran-consultor\\Downloads\\csvprueba.csv"
def write_chunk(part, lines):
    with open('./csvgenerados/data_part_'+ str(part) +'.csv', 'wb') as f_out:
        # f_out.write(header)
        f_out.writelines(lines)
        # f_out.



with open(csvfile, "rb") as f:
    count = 0
    header = f.readline()
    lines = []
    for line in f:
        count += 1
        lines.append(line)
        if count % chunk_size == 0:
            write_chunk(count // chunk_size, lines)
            lines = []
    # write remainder
    if len(lines) > 0:
        write_chunk((count // chunk_size) + 1, lines)