# User story: A new user account can be created if a proper unused username
# and a proper password are given 

*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  python310

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  pp  python310
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  pp35  python310
    Output Should Contain  Username invalid

Register With Valid Username And Too Short Password
    Input Credentials  pekka  310
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pekka  pythonguru
    Output Should Contain  Password invalid

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123


