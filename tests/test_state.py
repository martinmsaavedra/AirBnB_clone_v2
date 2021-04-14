#!/usr/bin/python3
"""
Contains the class Test State
"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand

class Test_State(unittest.TestCase):
    """Class for testing documentation of the console"""
    def testState(self):
        '''Test the creation of new State in database'''
        