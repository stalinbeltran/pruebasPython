chunk_size = 40000
DB_NAME = "bd_transacciones_vale"
csvfile = "C:\\Users\\sbeltran-consultor\\Downloads\\cedulad.csv"
# csvfile = "C:\\Users\\sbeltran-consultor\\Downloads\\csvprueba.csv"


import mysql.connector


mydb = mysql.connector.connect(
  host="10.253.178.3",
  user="sbeltran",
  password="sbeltran",
  database= DB_NAME
)

mycursor = mydb.cursor()
# mycursor.execute("USE " + DB_NAME + ";")




def writeScript(fscripts, filename):
    script = """
LOAD DATA LOCAL INFILE '""" + filename + """' 
INTO TABLE `""" + DB_NAME + """`.`transacciones` 
CHARACTER SET utf8 FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'  ESCAPED BY '\\\\' 
LINES TERMINATED BY '\\n' (`TransactionId`, `TransactionFechaCreacion`, `TranctionCreatoruserid`, `TranctionLastModifierUserid`, `TransactionIsDeleted`, `TransactionIsDeletedNew`, `TransactionDeleterUserId`, `TransactionDeletionTime`, `TransactionTenantId`, `TransactionAuthorizationNumber`, `TransactionCashierId`, `TransactionIdenfierType`, `TransactionIdenfier`, `TransactionAmount`, `TransactionBalance`, `TransactionResponsecode`, `TransactionSetledStatus`, `TransactionBranchId`, `TransactionRequestDate`, `TransactionResponseDate`, `TransactionTrackingId`, `TransactionReferenceId`, `TransactionType`, `TransactionProgramId`, `TransactionIsVoided`, `TransactionProcessType`, `UserNombreComnercio`, `TenantId`, `BranchId`, `BranchNombreSucursal`, `BranchDireccion`, `ProgramPrograma`, `UserName`, `UserSurName`);

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
truncate = "TRUNCATE TABLE `" + DB_NAME + "`.`transacciones`;"


with open(scriptsfile, "w") as fscripts:
    fscripts.write(truncate)
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
                # break
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines, fscripts)

