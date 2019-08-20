import unittest
from robot import Robot # import class Robot from robot.py file

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.test_robot = Robot("Test Robot", battery=50) # use setUp method to make a test instance (test_robot) of Robot class 
                                                          # for each test method

    def test_init(self):
        """robot should have name and battery"""
        self.assertEqual(self.test_robot.name, "Test Robot")
        self.assertEqual(self.test_robot.battery, 50)

    def test_charge(self):
        """should charge battery to 100%"""
        self.test_robot.charge() # test test_robot.charge() method on test instance (test_robot)
        self.assertEqual(self.test_robot.battery, 100) # test_robot.charge method should make test_robot.battery attribute = 100

    def test_say_name(self):
        """should say name in uppercase"""
        self.assertEqual(
            self.test_robot.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM TEST ROBOT")
        self.assertEqual(self.test_robot.battery, 49)


if __name__ == "__main__":
    unittest.main()
