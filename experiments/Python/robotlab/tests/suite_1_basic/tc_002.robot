*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TC - Browser
    Open Browser    https://www.twitch.tv/ chrome
    Maximize Browser Window
    Close Browser