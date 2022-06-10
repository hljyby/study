"""
使用单元测试，测试搜索引擎的RESTFUL接口
- requests
- unittest
"""

from unittest import TestCase,TestSuite,TextTestRunner
import unittest 

class TestIndex(TestCase):
    def setUp(self):
        print("---测试前的资源准备工作---")

    def test_a_add_index(self):
        print("-添加索引-")
        index_name = "person_sos"

    def test_b_get_index(self):
        print("-查询索引-")
        

    def test_c_remive_index(self):
        print("-删除索引-")


    def tearDown(self):
        print("---测试后资源回收的工作---")
class TestDoc(TestCase):

    def test_a1_add_index(self):
        print("-添加索引1111-")


    def test_b1_get_index(self):
        print("-查询索引2222-")
        

    def test_c1_remive_index(self):
        print("-删除索引33333-")
if __name__ == "__main__":
    suite = TestSuite()
    suite.addTest(TestIndex.test_a_add_index)
    suite.addTest(TestDoc.test_a1_add_index)

    TextTestRunner().run(suite)
    unittest.main()