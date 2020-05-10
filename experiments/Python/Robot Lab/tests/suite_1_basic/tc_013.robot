*** Variables ***
${number}    100
${name}      udfds

*** Test Cases ***
TC - Operations
    Log               Test of operations
    Should Be True    ${number} == 100
    Log               ${name}
    ${var}            Set Variable          Robot Framework
    Log               ${var}
    ${def}            Set Variable          If                 ${number} > 100    Greate    Less
    Log               ${def}