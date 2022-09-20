from unittest import TestCase, main
from question import zeros

class ZerosTestCase(TestCase):
    def test_1_basics(self):
        self.assertEqual(zeros([0,1,2,3,5]), [1,2,3,5,0])

    def test_2_all_zeros(self):
        self.assertEqual(zeros([0,0,0,0,0]), [0,0,0,0,0])

    def test_3_no_zeros(self):
        self.assertEqual(zeros([1,2,3,4,5]), [1,2,3,4,5])

    def test_4_two_zeros(self):
        self.assertEqual(zeros([1,2,0,0,3,4,5]), [1,2,3,4,5,0,0])

    def test_5_three_zeros(self):
        self.assertEqual(zeros([1,2,0,0,0,3,4,5]), [1,2,3,4,5,0,0,0])

    def test_6_all_zeros_but_1(self):
        self.assertEqual(zeros([0,0,0,0,1,0,0]), [1,0,0,0,0,0,0])

