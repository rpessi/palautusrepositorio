*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jaakko
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Credentials
    Registering Should Succeed

Login After Succesful Registration
    Go To Login Page
    Set Username  jaakko
    Set Password  jaakko123
    Submit Login Credentials
    Login Should Succeed

Register With Too Short Username And Valid Password
    Set Username  JP
    Set Password  salasana35
    Set Password Confirmation  salasana35
    Submit Credentials
    Registering Should Fail With Message  Username is too short

Login After Unsuccesful Registration
    Go To Login Page
    Set Username  JP
    Set Password  salasana35
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

Register With Valid Username And Invalid Password
    Set Username  Kaija
    Set Password  ei234
    Set Password Confirmation  ei234
    Submit Credentials
    Registering Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  uolevi
    Set Password  ovela123
    Set Password Confirmation  ovela122
    Submit Credentials
    Registering Should Fail With Message  Password confirmation failed

*** Keywords ***
Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button    Register

Submit Login Credentials
    Click Button    Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
