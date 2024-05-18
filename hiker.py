'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''

def global_answer(power = 1):
    return pow(6 * 8, power)

class Hiker:

    def instance_answer(self):
        return global_answer()
