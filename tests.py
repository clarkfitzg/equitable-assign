from equiassign import *

import unittest

class TestStringMethods(unittest.TestCase):

    def test_len(self):
        a = assign(19, 4, 2)
        self.assertEqual(len(a), 4)

    def test_default(self):
        a = assign(19)
        # self.assertEqual(....)




if __name__ == '__main__':
    unittest.main()
