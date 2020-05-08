*** Settings ***
Library         SeleniumLibrary
Suite setup     Before run suite
Suite Teardown  After run suite
Test Setup      Before run test
Test Teardown   After run test

*** Keywords ***
Before run suite 
    Log     Open connections

After run suite
    Log     Close connections 

Before run test
    Log     Create data

After run test
    Log     Delete data


*** Test Cases ***
TC - Canvas Chrome
    Open Browser    https://www.w3schools.com/graphics/tryit.asp?filename=trycanvas_image   chrome
    Capture Page Screenshot     ss_tc_012_a.png 
    Close Browser

TC - Canvas Firefox
    Open Browser    https://www.w3schools.com/graphics/tryit.asp?filename=trycanvas_image   firefox
    Capture Page Screenshot     ss_tc_012_b.png 
    Close Browser
