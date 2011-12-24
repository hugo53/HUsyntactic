'''
Created on 11-12-2011

@author: hoangnm
'''
from cky.utils.ckyIO import CKYIO
from cky.algorithm import ckyAlgorithm

if __name__ == '__main__':
    io = CKYIO('../resources/cky/GRAMMAR.IN', \
            '../resources/cky/LEXICON.IN', \
            '../resources/cky/SENTENCES.IN')
    listOfGrammar = io.readGrammar()
    listOfLexicon = io.readLexicon()
    listOfSentence = io.readSentence()
    outfile = '../resources/cky/OUTFILE.OUT'
    
    cykInstance = ckyAlgorithm.CKY(listOfGrammar,listOfLexicon, outfile)    
    i =0
    for sent in listOfSentence:
        print 'SENTENCE ',i,':' , sent
      
        cykInstance.syntacticAnalyzer(sent)
      
        i=i+1
        print "----------------------------------------------------------------"
    print "DONE" 