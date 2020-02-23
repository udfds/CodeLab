import pyodbc 
import os
import subprocess
import sys
import time

# ------------------------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------------------------

PATH_SCRIPTS_SQL = "PATH_SCRIPTS_SQL"

cnxn = pyodbc.connect("CONNECTION_STRING", autocommit=True)

# ------------------------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------------------------

def load_file_content(path):
    with open(path) as f:
        content = f.readlines()
    return content

# ------------------------------------------------------------------------------------------------
# Executing script
# ------------------------------------------------------------------------------------------------

exist = os.path.isfile("PATH_BASIC_BACKUP")
if not exist:
    print("The backup was not found, expected path: ")
    print("     PATH_BASIC_BACKUP")
    sys.exit()

cursor = cnxn.cursor()

command_restore = """
USE master 

ALTER DATABASE [DATABASE_NAME] SET SINGLE_USER

WITH ROLLBACK IMMEDIATE 

RESTORE DATABASE [DATABASE_NAME] FROM  DISK = N'PATH_BASIC_BACKUP' WITH  FILE = 1,  MOVE N'DATABASE_NAME' TO N'PATH_DATABASE_MDF.mdf',  MOVE N'DATABASE_NAME_LOG' TO N'PATH_DATABASE_LDF.ldf',  NOUNLOAD,  REPLACE,  STATS = 5
"""

print(" -- Restoring the database DATABASE_NAME \n\n")
affected = cursor.execute(command_restore)
while cursor.nextset():
    pass
cursor.commit()

time.sleep(2)

print(" -- Migration of DATABASE_NAME \n\n")
folders = os.listdir(PATH_SCRIPTS_SQL)

for folder in sorted(folders, key=str.lower):
    if folder != "SPECIAL_FOLDER_1" and folder != "SPECIAL_FOLDER_2" and folder != "SPECIAL_FOLDER_3" and folder != "initDB.sh": 
        files = os.listdir(PATH_SCRIPTS_SQL + folder)
        structure_migration = None
        bootstrap_migration = None
        functions_migration = None

        for file in sorted(files, key=str.lower):
            if "STRUCTURE_MIGRATION" in file:
                structure_migration = PATH_SCRIPTS_SQL + folder + "/" + file

            if "BOOTSTRAP_MIGRATION" in file:
                bootstrap_migration = PATH_SCRIPTS_SQL + folder + "/" + file

            if "FUNCTIONS" in file:
                functions_migration = PATH_SCRIPTS_SQL + folder + "/" + file

        if functions_migration:
            print(" -- Running script of functions from " +  folder + "\n\n")
            subprocess.call(["sqlcmd", "-S", "MACHINE_NAME\\DATABASE_NAME", "-i", functions_migration, "-f","65001" ])

        if structure_migration:
            print(" -- Running script of structure from " +  folder + "\n\n")
            subprocess.call(["sqlcmd", "-S", "MACHINE_NAME\\DATABASE_NAME", "-i", structure_migration, "-f","65001" ])

        if bootstrap_migration:
            print(" -- Running script of bootstrap from " +  folder + "\n\n")
            subprocess.call(["sqlcmd", "-S", "MACHINE_NAME\\DATABASE_NAME", "-i", bootstrap_migration, "-f","65001" ])

if '--OPTIONAL_SCRIPT' in sys.argv:
    print(" -- Running script of OPTIONAL_SCRIPT \n\n")
    special_script = "PATH_OPTIONAL_SCRIPT"
    subprocess.call(["sqlcmd", "-S", "MACHINE_NAME\\DATABASE_NAME", "-i", special_script, "-f","65001" ])



cnxn.commit()

print("")
print("..ciao!")

print(sys.argv) 
