'''
Created on 10-12-2011

@author: hoangnm
'''

class Sentence:
    '''
    A Sentence object is a list that is contains words in a sentence
    '''

    def __init__(self, sentence):
        '''
        Constructor with a parameter
            * sentence: a sentence stores in Sentence object
        '''
        self.listOfWords = sentence.split()
        
    def getWordAt(self, i):
        '''
        Get word at i index
        
        Parameters
        ----------
        i : index of word want to get
        
        Returns
        -------
        out: a word (as a string) at index i in list word of this sentence
        '''
        return self.listOfWords[i]
    
    def getLength(self):
        '''
        Get length of 'listOfWords', this is number of words in sentence
        
        Parameters
        ----------
        
        Returns
        -------
        out: an integer, number of words in sentence
        '''
        return len(self.listOfWords)
    
    def getListOfWords(self):
        '''
        Get list of words
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list, this is 'listOfWords'
        '''
        return self.listOfWords