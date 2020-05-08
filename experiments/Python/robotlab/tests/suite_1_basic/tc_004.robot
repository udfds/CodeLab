*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC - Capture
    Open Browser    https://www.twitch.tv/  chrome
    Capture Page Screenshot     ss_tc_004.png
    Close Browser