*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${username}     udfds   #Target username
${password}     1234    #Target password

*** Test Cases ***
TC - Login
    Open Browser    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_social_login   chrome
    Select Frame    id:iframeResult
    Input Text  name:username   ${username}
    Input Password  name:password   ${password}
    Capture Page Screenshot     ss_tc_010_a.png
    Click Button    xpath:/html/body/div[1]/form/div/div[3]/input[3]
    Capture Page Screenshot     ss_tc_010_b.png
    Close Browser