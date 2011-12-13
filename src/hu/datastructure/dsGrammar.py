'''
Created on 10-12-2011

@author: hoangnm
'''

class Grammar:
    '''
    classdocs
    '''
    
    #Init
    def __init__(self, leftComponent, rightComponentFirst, rightComponentSecond):
        '''
        Constructor with threes components
        '''
        self.left = leftComponent
        self.rightFirst = rightComponentFirst
        self.rightSecond = rightComponentSecond
    
    # left operators    
    def getLeft(self):
        return self.left
    def setLeft(self, leftComponent):
        self.left = leftComponent
        
    # right operators
    def getRightFirst(self):
        return self.rightFirst
    def getRightSecond(self):
        return self.rightSecond
    def setRightFirst(self, rightComponentFirst):
        self.rightFirst = rightComponentFirst
    def setRightSecond(self, rightComponentSecond):
        self.rightSecond = rightComponentSecond
    
    #Operator
    #Compare Right component
    def compareRightTo(self, otherGrammar):
        if ((self.rightFirst==otherGrammar.rightFirst)
            &(self.rightSecond==otherGrammar.rightSecond)):
            return True
        else:
            return False 
    #Compare Left component        
    def compareLeftTo(self, otherGrammar):
        if (self.left == otherGrammar.left):
            return True
        else:
            return False
    