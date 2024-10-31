***Settings***
Documentation    *Author: Rajeev Kendre*
...              General Test Steps Approach:
...                - Log in and navigate to the Search results page.

Library    SeleniumLibrary
Library    BuiltIn
Library    String
Library    Collections
Resource    ../Object_Repository/login_page.robot
Resource    ../Test_Data/Test_Data_File.robot
Library    ../Lib/Python/file_operations.py
Resource    ../Common/common_keyword_one.robot
Resource    ../Object_Repository/Dashboard_Page.robot
Library     DataDriver    file=D:\\Users\\rkendre\\Rajeev\\learning\\previous_projects\\jciExacqPoc\\exacqpoc\\file_handeling\\Lib\\Python\\Book2.xlsx
Test Template    Data driven approach to create new servers


Suite Teardown      Close All Browsers

***Variables***

${ROOT}
${fileName}    log_settings.yaml
${filePath}    ${ROOT}/EnterpriseSystemManager/logs/${fileName}
${listItems}    (//*[@method="get"]//a)
${listItems_m}    (//*[@method="get"]//a)[<index>]


***Test Cases***

Data driven ${username} approach for ${password} users
    [Documentation]       web Navigation' 
    ...                    \n\ is set to correct default value \n
    [Tags]    web
    Log many    ${username}    ${password}

    # Launch browser and Search    ${link}   ${browser}
    # Element Should Be Visible    ${dashboard}
    # Wait Until Element Is Visible    ${search_box}
    # Sleep    10s
    # SeleniumLibrary.Click Element    ${search_box}
    # Input Text    ${search_box}    test
    # Sleep    4s
    # # Press Key    ${search_box}    TAB
    # SeleniumLibrary.Press Keys    ${search_box}    RETURN
    # Sleep    5s
    # # @{user_list}    Get Element Attribute    //*[@method="get"]//a    text
    # # log to console    @{user_list}
    # Wait Until Element Is Visible    ${listItems}
    # ${ROWS} =    Get WebElements    ${listItems}
    # ${EMAIL_ID_LIST}=    Create List
    # ${ROW_COUNT}=    Get Length    ${ROWS}
    #     FOR    ${I_CTR}    IN RANGE    1    ${ROW_COUNT}
    #     ${I_CTR}=    Convert To String    ${I_CTR}
    #     ${EMAIL_ID}=    Replace String    ${listItems_m}    <index>    ${I_CTR}
    #     ${user_list}    Get Element Attribute    ${EMAIL_ID}    text
    #     # ${EMAIL}=    Get Text    ${EMAIL_ID}
    #    Append To List    ${EMAIL_ID_LIST}    ${user_list}
    # END
    # Log to console    ${EMAIL_ID_LIST}
    # Log    ${EMAIL_ID_LIST}
    # Sleep    10s


*** keywords ***

Data driven approach to create new servers
    [Arguments]    ${username}    ${password}
    # Log Many    ${username}    ${password}
    Launch browser and Search    ${link}   ${browser}
    Element Should Be Visible    ${dashboard}
    Wait Until Element Is Visible    ${servers_root}
    Sleep    10s
    SeleniumLibrary.Click Element    ${servers_root}
    # Input Text    ${search_box}    test
    Sleep    4s
    # Press Key    ${search_box}    TAB
    # SeleniumLibrary.Press Keys    ${search_box}    RETURN
    # Sleep    5s
    # @{user_list}    Get Element Attribute    //*[@method="get"]//a    text
    # log to console    @{user_list}  //a[text() = 'Add Server']
    SeleniumLibrary.Click Element    //a[text() = 'Add Server']
    Sleep    5s
    
    Wait Until Element Is Visible    ${listItems}
    ${ROWS} =    Get WebElements    ${listItems}
    ${EMAIL_ID_LIST}=    Create List
    ${ROW_COUNT}=    Get Length    ${ROWS}
        FOR    ${I_CTR}    IN RANGE    1    ${ROW_COUNT}
        ${I_CTR}=    Convert To String    ${I_CTR}
        ${EMAIL_ID}=    Replace String    ${listItems_m}    <index>    ${I_CTR}
        ${user_list}    Get Element Attribute    ${EMAIL_ID}    text
        # ${EMAIL}=    Get Text    ${EMAIL_ID}
       Append To List    ${EMAIL_ID_LIST}    ${user_list}
    END
    Log to console    ${EMAIL_ID_LIST}
    Log    ${EMAIL_ID_LIST}
    Sleep    10s