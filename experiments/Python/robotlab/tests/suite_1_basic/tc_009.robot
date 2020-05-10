*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
BrowserDetails
    [Arguments]                ${url}
    Open Browser               ${url}                    chrome

*** Test Cases ***
TC - Keywords
    BrowserDetails             https://www.google.com
    Input Text                 name:q                    robotframework
    Capture Page Screenshot    ss_tc_009.png
    Close Browser