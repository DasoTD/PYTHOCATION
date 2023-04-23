import unittest
from unittest.mock import MagicMock

# Define a class that depends on an external object
class MyClass:
    def __init__(self, dependency):
        self.dependency = dependency
        
    def do_something(self):
        result = self.dependency.get_value()
        return result * 2

# Define a test case that uses a mock object to isolate the code under test
class TestMyClass(unittest.TestCase):
    def test_do_something(self):
        # Create a mock object that simulates the behavior of the external object
        mock_dependency = MagicMock()
        mock_dependency.get_value.return_value = 5
        
        # Create an instance of the class under test, passing in the mock object as a dependency
        my_instance = MyClass(mock_dependency)
        
        # Call the method under test and check the result
        result = my_instance.do_something()
        self.assertEqual(result, 10)
        
        # Check that the mock object was called correctly
        mock_dependency.get_value.assert_called_once()
