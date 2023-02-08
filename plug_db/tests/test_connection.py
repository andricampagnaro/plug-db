import unittest

import plug_db

class TestConnection(unittest.TestCase):
    def setUp(self):
        self.my_connection = plug_db.Connection()

    def test_validation_method(self):
        result = self.my_connection.validation_method()
        self.assertEqual(result, 'Class created!')

if __name__ == '__main__':
    unittest.main()