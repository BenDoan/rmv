import unittest
import os
import shutil
import subprocess

TEST_DIR = "testdir"
MOVE_DIR = "movedir"
NUM_FILES = 1000 #should be even

class TestDefault(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TEST_DIR):
            shutil.rmtree(TEST_DIR)
        os.makedirs(TEST_DIR)
        os.makedirs("%s/%s" % (TEST_DIR,MOVE_DIR))
        os.chdir(TEST_DIR)
        for n in range(NUM_FILES):
            with open("test%s" % n, 'w+') as f:
                f.write("test")

    def test_move(self):
        subprocess.call(["../rmv", MOVE_DIR])
        self.assertEqual(len(os.listdir(MOVE_DIR)), NUM_FILES/2)

    def tearDown(self):
        os.chdir("..")
        shutil.rmtree(TEST_DIR)

class TestPercent(TestDefault):
    def test_move(self):
        subprocess.call(["../rmv","-p 33", MOVE_DIR])
        self.assertEqual(len(os.listdir(MOVE_DIR)), 330)

if __name__ == '__main__':
    unittest.main()
