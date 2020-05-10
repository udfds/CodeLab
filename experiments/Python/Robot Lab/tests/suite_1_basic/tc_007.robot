*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TC - Checkbox
    Open Browser               https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox    chrome
    Select Frame               id:iframeResult
    Select Checkbox            name:vehicle3
    Capture Page Screenshot    ss_tc_007.png
    Close Browser