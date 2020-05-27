import unittest
import sample

class TestStringMethods(unittest.TestCase):

  def setUpClass():
    print('*** Before entire tests ***')

  def tearDownClass():
    print('*** After entire tests ***')

  def setUp(self):
    print('+ Before test')

  def tearDown(self):
    print('+ After test')

  def test_add_num(self):

    print('start test_add_num')
    self.assertEqual(7, sample.add_num(3, 4))
    print('end test_add_num')

  @unittest.skip('skip the test because of modifying a module')
  def test_is_positive(self):

    print('start test_is_positive')
    self.assertTrue(sample.is_positive(3))
    self.assertFalse(sample.is_positive(0))
    self.assertFalse(sample.is_positive(-1))
    print('end test_is_positive')
