import unittest 
from activities import is_funny, laugh # import function to test from activities.py file

class ActivityTests(unittest.TestCase): # create a class from unittest.TestCase class
    def test_is_funny_tim(self): # make a test method for is_funny function
    	self.assertEqual(is_funny("tim"), False) # assertEquals check if the is_funny("tim") function call returns False
 
    def test_is_funny_anyone_else(self):
    	"""anyone else but tim should be funny"""
    	self.assertTrue(is_funny("blue"), "blue should be funny") # assertTrue checks if the is_funny("blue") is Truthy
    
    def test_laugh(self):
    	"""laugh returns a laughing string"""
    	self.assertIn(laugh(), ('lol', 'haha', 'tehehe')) # assertIn checks if the laugh() function returns a value that 
														  # is in a tuple ('lol', 'haha', 'tehehe')

if __name__ == "__main__": # check if we lauch the test file
    unittest.main() # lauch the tests