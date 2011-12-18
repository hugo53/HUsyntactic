'''
Created on 14-12-2011

@author: hoangnm
'''

class State(object):
    '''
    classdocs
    '''


    def __init__(self, rule, position, backpointer):
        '''
        Constructor
        '''
        #self.stateID = id               # an int (e.g: 0, 1, 2)
        self.rule    = rule             # a Rule
        self.position = position        # a list as [startPos, endPos]
        self.backPointer = backpointer  # a list of state
                                        #         as [first state, second state]
        #self.operation   = operation    # a string
                                        #        (seed, predictor,
                                        #         scanner, completer)
                                        
    
    #get methods
    #def getID(self):
    #    return self.stateID
    #compare Id
    # for tracking
    #def compareID(self, anotherRule):
#        if (self.stateID == anotherRule.getID()):
#            return True
#        else:
#            return False
    
    #get back pointer
    #    return a list contains maximum 2 elements
    #    first: first state
    #    second : second state
    def getBackPointer(self):
        return self.backPointer
    
    def addBackPointer(self, aState):
        self.backPointer.append(aState)
    
    #get positions
    #    return a list contains two 2 elements
    #    first  : start pos
    #    second : end pos
    def getPosition(self):
        return self.position
    #get Rule
    def getRule(self):
        return self.rule
      
    # compare to another state
    def compareTo(self, aState):
        return self.rule.compareTo(aState.getRule())
    
    # define complete
    def isComplete(self):
        return self.rule.isComplete()
    
    
              
        
        
        
        