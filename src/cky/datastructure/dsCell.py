'''
Created on 11-12-2011

@author: hoangnm
'''

class Cell:
    '''
    A cell is list of dictionaries. 
    Each dictionary contains:
        - key  : a tuple
        - value: a data structure as Grammar or Lexicon  
    '''

    def __init__(self):
        '''
        Initialize a cell with list 'listInCell' is empty
        '''
        self.listInCell=[]
        
    def appendList(self, anElement):
        '''
        Append an element to 'listInCell' list
        
        Parameters
        ----------
        anElement: a dictionary with key is a tuple 
                   and value is Grammar or Lexicon
        
        Returns
        -------
        out: return True if success and 'listIncell' list is increased 1 element 
        '''
        self.listInCell.append(anElement)
        return True
    
    def getList(self):
        '''
        Get 'listInCell' list
        
        Parameters
        ----------
        
        Returns
        ------
        out: a list (that is 'listInCell' of this object)
        '''
        return  self.listInCell

    def getElementAt(self, i):
        '''
        Get element at index i of 'listInCell' list
        
        Parameters
        ----------
        i : index of element in 'listInCell' list
        
        Returns
        ------
        out: a dictionary at index i of 'listInCell' list
        '''
        return self.listInCell[i]
    
    def lenOfListInCell(self):
        '''
        Get length of 'listInCell'
        
        Parameters
        ----------
        
        Returns
        ------
        out: an integer, length of 'listInCell'
        '''
        return len(self.listInCell)
    
    def isEmpty(self):
        '''
        Check 'listInCell' is empty
        
        Parameters
        ----------
        
        Returns
        ------
        out: if 'listInCell' list is empty, return True
             otherwise, return False
        '''
        if len(self.listInCell)==0:
            return True
        else:
            return False       