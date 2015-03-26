Feature: Fight or Flight (Natural Language, tutorial02)

    In order to increase the ninja survival rate,
    As a ninja commander
    I want my ninjas to decide whether to take on an opponent
    based on their skill levels.

    Scenario: Weaker opponent
        Given the ninja has a third level black-belt
        When attacked by a samurai
        Then the ninja should engage the opponent

    Scenario: Stronger opponent
        Given the ninja has a third level black-belt
        When attacked by Chuck Norris
        Then the ninja should run for his life

    Scenario: Stronger opponent
        Given the ninja has a third level yellow-belt
        When attacked by Pascal Schreiber
        Then the ninja should run for his life

    Scenario: No opponent
        Given the ninja has a third level yellow-belt
        When not attacked
        Then the ninja should relax
