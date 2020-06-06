*** Settings ***
Documentation    Create email

Library          SeleniumLibrary

*** Test Cases ***
Create email
    Log To Console    "Hello Robot!"
    Open Browser      https://temp-mail.org/pt/change                                                         chrome                                                   alias=tab1
    Open Browser      https://twitter.com/i/flow/signup                                                       chrome                                                   alias=tab2

    switch browser    tab1
    Sleep             3s
    ${number}=        Evaluate                                                                                random.randint(0, 10)                                    random
    ${user}=          Evaluate                                                                                'temp_email_' + str(${number}) + '0' + str(${number})
    Input Text        id:new_mail                                                                             ${user}
    ${email}=         Evaluate                                                                                ${user}@mailnd7.com
    Click Element     id:postbut

    switch browser    tab2
    Input Text        name=name                                                                               ${user}
    Click Element     xpath=//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div/div[4]
    Input Text        name=email                                                                              ${email}

    #Sleep             3s
    #Select Frame      xpath=/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[1]/div/div/div[2]/iframe
    #Input Text        id:username                                                                                                 web_bot_001
    #Unselect Frame
    #Select Frame      xpath=/html/body/div[2]/div/div/div/div[1]/form/div[2]/section/div/div[2]/iframe
    #Click Element     class:btn-submit
    #Unselect Frame
    #Sleep             2s
    #Click Element     id:confirmModalBtn