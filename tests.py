from equiassign import *

import unittest

class TestStringMethods(unittest.TestCase):

    def test_len(self):
        a = assign(19, 4, 2)
        self.assertEqual(len(a), 4)

    #test if there are a total of 8 "slips" for task17 assigned to the workers
    def test_total_slips(self):
        a = assign(96,15,8)
        total = sum(x.count(17) for x in a) 
        self.assertEqual(total,8)

    #check if any of the workers have duplicates meaning that they have two of the same tasks
    def tests_duplicates(self):
        a = assign(55,12,3)
        total = 0
        for i in a:
            if(len(i) != len(set(i))):
                total +=1 
        self.assertEqual(total,0)

    #check if the they all have the same taskload
    def test_taskload_perfect_balance(self):
        a = assign(10,5,4)
        alpha = 0
        it = iter(a)
        the_len = len(next(it))
        if not all(len(l) == the_len for l in it):
            alpha = 5

        self.assertEqual(alpha,0)

    #check if they are off by one
    def test_task_oneoff(self):
        a = assign(10,7,4)
        alpha = [len(x) for x in a] 
        diff = max(alpha) - min(alpha)
        self.assertEqual(diff,1)


if __name__ == '__main__':
    unittest.main()
