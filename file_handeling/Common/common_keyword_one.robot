*** Settings ***
Documentation     this is common keyword file
Library    SeleniumLibrary
Library     BuiltIn
Resource    ../Object_Repository/login_page.robot
Resource    ../Test_Data/Test_Data_File.robot



*** Keywords ***

Launch browser and Search
    [Arguments]     ${link}   ${browser_name}
    # Navigate to URL
    Open browser    ${link}    ${browser_name}
    Wait Until Element Is Visible    ${clickLoginButton}
    Element Should be visible     ${clickLoginButton}
    # input in search box
    Input text      ${usernameField}     ${Username}
    Input text      ${passwordField}     ${Password}
    Click Element       ${clickLoginButton}
    Sleep   5s   reason='waiting for element to appear'