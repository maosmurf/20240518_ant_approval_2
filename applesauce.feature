Feature: Ant

  # The first example has two steps
  Scenario Outline: Fresh game
    Given the game starts with ">"
    When <steps> run
    Then the board looks like "<expected>"
    Examples:
      | steps | expected |
      | 0     | >        |
      | 1     | .v       |

