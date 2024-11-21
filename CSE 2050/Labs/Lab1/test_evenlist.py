import unittest
from exmaple import Evenlist

class TestEvenlist(unittest.TestCase):
    #creat a meathod for each unit test
    #atlest one unit test for each public method
    #ideaolly its sevral test to cover all represetative sanarios
    def testEvenlistInit(self):
        test_list = Evenlist([i for i in range(11)])
        self.assertEqual(test_list._evenlist, [10,8,6,4,2])


unittest.main()