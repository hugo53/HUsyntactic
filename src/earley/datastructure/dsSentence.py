'''
Created on 10-12-2011

@author: hoangnm
'''

class Sentence:
    '''
    classdocs
    '''

    def __init__(self, sentence):
        '''
        Constructor
        '''
        self.listOfWords = sentence.split()
        
    def getWordAt(self, i):
        return self.listOfWords[i]
    
    def getLength(self):
        return len(self.listOfWords)
    def getListOfWords(self):
        return self.listOfWords