*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC - Radio button
    Open Browser    https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio     chrome
    Select Frame    id:iframeResult
    Select Radio Button     gender  male
    Select Radio Button     age     30
    Capture Page Screenshot     ss_tc_006.png
    Close Browser