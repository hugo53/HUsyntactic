'''
Created on 10-12-2011

@author: hoangnm
'''

class Lexicon:
    '''
    A lexicon object has two part:
        * leftComponent : a string
        * rightComponent: a string
    '''

    def __init__(self, leftComponent, rightComponent):
        '''
        Constructor with two parameters:
            * leftComponent for 'left'
            * rightComponent for 'right'
        '''
        self.left = leftComponent
        self.right = rightComponent
    
    def getLeft(self):
        '''
        Get left part of lexicon object
        
        Parameters
        ----------
        
        Returns
        -------
        out: left component of Lexicon object
        '''
        return self.left
    
    def setLeft(self, leftComponent):
        '''
        Set left component of Lexicon object
        
        Parameters
        ----------
        leftComponent: a string to assign to self variable 'left'
        
        Returns
        -------
        '''
        self.left = leftComponent
        
    def getRight(self):
        '''
        Get right component of Lexicon object
        
        Parameters
        ----------
        
        Returns
        -------
        out: right component 
        '''
        return self.right
    
    def setRight(self, rightComponent):
        '''
        Set right component
        
        Parameters
        ----------
        rightComponent: a string to assign to self variable 'right'
        
        Returns
        -------
        '''
        self.right = rightComponent
    
    def compareLeftTo(self, otherLexicon):
        '''
        Compare left part with another Lexicon object
        
        Parameters
        ----------
        otherLexicon: another Lexicon object for compare
        
        Returns
        -------
        out: True if left parts are similar
             otherwise, return False
        '''
        if self.left == otherLexicon.left:
            return True
        else:
            return False
    
    def compareRightTo(self, otherLexicon):
        '''
        Compare right part with another Lexicon object
        
        Parameters
        ----------
        otherLexicon: another Lexicon object for compare
        
        Returns
        -------
        out: True if right parts are similar
             otherwise, return False
        '''
        if self.right == otherLexicon.right:
            return True
        else:
            return False