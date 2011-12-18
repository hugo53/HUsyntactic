'''
Created on 12-12-2011

@author: hoangnm
'''
import unittest

from hu.utils.uIO import IO

class Test(unittest.TestCase):


    def setUp(self):
        self.io = IO('../../../resources/GRAMMAR.IN' \
            ,'../../../resources/LEXICON.IN','../../../resources/SENTENCES.IN')

    def tearDown(self):
        self.io = None
        
    def testWriteResult(self):
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWriteResult']
    unittest.main()