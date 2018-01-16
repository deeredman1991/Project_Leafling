import unittest
import sys
sys.path.append('{}/../..'.format( sys.path[0] )) #Adds the project's root directory to the sys path.

from scripts.stat import Stat

class TestStat(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStat, self).__init__(*args, **kwargs)
        
        self.test_class = Stat(self, "Test_Critter", 0, 10)
        
    def test_value(self):
        for i in range(1,11):
            self.test_class.value = i
            self.assertEqual(self.test_class.value, i)
            self.assertEqual(self.test_class._value, i)
        
if __name__ == '__main__':
    unittest.main()