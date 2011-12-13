'''
Created on 11-12-2011

@author: hoangnm
'''

class Cell:
    '''
    A cell is list of dictionaries. 
    Each dictionary contains:
        - key  : a tuple
        - value: a datastruct as Grammar or Lexicon  
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.listInCell=[]
        
    def appendList(self, anElement):
        self.listInCell.append(anElement)
        return True
    
    def getList(self):
        return  self.listInCell

    def getElementAt(self, i):
        return self.listInCell[i]
    
    def lenOfListInCell(self):
        return len(self.listInCell)
    
    def isEmpty(self):
        if len(self.listInCell)==0:
            return True
        else:
            return False       