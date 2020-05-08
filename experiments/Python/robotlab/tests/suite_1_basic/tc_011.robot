*** Settings ***
Library     SeleniumLibrary

*** Variables ***
&{map}     username=udfds  password=1234
@{list}   udfds  1234

*** Test Cases ***
TC - Map
    Open Browser    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_social_login   chrome
    Select Frame    id:iframeResult
    Input Text  name:username   &{map}[username]
    Input Password  name:password   &{map}[password]
    Capture Page Screenshot     ss_tc_011_a.png
    Click Button    xpath:/html/body/div[1]/form/div/div[3]/input[3]
    Capture Page Screenshot     ss_tc_011_b.png
    Close Browser

TC - List
    Open Browser    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_social_login   chrome
    Select Frame    id:iframeResult
    Input Text  name:username   @{list}[0]
    Input Password  name:password   @{list}[1]
    Capture Page Screenshot     ss_tc_011_c.png
    Click Button    xpath:/html/body/div[1]/form/div/div[3]/input[3]
    Capture Page Screenshot     ss_tc_011_d.png
    Close Browser