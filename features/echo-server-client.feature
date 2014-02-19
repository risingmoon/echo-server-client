Feature: Receive Data Interace
    As a client with a message
    I want to send message to server
    So that server may receive message

    Scenario: Receive Data
    Given client message string "this is the message to send to the server"
    When I pass socket and buffer
    Then I see "this is the message to send to the server"