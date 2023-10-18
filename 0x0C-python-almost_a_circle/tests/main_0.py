#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
     """ Test Class for Auto ID assignment """
     def test_auto_assign_id(self):
         instance1 = Base()
         instance2 = Base()
         self.assertEqual(instance1.id, 1)
         self.assertEqual(instance2.id, 2)

if __name__ == '__main__':
    unittest.main()
