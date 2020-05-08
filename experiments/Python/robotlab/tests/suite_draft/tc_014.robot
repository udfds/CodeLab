*** Settings ***
Library     DatabaseLibrary

*** Variables ***
${dbname}       customers
${dbuser}       root
${dbpasswd}     admin
${dbhost}       localhost
${dbport}       3306
@{raw}

*** Test Cases ***
TC - Database
    Connect To Database     pymysql     ${dbname}   ${dbuser}   ${dbpasswd}     ${dbhost}   ${dbport}
    Table Must Exist    customer
    Check If Exist  SELECT * FROM customer 
    @{raw}  Query   SELECT * FROM customer
    Log     @{raw}[0