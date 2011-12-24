'''
Created on 11-12-2011

@author: hoangnm
'''
import unittest
from cky.utils.ckyIO import CKYIO

class Test(unittest.TestCase):
    
    def setUp(self):
        self.io = CKYIO('../../../resources/GRAMMAR.IN', \
                     '../../../resources/LEXICON.IN', \
                     '../../../resources/SENTENCES.IN')
        
    def tearDown(self):
        self.io = None

    def testReadGrammar(self):
        listGrammar = self.io.readGrammar()
        self.assertEqual(listGrammar[0].getLeft(), \
                                                "S",'Read grammar: Error 1')
        self.assertEqual(listGrammar[0].getRightFirst(), \
                                              "NP", 'Read grammar: Error 2')
        self.assertEqual(listGrammar[0].getRightSecond(), \
                                              "VP", 'Read grammar: Error 3') 

    def testReadLexicon(self):
        listLexicon = self.io.readLexicon()
        self.assertEqual(listLexicon[0].getLeft(), \
                                              "NP", "Read Lexicon: Error 1")
        self.assertEqual(listLexicon[0].getRight(), \
                                           "Fivel", "Read Lexicon: Error 2")
        
    def testReadSentence(self):
        listSentence = self.io.readSentence()
        self.assertEqual(listSentence[0], "Fivel ate the cheese\n", \
                                                   "Read Sentence: Error 1")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()