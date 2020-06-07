*** Settings ***
Documentation    Create email

Library          SeleniumLibrary

*** Test Cases ***
Create email
    Log To Console                "Hello Robot!"
    Open Browser                  https://temp-mail.org/pt/change                               chrome                                                                 alias=tab_email
    Open Browser                  https://animeshouse.net/account/                              chrome                                                                 alias=tab_anime
    Set Selenium Implicit Wait    5

    Switch Browser                tab_email
    Sleep                         1s
    ${number}=                    Evaluate                                                      random.randint(0, 10)                                                  random
    ${user}=                      Evaluate                                                      'botlab__' + str(${number}) + '0' + str(${number})
    Input Text                    id:new_mail                                                   ${user}
    ${email}=                     Evaluate                                                      'botlab__' + str(${number}) + '0' + str(${number}) + '@mailnd7.com'
    Click Element                 id:postbut

    Switch Browser                tab_anime
    Click Element                 xpath=/html/body/div/div/div[2]/form/fieldset[4]/span[1]/a
    Sleep                         1s
    Input Text                    id=username                                                   ${user}
    Input Text                    id=email                                                      ${email}
    Input Text                    id=spassword                                                  password@@
    Input Text                    id=firstname                                                  ${user}
    Input Text                    id=lastname                                                   labtob
    Sleep                         1s
    Click Element                 id=dooplay_signup_btn
    Sleep                         3s
    Input Text                    id=s                                                          kaguya-sama
    Press Keys                    id=s                                                          ENTER


