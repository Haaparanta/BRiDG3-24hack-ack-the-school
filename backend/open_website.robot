*** Settings ***
Documentation     A simple test to open a website.
Library           SeleniumLibrary
Library           OperatingSystem

*** Test Cases ***
Open Website Test
    ${email}=    Get Environment Variable    EMAIL
    ${password}=    Get Environment Variable    PASSWORD
    Should Not Be Empty    ${email}    EMAIL environment variable is not set
    Should Not Be Empty    ${password}    PASSWORD environment variable is not set

    Open Browser    https://moodle.tuni.fi/course/view.php?id=37071    browser=safari
    Sleep    3s    # Waits for 30 seconds
    Click Element    css:.additional-login
    Sleep    3s    # Waits for 30 seconds
    Wait Until Page Contains Element    id=i0116    timeout=30s
    Input Text    id=i0116    ${EMAIL}
    Sleep   3s    # Waits for 30 seconds
    Click Element    id=idSIButton9
    Sleep    3s    # Waits for 30 seconds
    Wait Until Page Contains Element    id=i0118    timeout=30s
    Input Text    id=i0118    ${PASSWORD}
    Sleep    3s    # Waits for 30 seconds
    Click Element    id=idSIButton9
    Sleep    15s    # Waits for 30 seconds
    [Teardown]    Close Browser


