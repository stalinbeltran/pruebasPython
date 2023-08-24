chunk_size = 40000
csvfile = "C:\\Users\\sbeltran-consultor\\Downloads\\cedulad.csv"
# csvfile = "C:\\Users\\sbeltran-consultor\\Downloads\\csvprueba.csv"


def writeScript(fscripts, filename):
    script = """
TRUNCATE TABLE `transaccionesvale`.`transacciones`;
LOAD DATA LOCAL INFILE '""" + filename + """' 
INTO TABLE `transaccionesvale`.`transacciones` 
CHARACTER SET utf8 FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'  ESCAPED BY '\\\\' 
LINES TERMINATED BY '\\n' (`TransactionId`, `TransactionFechaCreacion`, `TranctionCreatoruserid`, `TranctionLastModifierUserid`, `TransactionIsDeleted`, `TransactionIsDeletedNew`, `TransactionDeleterUserId`, `TransactionDeletionTime`, `TransactionTenantId`, `TransactionAuthorizationNumber`, `TransactionCashierId`, `TransactionIdenfierType`, `TransactionIdenfier`, `TransactionAmount`, `TransactionBalance`, `TransactionResponsecode`, `TransactionSetledStatus`, `TransactionBranchId`, `TransactionRequestDate`, `TransactionResponseDate`, `TransactionTrackingId`, `TransactionReferenceId`, `TransactionType`, `TransactionProgramId`, `TransactionIsVoided`, `TransactionProcessType`, `UserNombreComnercio`, `TenantId`, `BranchId`, `BranchNombreSucursal`, `BranchDireccion`, `ProgramPrograma`, `UserName`, `UserSurName`);
SHOW WARNINGS;
"""
    fscripts.write(script)

def write_chunk(part, lines, fscripts):
    filename = './csvgenerados/data_part_'+ str(part) +'.csv'
    filenameAbsoluto = "C:\\\\desarrollo\\\\pruebasPython\\\\csvgenerados\\\\data_part_" + str(part) +'.csv'
    writeScript(fscripts, filenameAbsoluto)
    with open(filename, 'wb') as f_out:
        # f_out.write(header)
        f_out.writelines(lines)
        # f_out.


scriptsfile = './csvgenerados/_scriptsImportar.sql'
with open(scriptsfile, "w") as fscripts:
    with open(csvfile, "rb") as f:
        count = 0
        header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % chunk_size == 0:
                write_chunk(count // chunk_size, lines, fscripts)
                lines = []
                break
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines, fscripts)

