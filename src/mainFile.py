'''
Created on 11-12-2011

@author: hoangnm
'''
from hu.utils.uIO import IO
from hu.cky import ckyAlgorithm

if __name__ == '__main__':
    io = IO('../resources/GRAMMAR.IN', \
            '../resources/LEXICON.IN', \
            '../resources/SENTENCES.IN')
    listOfGrammar = io.readGrammar()
    listOfLexicon = io.readLexicon()
    listOfSentence = io.readSentence()
    outfile = 'OUTFILE.OUT'
    
    cykInstance = ckyAlgorithm.CKY(listOfGrammar,listOfLexicon, outfile)    
    i =0
    for sent in listOfSentence:
        print 'SENTENCE ',i,':' , sent
        #print "..." , cykInstance.syntacticAnalyzer(sent)
        cykInstance.syntacticAnalyzer(sent)
        #cykInstance.printTable()
        i=i+1
        print "----------------------------------------------------------------"
    print "DONE" 