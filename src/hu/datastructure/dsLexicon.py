'''
Created on 10-12-2011

@author: hoangnm
'''

class Lexicon:
    '''
    classdocs
    '''

    # Init
    def __init__(self, leftComponent, rightComponent):
        '''
        Constructor
        '''
        self.left = leftComponent
        self.right = rightComponent
    
    # get-set
    def getLeft(self):
        return self.left
    def setLeft(self, leftComponent):
        self.left = leftComponent
        
    def getRight(self):
        return self.right
    def setRight(self, rightComponent):
        self.right = rightComponent
    
    # operators
    def compareLeftTo(self, otherLexicon):
        if self.left == otherLexicon.left:
            return True
        else:
            return False
    
    def compareRightTo(self, otherLexicon):
        if self.right == otherLexicon.right:
            return True
        else:
            return False