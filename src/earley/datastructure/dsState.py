'''
Created on 14-12-2011

@author: hoangnm
'''

class State(object):
    '''
    A State object in earley's process
    '''

###############################################################################
# BEGIN CONSTRUCTOR
    def __init__(self, rule, position, backpointer):
        '''
        Initialize a state in Earley algorithm process
        A state includes three components: 
            * rule       : instance of Rule, maybe grammar or lexicon
            * position   : a list as [0,1], index of words position in sentence
            * backpointer: a list contains other state for back track 
                           to build tree parse
        '''
        self.rule    = rule             # a Rule
        self.position = position        # a list as [startPos, endPos]
        self.backPointer = backpointer  # a list of state
                                        # as [first state, second state]
                                        
# END CONSTRUCTOR                                        
###############################################################################

###############################################################################
# BEGIN GET FUNCTIONS                                        

    def getPosition(self):
        '''
        Get position list of state 
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list position of this state            
        '''
        return self.position
    
    def getRule(self):
        '''
        Get rule of this state 
        
        Parameters
        ----------
        
        Returns
        -------
        out: rule in this state           
        '''
        return self.rule
        
    def getBackPointer(self):
        '''
        Get back pointer list of this state 
        
        Parameters
        ----------
        
        Returns
        -------
        out: backpointer list           
        '''        
        return self.backPointer
    
# END GET FUNCTIONS
###############################################################################
      
###############################################################################
# BEGIN CHECK FUNCTIONS
    def isComplete(self):
        '''
        Check this state is complete 
        
        Parameters
        ----------
        
        Returns
        -------
        out: True if complete
             Otherwise, return False
        '''        
        return self.rule.isComplete()

# END CHECK FUNCTIONS
###############################################################################

###############################################################################
# BEGIN UTILITY FUNCTIONS
    # compare to another state
    # Input : another state
    # Output: True if rule of this state is similar with another state
    #         False if otherwise
    def compareTo(self, aState):
        '''
        Compare this state with another state 
        
        Parameters
        ----------
        aState: another state
        
        Returns
        -------
        out: True if rule of this state is similar to rule of another state           
        '''        
        return self.rule.compareTo(aState.getRule())
    
    
    def addBackPointer(self, aState):
        '''
        Add a state to backpointer list 
        
        Parameters
        ----------
        aState: a state 
        
        Returns
        -------
        out: backpointer list increases 1 element           
        '''
        self.backPointer.append(aState)
# END UTILITY FUNCTIONS
###############################################################################   