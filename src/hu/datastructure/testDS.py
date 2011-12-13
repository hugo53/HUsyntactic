'''
Created on 10-12-2011

@author: hoangnm
'''
from dsSentence import Sentence
from dsCell import Cell
from hu.datastructure.dsLexicon import Lexicon
if __name__ == '__main__':
#    sen = Sentence("hello, how are you")
#    print sen.listOfWords
#    print sen.getWordAt(0)
#    print sen.getLength()
#    cell = Cell()
#    
#    row = []
#    matrix=[]
#    for i in range(0,5):
#        row.append(cell)
#    for i in range(0,5):
#        matrix.append(row)
#    
#    matrix[0][0].appendList({(1,2):'hello'})    
#    print matrix[0][0].getElementAt(0).keys()[0][1]
#    matrix[0][0].appendList({(1,3):'bello'})
#    print matrix[0][0].getElementAt(1).keys()[0][1]
#    print matrix[0][0].getList()
#    print type(matrix[0][0])

#    lexicon = Lexicon("S","NP")
#    s = ['NP',1,2]
#    for i in range(0, len(s)):
#        if s[i] == lexicon.getRight():
#            print "OK"
#        else:
#            print "OH, no-"

    cell = Cell()
    row=[]
    for i in range(0, 10):
        row.append(cell)
    for i in range(0, 10):
        matrix.append(row)
    print "len of matrix is: ", len(self.matrix)
