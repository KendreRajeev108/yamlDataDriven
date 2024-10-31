***Settings***
Documentation    *Author: Rajeev Kendre*
...              General Test Steps Approach:
...                - Log in and navigate to the Search results page.

Library    SeleniumLibrary
Library    BuiltIn
Library    String
Library    Collections
Library    ../Lib/Python/webElements.py
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
${listItems}    (//*[@method="get"]//a)
${listItems_m}    (//*[@method="get"]//a)[<index>]


***Test Cases***

# TC01 Login to the application and search for roles
#     [Documentation]       web Navigation' 
#     ...                    \n\ is set to correct default value \n
    
#     [Tags]    web    
#     Launch browser and Search    ${link}   ${browser}
#     Element Should Be Visible    ${dashboard}
#     Wait Until Element Is Visible    ${search_box}
#     Sleep    10s
#     SeleniumLibrary.Click Element    ${search_box}
#     Input Text    ${search_box}    test
#     Sleep    4s
#     # Press Key    ${search_box}    TAB
#     SeleniumLibrary.Press Keys    ${search_box}    RETURN
#     Sleep    5s
#     # @{user_list}    Get Element Attribute    //*[@method="get"]//a    text
#     # log to console    @{user_list}
#     Wait Until Element Is Visible    ${listItems}
#     ${ROWS} =    Get WebElements    ${listItems}
#     ${EMAIL_ID_LIST}=    Create List
#     ${ROW_COUNT}=    Get Length    ${ROWS}
#         FOR    ${I_CTR}    IN RANGE    1    ${ROW_COUNT}
#         ${I_CTR}=    Convert To String    ${I_CTR}
#         ${EMAIL_ID}=    Replace String    ${listItems_m}    <index>    ${I_CTR}
#         ${user_list}    Get Element Attribute    ${EMAIL_ID}    text
#         # ${EMAIL}=    Get Text    ${EMAIL_ID}
#        Append To List    ${EMAIL_ID_LIST}    ${user_list}
#     END
#     Log to console    ${EMAIL_ID_LIST}
#     Log    ${EMAIL_ID_LIST}
#     Sleep    10s
    
#     # python script to check user is available or not
#     ${output}    Check Roles Avaibility    ${EMAIL_ID_LIST}    miketestuser
#     Log    ${output}
#     Log to console    ${output}  
#     Close All Browsers

# TC02 Verify the initial date format in file
#     [Documentation]       Name: Advanced Logging Features 'formatters_standard_datefmt' 
#     ...                    \n\ is set to correct default value \n
    
#     [Tags]    TEST-T508    Regression_Test    Logging    Settings    Enterprise_Manager
#     ${recievedFormat}    read data from file    ${filePath}    ${advanced_options}    ${formatters_standard_datefmt}
#     log    ${recievedFormat}
#     Log To Console    ${recievedFormat}
#     Should Be Equal As Strings    ${expectedDateFormat}    ${recievedFormat}        msg=verification failed as ${expectedDateFormat} was not equal to ${recievedFormat}

# TC03 Verify the initial date format in file
#     [Documentation]       Name: Advanced Logging Features 'formatters_standard_datefmt' 
#     ...                    \n\ is set to correct default value \n
    
#     [Tags]    TEST-T508    Regression_Test    Logging    Settings    Enterprise_Manager
#     ${recievedFormat}    read data from file    ${filePath}    ${advanced_options}    ${formatters_standard_format}
#     log    ${recievedFormat}
#     Log To Console    ${recievedFormat}
#     Should Be Equal As Strings    ${formatters_standard_format_value}    ${recievedFormat}        msg=verification failed as ${expectedDateFormat} was not equal to ${recievedFormat}

# TC04 Verify the initial date format in file
#     Pass Execution    message



TC01 Login to the application and search for roles
    [Documentation]       web Navigation' 
    ...                    \n\ is set to correct default value \n
    
    [Tags]    web    
    Launch browser and Search    ${link}   ${browser}
    Element Should Be Visible    ${dashboard}
    Wait Until Element Is Visible    ${search_box}
    Sleep    15s
    Click Element    //*[text()="servers" and contains(@class,'title')]
    # Click Element    //*[text()="audit log"]
    sleep     10s
    Click Element    //*[@id="serverstage"]//tbody//tr[1]//td[2]
    Sleep    10s
    
    # Wait Until Element Is Visible    ${clickLoginButton}
    # Element Should be visible     ${clickLoginButton}
    # # input in search box
    # Input text      ${usernameField}     ${Username}
    # Input text      ${passwordField}     ${Password}
    # Click Element       ${clickLoginButton}
    Sleep   5s   reason='waiting for element to appear'
    Sleep    10s

    
    # # Click Element    //*[@title="Filter displayed data"]
    # Sleep    5s

    # Select From List By Index    xpath=//select[@id="reason"]    1

    # Select From List by Value    xpath=(//*[contains(@class,"select__control")])[2]   Action

    

    # SeleniumLibrary.Click Element    ${search_box}
    # Input Text    ${search_box}    test
    # Sleep    4s
# DTC01 get test specific data 
#     Pass Execution    message

# DTC02 Get key data 
#     Pass Execution    message

# DTC03 Get multiple key data
#     Pass Execution    message

*** Keywords ***