'''
Created on 14-12-2011

@author: hoangnm
'''

from types import *
from earley.datastructure.dsRule import Rule
from earley.datastructure.dsState import State
from earley.utils.uIO import IO

class EarleyAlgorithm:
    '''
    classdocs
    '''
    
    # Global variables   
    # Use 'in' for check a object is nonterminal
    # Example: 
    #         var in list   ---> Return True of False
    nonSet = ['NP', 'VP', 'PP', 'ADV', 'ADJ','N', 
                    'V', 'DET', 'Det', 'P', 'ROOT']
    POS = ['N', 'V', 'P', 'DET', 'Det', 'ADV', 'ADJ']
    listPOS = []
    

    def __init__(self, grammar, outfile):
        '''
        Constructor
        '''
        # grammar: list of rule
        self.grammar = grammar
        self.tempGrammar = tuple(self.grammar)
        #self.listGr = grammar[:]
       
#        print "++++++++++++++++++++++++++++++++++++++++++"
#        for e in self.tempGrammar:
#            print e.getLeft(),' ', e.getRightOne(),' ', e.getRightTwo()
#        print "++++++++++++++++++++++++++++++++++++++++++" 
        self.chart = []
        self.sentence = []
        self.outfile = outfile
        outtemp = open(self.outfile, 'w')   # Create new outfile
        outtemp.close()                     # End create new outfile
        
    def run(self, sent):
        N = len(sent.split())
        self.earleyParse(sent)

        print "len is: ", len(self.chart[N-1])
        
        print '*************************************************'
        print "CHART"
        self.printChart()
        print '*************************************************'
        print '************************************************'
        print "TRACKING"
        for state in self.chart[N]:
            print"STATE ", state.getRule().getLeft(), "->", \
                            state.getRule().getRightOne(),".", \
                            state.getRule().getRightTwo(), state.getPosition(), \
                            state.getBackPointer()
        print '************************************************'
        
        for state in self.chart[N]:
            if (
                  (state.getRule().getLeft()=='S') 
                & (state.getRule().isComplete())
                & (state.getPosition()[0]==0)
                & (state.getPosition()[1]==N)
                ):
             #tree = 
                print "Track at " , state.getRule().getLeft()
                #print "TREE is: "
                result = self.genSexpression(self.tracking(state, self.chart))
                self.writeResult(self.outfile, '(')
                self.writeResult(self.outfile, result)
                self.writeResult(self.outfile, ')')
                print "res is: ", result
                print "List ", self.tracking(state, self.chart)
                
                #print 'END TREE ----------------------------------'            
        self.writeResult(self.outfile, '\n')
    
    def earleyParse(self, sent):
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
#        print self.chart
        #print lenSent
        # Seed
        startRule = Rule('ROOT', [],['S'])
        startState = State(startRule, [0,0], [])
        self.addToChart(startState, self.chart[0])
        #Loop 
        for i in range(0, lenSent+1):
            print "------------------------------------------------------------"
            print "Chart ", i
            
            for state in self.chart[i]:
                print"STATE ", state.getRule().getLeft(), "->", \
                            state.getRule().getRightOne(),".", \
                            state.getRule().getRightTwo(), state.getPosition(), \
                            state.getBackPointer()
                                
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
                   
    def initChart(self, len):
        for i in range(0, len):
            self.chart.append([])
            
    def addToChart(self, state, chartI):
        if self.checkStateInChartEntry(state, chartI) == False:
            chartI.append(state)
    
    def predictor(self, state):
        B = state.getRule().getFirstRightTwo()
        j = state.getPosition()[1] 
        print "AT predictor: ", B
       
#        print "++++++++++++++++++++++++++++++++++++++++++"
#        for e in self.tempGrammar:
#            print e.getLeft(),' ', e.getRightOne(),' ', e.getRightTwo()
#        print "++++++++++++++++++++++++++++++++++++++++++" 
        
        tempGram = self.grammarRulesFor(B)
        print 'tempGram', tempGram[0].getLeft(), tempGram[0].getRightOne(), tempGram[0].getRightTwo()
        for temp in tempGram:
            newState = State(temp, [j,j],[])
            self.addToChart(newState, self.chart[j])
                
                
    def scanner(self, state):
        B = state.getRule().getFirstRightTwo()
        #print "index", state.getPosition()[1]
        print "AT scanner", B, '|', state, '|', self.listPOS[0]
        j = state.getPosition()[1]
        print "j is: ", j
        listPosOfWordJ = self.listPOS[j]
        
        if (B in listPosOfWordJ):
            newRule = Rule(B, [self.sentence[j]], [])
            newState = State(newRule, [j, j+1], [])
            self.addToChart(newState, self.chart[j+1])
            
    
    def completer(self, state):
        B = state.getRule().getLeft()
        j = state.getPosition()[0]
        k = state.getPosition()[1]
#        if (B=='ROOT'):
#            pass
#        else:                
#            print "AT completer ", B, j
#            for stateTemp in self.chart[j]:
#                if(stateTemp.getRule().getFirstRightTwo()==B):
#                    i = stateTemp.getPosition()[0]
#                    if(stateTemp.getPosition()[1]==j):
#                        #newRule = stateTemp.getRule()
#                        L = stateTemp.getRule().getLeft()
#                        R1 = stateTemp.getRule().getRightOne()[:]
#                        R2 = stateTemp.getRule().getRightTwo()[:]
#                        newRule = Rule(L,R1,R2)
#                        
#                        if(newRule.lenRightTwo() > 0):
#                            newRule.moveToRightOne()                    
#                        else:
#                            print "On NO"            
#                        #bp = stateTemp.getBackPointer()
#                        
#                        newState = State(newRule, [i,k], [])
#                        
##                        if (L=='S'):
##                            newState.addBackPointer(state)
##                        else:
#                        newState.addBackPointer(stateTemp)
#                        newState.addBackPointer(state)
#                        
#                        self.addToChart(newState, self.chart[k])
#                        print "ADDED...", newRule.getLeft(), " -> ", newRule.getRightOne(), ".", newRule.getRightTwo()
                        
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
                    else:
                        print "On NO"  
                                  
                    newState = State(newRule, [i,k], [])
                    if(state.getRule().isLexicon()):
                        newState.addBackPointer(state)
                    else:
                        for s in stateTemp.getBackPointer():
                            newState.addBackPointer(s)
                        newState.addBackPointer(state)
                        
                    self.addToChart(newState, self.chart[k])
                    print "ADDED...", newRule.getLeft(), " -> ", newRule.getRightOne(), ".", newRule.getRightTwo()

         
    def checkStateInChartEntry(self, state, chartEntry):
#        for i in range(0, len(chartEntry)):
#            if(chartEntry[i].compareTo(state)):
#                return True
#        return False
        if (state.getRule().getLeft()=='S'):
            return False
        else:
            for s in chartEntry:
                if(s.compareTo(state)):
                    return True
        return False    
        
    def checkNextCat(self, state):
        if(state.getRule().getFirstRightTwo() in self.POS):
            return True
        else:
            return False
        
    def grammarRulesFor(self, leftPartRule):
        #return a list rules, each rule contains leftPartRule at left part
        res = []
        for e in self.tempGrammar:
            if e.getLeft() == leftPartRule:
                res.append(e)
        return res
    
    #Tracking
    #return a list
    #Need a function convert from list to S-express
    def tracking(self, startState, chart):
        listTrack = []
        #if (startState.getRule().getIsLex() == True):
        if (startState.getRule().isLexicon() == True):
            print 'AT Lexicon ', startState.getRule().getLeft(), \
                                    startState.getRule().getRightOne()[0]
        #Or consider via len of backpointer, 0 --> this is lexicon
            listTrack.append('(')
            listTrack.append(startState.getRule().getLeft())
            listTrack.append(" ")
            listTrack.append(startState.getRule().getRightOne()[0])
            listTrack.append(')')
        else:
            listTrack.append('(')
            listTrack.append(startState.getRule().getLeft())

            #print "len of BP", len(startState.getBackPointer())
#            for s in startState.getBackPointer():
#                #print '@@ ',s.getRule().getLeft(), "->", s.getRule().getRightOne(),s.getRule().getRightTwo()
#                if(s.getRule().isSame(startState.getRule())):
#                    listTrack.pop()
#                    listTrack.append("(")
#                    listTrack.append(self.tracking(s, chart))
#                    listTrack.append(")")
##                    for sx in s.getBackPointer():
##                        listTrack.append(self.tracking(sx, chart))
#                     
#                else:
#                    #listTrack.append("(")
#                    #listTrack.append(startState.getRule().getLeft())
#                    #listTrack.append("(")
#                    listTrack.append("(")
#                    listTrack.append(self.tracking(s, chart))
#                    listTrack.append(")")
#                    #listTrack.append(")")
#            #listTrack.append(")")
#            listTrack.append(")")
            for s in startState.getBackPointer():
                listTrack.append(self.tracking(s, chart))
            listTrack.append(")")
        return listTrack
      
      
    #UnSupport tracking
    #return a state    
    def findState(self, stateID, chart):
        for i in range(0, len(chart)):
            for j in range(0, len(chart[i])):
                if (chart[i][j].getID() == stateID):
                    return chart[i][j]
                
    #get POS
    def posOfWord(self, word):
        posList = []
        for i in range(0, len(self.grammar)):
            if (self.grammar[i].getFirstRightTwo() == word):
                posList.append(self.grammar[i].getLeft())
        return posList
    
    #gen S expression
    def genSexpression(self, listGrammar):
        string = ''
        for i in range(0, len(listGrammar)):
            if type(listGrammar[i]) is ListType:
                string = string + self.genSexpression(listGrammar[i])
            else:
                string = string + listGrammar[i]
        return string
    # Write result with extend
    def writeResult(self, filename, string):
        outfile=open(filename, 'a')
        outfile.write(string)
        outfile.close()    
        
    def printChart(self):
        for chartEntry in self.chart:
            for state in chartEntry:
                print "STATE: ", "Rule: ", state.getRule().getLeft(), "->", state.getRule().getRightOne(),state.getRule().getRightTwo(), "Pos ", state.getPosition()
                print "----------------------- BackPointers: "
                for bp in state.getBackPointer():
                       print "BP", bp.getRule().getLeft(),"->", bp.getRule().getRightOne(), bp.getRule().getRightTwo(), "Pos: ", bp.getPosition()
                print "ENDSTATE-----------------------------------------"