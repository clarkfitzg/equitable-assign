import os
import unittest
import tempfile
import shutil

from equiassign import *


class TestStringMethods(unittest.TestCase):
    #give an illeagle input for the tasks
    def test_input_tasks(self):
        with self.assertRaises(ValueError):
            assign(-1,4,3)
    
    #give an illeagle input where number of workers per task is larger than the number of workers
    def test_worker_per_task_illogical(self):
        with self.assertRaises(ValueError):
            assign(15,6,7)

    def test_len(self):
        a = assign(19, 4, 2)
        self.assertEqual(len(a), 4)

    #test if there are a total of 8 "slips" for task17 assigned to the workers
    def test_total_slips(self):
        a  = assign(96,15,8)
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


class TestFiles(unittest.TestCase):
    def setUp(self):
        #create a temporary directory
        self.test_dir = tempfile.mktemp()
        os.mkdir(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_dir_view(self):
        data = assign(10,5,3)
        data = [list(x) for x in data]

        dirname = os.path.join(self.test_dir, "assignments")

        dir_view(dirname,data)

        #make sure there are 5 files 
        initial_count = 0
        for path in os.listdir(dirname):
            if os.path.isfile(os.path.join(dirname,path)):
                initial_count +=1

        self.assertEqual(initial_count,5)

if __name__ == '__main__':
    unittest.main()
