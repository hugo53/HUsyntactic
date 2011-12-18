'''
Created on 14-12-2011

@author: hoangnm
'''

class Rule(object):
    '''
    classdocs
    
    Each rule has two parts:
        - Left part: 
            * Start symbol S | Non-terminal symbol (Only one symbol)
        - Right part: has two sub-parts (as two lists)
            * right part 1: before dotted-symbol
            * right part 2: after dotted-symbol
            ex: ab.c
                >>> right part 1: [a,b]
                >>> right part 2: [c]
            Note: as default, a new rule has right part 1 empty 
                ex: a -> bc  <=> a -> .bc
                    >>> right part 1: []
                    >>> right part 2: [b,c] 
    '''
    
    # GLOBAL VARS
    nonSet = ['NP', 'VP', 'PP', 'ADV', 'ADJ', 'N', 
                    'V', 'DET', 'Det', 'P', 'ROOT']
    
    POS = ['N', 'V', 'P', 'DET', 'Det', 'ADV', 'ADJ']
    
    def __init__(self, left, rightOne, rightTwo, isLex=False):
        '''
        Constructor
        '''
        self.left = left                        # a string
        listRightOne = rightOne                 # a list
        listRight = rightTwo                    # a list
        self.right = [rightOne, rightTwo]       # a list (list of list)
        self.listParentRule = []                # a list (list of rule)
        self.isLex = isLex
    #set
    def setLeft(self, left):
        self.left = left
        
    def setRight(self, right):
        self.right = right
        
    # Methods
    # moveToRightOne
    #    move first element in right two to right one     
    def moveToRightOne(self):
        self.right[1].reverse()                 # reverse right two
        valuePop = self.right[1].pop()          # pop right two
        self.right[0].append(valuePop)          # add pop right two element to
                                                #         right one
        self.right[1].reverse()                 # reverse right two
        
    #get first element in right two
    #if right two contains at least one element, return first element 
    #else return -1
    #for:
    #    predict
    def getFirstRightTwo(self):
        if (len(self.right[1]) > 0):
            return self.right[1][0]
        else:
            return -1
    
    #get right one 
    def getRightOne(self):
        return self.right[0]
    #get right two
    def getRightTwo(self):
        return self.right[1]
    
    def lenRightTwo(self):
        return len(self.right[1])
    #get left part
    def getLeft(self):
        return self.left
    
    def getIsLex(self):
        return self.isLex
    
    
    #check is lexicon
    def isLexicon(self):
        lenOne = len(self.getRightOne())
        if (lenOne==1):
            if (
                  (self.getLeft() in self.POS)
                & (self.getRightOne()[0] not in self.nonSet)
                ):
                return True
        return False
    
    #check is complete rule
    def isComplete(self):
        if (len(self.getRightTwo())==0):
            return True
        else:
            return False
            
    #compare Rule
    def compareTo(self, aRule):
        if ((self.left == aRule.getLeft())
            &(self.right[0] == aRule.getRightOne())
            &(self.right[1] == aRule.getRightTwo())):
            return True
        else:
            return False
    def isSame(self, aRule):
        this = self.getRightOne()[:]
        this2 = self.getRightTwo()[:]
        this.extend(this2)
        
        that = aRule.getRightOne()[:]
        that2 = aRule.getRightTwo()[:]
        that.extend(that2)
        
        if((self.getLeft()==aRule.getLeft()) & (this==that)):
            return True
        else:
            return False
        
        
              
    