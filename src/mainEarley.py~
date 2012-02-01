'''
Created on 15-12-2011

@author: hoangnm
'''

####Xem lai su trung lap giua tempGrammar va Grammar

from earley.datastructure.dsRule import Rule
from earley.algorithm.earleyAlgorithm import EarleyAlgorithm
from earley.utils.earleyIO import EarleyIO

if __name__ == '__main__':
    grammarFile = '../resources/earley/GRAMMAR1.IN'
    lexiconFile = '../resources/earley/LEXICON1.IN'
    sentenceFile = '../resources/earley/SENTENCES1.IN'
    outFile = '../resources/earley/OUTFILE1.OUT'

    io = EarleyIO()
    sents = io.readSentence(sentenceFile)
    print sents
    gram1 = io.readGrammar(grammarFile)
    gram2 = io.readLexicon(lexiconFile)

    gram1.extend(gram2)

    earleyRun = EarleyAlgorithm(gram1, outFile)

    for i in range(0, len(sents)):
        earleyRun.run(sents[i])
    print "DONE!"
