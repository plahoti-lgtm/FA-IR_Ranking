'''
Created on Oct 9, 2017

@author: meike.zehlike
'''
import unittest
import numpy as np
from dataset_creator.synthetic import SyntheticDatasetCreator

class TestSyntheticDatasetCreator(unittest.TestCase):

    def test_constructor(self):
        size = 100000
        creator = SyntheticDatasetCreator(size, {"gender": 2, "ethnicity": 3, "disability": 2}, ["score"])
        self.assertTrue("gender" in creator.dataset.columns)
        self.assertTrue("ethnicity" in creator.dataset.columns)
        self.assertTrue("disability" in creator.dataset.columns)
        self.assertTrue("score" in creator.dataset.columns)

        self.assertEqual((size, 4), creator.dataset.shape)
        self.assertEqual(12, len(creator.groups))

        expectedGroups = [(0, 0, 0),
                          (0, 0, 1),
                          (0, 1, 0),
                          (0, 1, 1),
                          (0, 2, 0),
                          (0, 2, 1),
                          (1, 0, 0),
                          (1, 0, 1),
                          (1, 1, 0),
                          (1, 1, 1),
                          (1, 2, 0),
                          (1, 2, 1)]
        self.assertCountEqual(expectedGroups, creator.groups)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
