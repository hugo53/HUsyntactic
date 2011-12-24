'''
Created on 14-12-2011

@author: hoangnm
'''

from types import *
from earley.datastructure.dsRule import Rule
from earley.datastructure.dsState import State


class EarleyAlgorithm:
    '''
    Describe earley algorithm
    Initialize EarleyAlgorithm object and call 'run' method for each sentence
    to parse syntax tree by earley algorithm
    '''

################################################################################
# GLOBAL VARS   
    '''
    Non-Terminal Set
    '''
    nonSet = ['NP', 'VP', 'PP', 'ADV', 'ADJ','N', 'Nominal' 
                            'V', 'DET', 'Det', 'P', 'ROOT']
    '''
    Part of Speech Set
    '''
    POS = ['N', 'V', 'P', 'DET', 'Det', 'ADV', 'ADJ']
    
    '''
    list of POS for all word in sentence
    '''
    listPOS = []
    
################################################################################

################################################################################
# BEGIN CONSTRUCTOR
    def __init__(self, grammar, outfile):
        '''
        Initialize an EarleyAlgorithm object.
        An EarleyAlgorithm object includes:
            * grammar : 
            * outfile : output file name
        
        '''
        # grammar: list of rule
        self.grammar = grammar
        self.tempGrammar = tuple(self.grammar)        
        self.chart = []
        self.sentence = []
        self.outfile = outfile
        outtemp = open(self.outfile, 'w')   # Create new outfile
        outtemp.close()                     # End create new outfile

# END CONSTRUCTOR
################################################################################

################################################################################
# BEGIN RUN FUNCTION        
    
    def run(self, sent):
        '''
        Run Earley algorithm 
        
        Parameters
        ----------
        sent: a sentence
        
        Returns
        -------
        out: outfile (initialize at init) is wrote if sent has parse tree
        '''
        N = len(sent.split())
        self.earleyParse(sent)
        
        for state in self.chart[N]:
            if (
                  (state.getRule().getLeft()=='S') 
                & (state.getRule().isComplete())
                & (state.getPosition()[0]==0)
                & (state.getPosition()[1]==N)
                ):
                result = self.genSexpression(self.tracking(state, self.chart))
                self.writeResult(self.outfile, '(')
                self.writeResult(self.outfile, result)
                self.writeResult(self.outfile, ')')
        self.writeResult(self.outfile, '\n')

# END RUN FUNCTION
################################################################################

################################################################################
# BEGIN EARLEY PARSER

    def earleyParse(self, sent):
        '''
        Earley algorithm parse 
        
        Parameters
        ----------
        sent: sentence
        
        Returns
        -------
        out: chart (initialize at init) is complete           
        '''
        #Local variables   
        self.sentence = []
        self.sentence = sent.split()            # a list of word
        lenSent = len(self.sentence)
        #POS word i in sent
        self.listPOS = []
        for i in range(0, lenSent):
            self.listPOS.append(self.posOfWord(self.sentence[i]))
        # Init chart ( a list of list)
        self.initChart(lenSent+1)
        # Seed
        startRule = Rule('ROOT', [],['S'])
        startState = State(startRule, [0,0], [])
        self.addToChart(startState, self.chart[0])
        #Loop 
        for i in range(0, lenSent+1):
            for state in self.chart[i]:
                if((state.isComplete() == False)
                   & (self.checkNextCat(state) == False)):
                    self.predictor(state)
                elif((state.isComplete() == False) 
                     & (self.checkNextCat(state) == True)):
                    if i<lenSent:
                        self.scanner(state)
                    else:
                        pass
                        #self.completer(state)    
                else:
                    self.completer(state)
                
        return self.chart

# END EARLEY PARSER
################################################################################                   
 
################################################################################
# BEGIN CORES FUNCTIONS
   
    def predictor(self, state):
        '''
        Predict function 
        
        Parameters
        ----------
        state: state for predict
        
        Returns
        -------    
        '''
        B = state.getRule().getFirstRightTwo()
        j = state.getPosition()[1] 
        print "AT predictor: ", B
               
        tempGram = self.grammarRulesFor(B)
        for temp in tempGram:
            newState = State(temp, [j,j],[])
            self.addToChart(newState, self.chart[j])
                              
    def scanner(self, state):
        '''
        Scan function 
        
        Parameters
        ----------
        state: state for scan
        
        Returns
        -------
        ''' 
        B = state.getRule().getFirstRightTwo()
        print "AT scanner", B, '|', state, '|', self.listPOS[0]
        j = state.getPosition()[1]
        listPosOfWordJ = self.listPOS[j]
        
        if (B in listPosOfWordJ):
            newRule = Rule(B, [self.sentence[j]], [])
            newState = State(newRule, [j, j+1], [])
            self.addToChart(newState, self.chart[j+1])
              
    def completer(self, state):
        '''
        Complete function 
        
        Parameters
        ----------
        state: state for complete
        
        Returns
        -------     
        '''
        B = state.getRule().getLeft()
        j = state.getPosition()[0]
        k = state.getPosition()[1]

        print "AT completer ", B, j
        for stateTemp in self.chart[j]:
            if(stateTemp.getRule().getFirstRightTwo()==B):
                i = stateTemp.getPosition()[0]
                if(stateTemp.getPosition()[1]==j):
                    L = stateTemp.getRule().getLeft()
                    R1 = stateTemp.getRule().getRightOne()[:]
                    R2 = stateTemp.getRule().getRightTwo()[:]
                    newRule = Rule(L,R1,R2)
                        
                    if(newRule.lenRightTwo() > 0):
                        newRule.moveToRightOne()                    
                                  
                    newState = State(newRule, [i,k], [])
                    if(state.getRule().isLexicon()):
                        newState.addBackPointer(state)
                    else:
                        for s in stateTemp.getBackPointer():
                            newState.addBackPointer(s)
                        newState.addBackPointer(state)
                        
                    self.addToChart(newState, self.chart[k])
                    
    #Tracking parse tree
    #return a list
    def tracking(self, startState, chart):
        '''
        Generate parse tree
        
        Parameters
        ----------
        startState: state at last column of chart
        chart     : chart of Earley's algorithm
        
        Returns
        -------
        out: list of elements in parse tree
        '''
        listTrack = []
        if (startState.getRule().isLexicon() == True):
            print 'AT Lexicon ', startState.getRule().getLeft(), \
                                    startState.getRule().getRightOne()[0]
            listTrack.append('(')
            listTrack.append(startState.getRule().getLeft())
            listTrack.append(" ")
            listTrack.append(startState.getRule().getRightOne()[0])
            listTrack.append(')')
        else:
            listTrack.append('(')
            listTrack.append(startState.getRule().getLeft())
            for s in startState.getBackPointer():
                listTrack.append(self.tracking(s, chart))
            listTrack.append(")")
        return listTrack

# END CORE FUNCTIONS
################################################################################

################################################################################
# BEGIN UTILITY FUNCTIONS

    def initChart(self, len):
        '''
        Initialize chart for Earley's algorithm at start point 
        
        Parameters
        ----------
        len : length of sentence
        
        Returns
        -------
        out: an empty chart
        '''
        for i in range(0, len):
            self.chart.append([])
            
    def addToChart(self, state, chartI):
        '''
        Add state to chart entry 
        
        Parameters
        ----------
        state: state to add
        chartI: chart entry
        
        Returns
        -------
        '''        
        if self.checkStateInChartEntry(state, chartI) == False:
            chartI.append(state)
         
    def checkStateInChartEntry(self, state, chartEntry):
        '''
        Check state exists in chart entry
        
        Parameters
        ----------
        state: state to check (before add)
        chartEntry: chart entry
        Returns
        -------
        out: True if state exists
             Otherwise, return False
        '''
        if (state.getRule().getLeft()=='S'):
            return False
        else:
            for s in chartEntry:
                if(s.compareTo(state)):
                    return True
        return False    
        
    def checkNextCat(self, state):
        '''
        Check element after dot symbol in rule of state into POS set 
        
        Parameters
        ----------
        state: state for check 
        
        Returns
        -------
        out: True or False
           
        '''
        if(state.getRule().getFirstRightTwo() in self.POS):
            return True
        else:
            return False
        
    def grammarRulesFor(self, leftPartRule):
        '''
        Find rules for left part of a rule 
        
        Parameters
        ----------
        leftPartRule: left part of rule need find
        
        Returns
        -------
        out: a list contains rules there are satisfactory
        ''' 
        #return a list rules, each rule contains leftPartRule at left part
        res = []
        for e in self.tempGrammar:
            if e.getLeft() == leftPartRule:
                res.append(e)
        return res
         
    #get POS
    def posOfWord(self, word):
        '''
        Get list POS of word 
        
        Parameters
        ----------
        word : word want to get
        
        Returns
        -------
        out: a list includes POSs of word
        ''' 
        posList = []
        for i in range(0, len(self.tempGrammar)):
            if (self.tempGrammar[i].getFirstRightTwo() == word):
                posList.append(self.tempGrammar[i].getLeft())
        return posList
    
    #generate S expression
    def genSexpression(self, listGrammar):
        '''
        Convert a list to S-expression 
        
        Parameters
        ----------
        listGrammar: list contains elements of parse tree
        
        Returns
        -------
        out: a string S-expression
        ''' 
        string = ''
        for i in range(0, len(listGrammar)):
            if type(listGrammar[i]) is ListType:
                string = string + self.genSexpression(listGrammar[i])
            else:
                string = string + listGrammar[i]
        return string
    
    # Write result with extend
    def writeResult(self, filename, string):
        '''
        Write string to outfile 
        
        Parameters
        ----------
        filename: outfile name
        string  : string want to write
        
        Returns
        -------
        ''' 
        outfile=open(filename, 'a')
        outfile.write(string)
        outfile.close()    
                        
# END UTILITY FUNCTIONS
################################################################################