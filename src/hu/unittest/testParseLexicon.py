'''
Created on 11-12-2011

@author: hoangnm
'''
import unittest
from hu.utils.uIO import IO
from hu.cky.ckyAlgorithm import CKY

class Test(unittest.TestCase):

    def setUp(self):
        io = IO('../../../resources/GRAMMAR.IN','../../../resources/LEXICON.IN'
                ,'../../../resources/SENTENCES.IN')
        outfile = 'OUTFILE.'
        self.parser = CKY(io.readGrammar(), io.readLexicon(), outfile)
        self.parser.matrix=[]
        self.parser.initializeTable(4)
        
    def tearDown(self):
        self.parser = None
        
    def testParseLexicon(self):
        sent = 'Fivel ate the cheese'
        self.parser.parseLexicon(sent)
        self.assertEqual(self.parser.matrix[0][0].getElementAt(0).values()[0]
                         .getLeft(), 'NP', "At Left 00")
        self.assertEqual(self.parser.matrix[0][0].getElementAt(0).values()[0]
                         .getRight(), 'Fivel', "At Right 00")
        self.assertEqual(self.parser.matrix[1][1].getElementAt(0).values()[0]
                         .getLeft(), 'VP', "At Left 11")
        self.assertEqual(self.parser.matrix[1][1].getElementAt(0).values()[0]
                         .getRight(), 'ate', "At Right 11")
        self.assertEqual(self.parser.matrix[2][2].getElementAt(0).values()[0]
                         .getLeft(), 'DET', "At Left 22")
        self.assertEqual(self.parser.matrix[2][2].getElementAt(0).values()[0]
                         .getRight(), 'the', "At Right 22")
        self.assertEqual(self.parser.matrix[3][3].getElementAt(0).values()[0]
                         .getLeft(), 'NP', "At Left 33")
        self.assertEqual(self.parser.matrix[3][3].getElementAt(0).values()[0]
                         .getRight(), 'cheese', "At Right 33")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseLexicon']
    unittest.main()