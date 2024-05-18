Feature: Ant

  # The first example has two steps
  Scenario: Fresh game
    When the game starts
    Then the board looks like ">"

