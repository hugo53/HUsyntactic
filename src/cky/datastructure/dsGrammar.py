'''
Created on 10-12-2011

@author: hoangnm
'''

class Grammar:
    '''
    A Grammar object has two main parts:
        * leftComponent : a string  
        * rightComponent includes two sub parts:
            ** rightComponentFirst : a string
            ** rightComponentSecond: a string
    '''
    
    def __init__(self, leftComponent, rightComponentFirst, rightComponentSecond):
        '''
        Constructor with threes components
        
        Parameters
        ----------
        Consider a grammar: S -> NP VP
        leftComponent       : S
        rightComponentFirst : NP
        rightComponentSecond: VP
        
        Returns
        -------
        '''
        self.left = leftComponent
        self.rightFirst = rightComponentFirst
        self.rightSecond = rightComponentSecond
    
    
    def getLeft(self):
        '''
        Get left part
        
        Parameters
        ----------
        
        Returns
        -------
        out: leftComponent
        '''
        return self.left
    
    def setLeft(self, leftComponent):
        '''
        Set left part
        
        Parameters
        ----------
        leftComponent: a string to assign to self variable 'leftComponent' 
        
        Returns
        -------
        '''
        self.left = leftComponent
        
    def getRightFirst(self):
        '''
        Get first right component
        
        Parameters
        ----------
        
        Returns
        -------
        out: rightFirst
        '''
        return self.rightFirst
    
    def getRightSecond(self):
        '''
        Get second right component
        
        Parameters
        ----------
        
        Returns
        -------
        out: rightSecond
        '''
        return self.rightSecond
    
    def setRightFirst(self, rightComponentFirst):
        '''
        Set first right component
        
        Parameters
        ----------
        rightComponentFirst: a string to assign to self variable 'rightFirst'
        
        Returns
        -------
        out: rightFirst
        '''
        self.rightFirst = rightComponentFirst
    
    def setRightSecond(self, rightComponentSecond):
        '''
        Set second right component
        
        Parameters
        ----------
        rightComponentSecond: a string to assign to self variable 'rightSecond'
        
        Returns
        -------
        out: rightFirst
        '''
        self.rightSecond = rightComponentSecond
    
    def compareRightTo(self, otherGrammar):                
        '''
        Compare right part with another Grammar object
        
        Parameters
        ----------
        otherGrammar: another Grammar object for compare
        
        Returns
        -------
        out: True if two sub parts of right parts are similar
             otherwise, return False
        '''
        if ((self.rightFirst==otherGrammar.rightFirst)
            &(self.rightSecond==otherGrammar.rightSecond)):
            return True
        else:
            return False 
        
    def compareLeftTo(self, otherGrammar):
        '''
        Compare left part with another Grammar object
        
        Parameters
        ----------
        otherGrammar: another Grammar object for compare
        
        Returns
        -------
        out: True if left parts are similar
             otherwise, return False
        '''        
        if (self.left == otherGrammar.left):
            return True
        else:
            return False
    