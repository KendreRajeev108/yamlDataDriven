***Settings***
Documentation    *Author: Rajeev Kendre*
...              General Test Steps Approach:
...                - Log in and navigate to the Search results page.

Library    SeleniumLibrary
Library     BuiltIn
Resource    ../Object_Repository/login_page.robot
Resource    ../Test_Data/Test_Data_File.robot
Library    ../Lib/Python/file_operations.py
Resource    ../Common/common_keyword_one.robot
Resource    ../Object_Repository/Dashboard_Page.robot

Suite Teardown      Close All Browsers

***Variables***

${ROOT}
${fileName}    log_settings.yaml
${filePath}    ${ROOT}/EnterpriseSystemManager/logs/${fileName}


***Test Cases***

TC01 Login to the application
    [Documentation]       web Navigation' 
    ...                    \n\ is set to correct default value \n
    
    [Tags]    web    
    Launch browser and Search    ${link}   ${browser}
    Element Should Be Visible    ${dashboard}


TC02 Verify the initial date format in file
    [Documentation]       Name: Advanced Logging Features 'formatters_standard_datefmt' 
    ...                    \n\ is set to correct default value \n
    
    [Tags]    TEST-T508    Regression_Test    Logging    Settings    Enterprise_Manager
    ${recievedFormat}    read data from file    ${filePath}    ${advanced_options}    ${formatters_standard_datefmt}
    log    ${recievedFormat}
    Log To Console    ${recievedFormat}
    Should Be Equal As Strings    ${expectedDateFormat}    ${recievedFormat}        msg=verification failed as ${expectedDateFormat} was not equal to ${recievedFormat}

TC03 Verify the initial date format in file
    [Documentation]       Name: Advanced Logging Features 'formatters_standard_datefmt' 
    ...                    \n\ is set to correct default value \n
    
    [Tags]    TEST-T508    Regression_Test    Logging    Settings    Enterprise_Manager
    ${recievedFormat}    read data from file    ${filePath}    ${advanced_options}    ${formatters_standard_format}
    log    ${recievedFormat}
    Log To Console    ${recievedFormat}
    Should Be Equal As Strings    ${formatters_standard_format_value}    ${recievedFormat}        msg=verification failed as ${expectedDateFormat} was not equal to ${recievedFormat}

TC04 Verify the initial date format in file
    Pass Execution    message




*** Keywords ***