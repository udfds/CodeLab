*** Settings ***
Documentation    Create email

Library          SeleniumLibrary

*** Test Cases ***
Create email
    Log To Console    "Hello Robot!"
    Open Browser      https://mail.protonmail.com/create/new?language=en                                     chrome
    Input Text        id:password                                                                            @web_bot_001
    Input Text        id:passwordc                                                                           @web_bot_001
    Sleep             3s
    Select Frame      xpath=/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[1]/div/div/div[2]/iframe
    Input Text        id:username                                                                            web_bot_001
    Unselect Frame
    Select Frame      xpath=/html/body/div[2]/div/div/div/div[1]/form/div[2]/section/div/div[2]/iframe
    Click Element     class:btn-submit
    Unselect Frame
    Sleep             2s
    Click Element     id:confirmModalBtn