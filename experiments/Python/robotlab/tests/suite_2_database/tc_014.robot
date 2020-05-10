*** Settings ***
Library        DatabaseLibrary

*** Variables ***
${dbname}      serviceorders
${dbuser}      root
${dbpasswd}    Play@2020
${dbhost}      localhost
${dbport}      3306
@{raw}

*** Test Cases ***
TC - Database
    Connect To Database            pymysql                 ${dbname}               ${dbuser}    ${dbpasswd}    ${dbhost}    ${dbport}
    Table Must Exist               client
    Check If Exists In Database    SELECT * FROM client
    @{raw}                         Query                   SELECT * FROM client
    Log                            @{raw}[0]