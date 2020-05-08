*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC - Click
    Open Browser    https://www.youtube.com     chrome
    Input Text      name:search_query       robot framework
    Click Button    id:search-icon-legacy
    Capture Page Screenshot     ss_tc_005.png
    Close Browser
