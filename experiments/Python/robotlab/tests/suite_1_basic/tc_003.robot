*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Display Message
    [Arguments]        ${msg}         ${level}
    Log                ${msg}         ${level}

*** Test Cases ***
TC - Arguments
    Display Message    Hello World    info