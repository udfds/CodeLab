*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC - Select option
    Open Browser    https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option_selected   chrome
    Select Frame    id:iframeResult
    Select From List By Index   id:cars     3
    Capture Page Screenshot     ss_tc_008_a.png
    Select From List By Label   id:cars     Saab
    Capture Page Screenshot     ss_tc_008_b.png
    Select From List by Value   id:cars     vw
    Capture Page Screenshot     ss_tc_008_c.png
    Close Browser 