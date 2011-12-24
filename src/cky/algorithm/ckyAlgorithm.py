'''
Created on 10-12-2011

@author: hoangnm
'''

from types import *
from cky.datastructure.dsSentence import Sentence
from cky.datastructure.dsCell import Cell

class CKY:
    '''
    CKY implements CKY algorithm to parse syntax tree
    '''

    def __init__(self, listOfGrammars, listOfLexicons, outfile):
        '''
        Constructor with 3 parameters:
            * listOfGrammars : list contains Grammar objects
            * listOfLexicons : list contains Lexicon objects
            * outfile        : output file
        '''
        self.listGrammars = listOfGrammars  # List of grammar
        self.listLexicons = listOfLexicons  # List of lexicon
        self.matrix = []                    # Table for CYK Algorithm
        self.lenSent = 0                    # Length of sentence
        self.numOfParseTrees = 0            # Number of trees
        self.satisfactory = False           # Check sentence is correct sentence
        self.outfile =  outfile             # Output file
        outtemp = open(self.outfile, 'w')   # Create new outfile
        outtemp.close()                     # End create new outfile
        
    def syntacticAnalyzer(self, sent):
        '''
        Parse syntax tree uses CKY algorithm.
        
        Parameters
        ----------
        sent: a sentence to parse
        
        Returns
        -------
        out: True if sentence 'sent' is valid sentence with grammars and lexicon
             at initialize. Moreover, outfile includes all syntax tree for 
             'sent'
             Otherwise, return False.           
        '''
        self.matrix = []
        self.lenSent = 0
        self.satisfactory = False
        listOfWords = Sentence(sent).getListOfWords()           
        self.lenSent = len(listOfWords)           
        
        # Init matrix
        self.initializeTable(self.lenSent)
        # Parse lexicon
        checkParse = self.parseLexicon(sent)
        if checkParse:    
            # Generate and Parse Grammar
            self.parseGrammar()                    
            # Check
            self.satisfactory = self.hasTree()            
            if(self.satisfactory):
                #Tracking
                for i in range(0, self.matrix[0][self.lenSent-1] \
                               .lenOfListInCell()):
                    if (self.matrix[0][self.lenSent-1].getElementAt(i)
                                        .values()[0].getLeft()=='S'):
                        result = self.genSexpression(self.trackingTree \
                               (self.matrix[0][self.lenSent-1].getElementAt(i)))

                        self.writeResult(self.outfile, '(')
                        self.writeResult(self.outfile, result)
                        self.writeResult(self.outfile, ')')
                        print result
                self.writeResult(self.outfile, '\n') 
            else:
                result = 'THIS IS NOT CORRECT SENTENCE'
                self.writeResult(self.outfile, result+'\n')
                print result                            
        else:
            result = 'THIS IS NOT CORRECT SENTENCE'
            self.writeResult(self.outfile, result+'\n')
            print result                            
            return False
        return self.satisfactory
    
    def parseLexicon(self,sent):
        '''
        Find Lexicon object for each word in sentence 'sent'
        
        Parameters
        ----------
        sent: sentence
        
        Returns
        -------
        out: True if all words into Lexicon objects
             False if otherwise and 'sent' is invalid sentence
        '''
        listOfWords = Sentence(sent).getListOfWords()
        lenSent = len(listOfWords)              
        for i in range(0, lenSent):
            countForWord = 0
            for j in range(0, len(self.listLexicons)):
                if (listOfWords[i]==self.listLexicons[j].getRight()):
                    self.matrix[i][i].appendList({((i, i),(i, i)
                                            ,None, None):self.listLexicons[j]})
                    countForWord = countForWord+1
            if countForWord==0:
                return False       
        return True
        
    def parseGrammar(self):
        '''
        Find Grammar objects in CKY's process
        
        Parameters
        ----------
        
        Returns
        -------
        out: a table is complete
        '''
        for j in range(1, self.lenSent): 
            for i in range(j-1, -1, -1):
                for k in range(0, j-i):
                    #consider (i,j=i+k) for (First), (i=i+1+k,j) for (Second) 
                    if (((self.matrix[i][i+k].isEmpty())==False)
                                &((self.matrix[i+1+k][j].isEmpty())==False)):
                        for u in range(0, self.matrix[i][i+k] \
                                       .lenOfListInCell()):
                            rightFist = self.matrix[i][i+k].getElementAt(u) \
                                                          .values()[0].getLeft()
                            for v in range(0, self.matrix[i+1+k][j] \
                                           .lenOfListInCell()):
                                rightSecond = self.matrix[i+1+k][j] \
                                          .getElementAt(v).values()[0].getLeft()
                                for t in range(0, len(self.listGrammars)):
                                    if ((rightFist== \
                                        self.listGrammars[t].getRightFirst())
                                        &(rightSecond==self.listGrammars[t] \
                                        .getRightSecond())):
                                        self.matrix[i][j].appendList({((i, i+k)\
                                          ,(i+1+k,j),u,v):self.listGrammars[t]})

    def trackingTree(self, start):
        '''
        Generate parse tree
        This is a recursion function
        
        Parameters
        ----------
        start:  Start symbol Grammar in last column
        
        Returns
        -------
        out: one parse tree for sentence
        '''
        tree = []
        ihorizontal = start.keys()[0][0][0]         #Horizontal 
        jhorizontal = start.keys()[0][0][1]
        ivertical   = start.keys()[0][1][0]         #Vertical
        jvertical   = start.keys()[0][1][1]
        if(ihorizontal == jhorizontal == ivertical == jvertical):
            tree.append('(')
            tree.append(start.values()[0].getLeft())
            tree.append(' ')
            tree.append(start.values()[0].getRight())
            tree.append(')')
        else:
            tree.append('(')
            tree.append(start.values()[0].getLeft())
            tree.append(self.trackingTree(self.matrix[start.keys()[0][0][0]] \
                    [start.keys()[0][0][1]].getElementAt(start.keys()[0][2])))
            tree.append(self.trackingTree(self.matrix[start.keys()[0][1][0]] \
                    [start.keys()[0][1][1]].getElementAt(start.keys()[0][3])))
            tree.append(')')
        return tree

    def genSexpression(self, listGr):
        '''
        Generate S expression from list (return value of trackingTree)
        This is a recursion function
        
        Parameters
        ----------
        start:  Start symbol Grammar in last column
        
        Returns
        -------
        out: 
        '''
        string = ''
        for i in range(0, len(listGr)):
            if type(listGr[i]) is ListType:
                string = string + self.genSexpression(listGr[i])
            else:
                string = string + listGr[i]
        return string

    def initializeTable(self, lenSent): 
        '''
        Initialize table at start algorithm
        
        Parameters
        ----------
        lenSent : lenght of sentence
        
        Returns
        -------
        out: an empty table
        '''
        for i in range(0, lenSent):
            tempRow=[]
            for j in range(0, lenSent):
                tempCell = Cell()
                tempRow.append(tempCell)
            self.matrix.append(tempRow)

    def writeResult(self, filename, string):
        '''
        Write parse tree to output file
        
        Parameters
        ----------
        filename: output file name
        string  : string to write
        
        Returns
        -------
        '''
        #Write tree to outfile
        outfile=open(filename, 'a')
        outfile.write(string)
        outfile.close()

################################################################################
# ADDITION FUNCTIONS              
    def hasTree(self): 
        # check sentence has Tree
        if self.matrix[0][self.lenSent-1].isEmpty():
            return False
        else:
            self.numOfParseTrees = 0
            for i in range(0, self.matrix[0][self.lenSent-1].lenOfListInCell()):
                if (self.matrix[0][self.lenSent-1].getElementAt(i)
                                                   .values()[0].getLeft()=='S'):
                    self.numOfParseTrees = self.numOfParseTrees+1
            if self.numOfParseTrees > 0:
                return True        
        return False
                
    def printTable(self):
        # print table for debug
        for i in range(0, self.lenSent):
            print "-----------------------------\n Row ", i
            for j in range(0, self.lenSent):
                if j>= i:
                    for k in range(0,self.matrix[i][j].lenOfListInCell()):
                        print '\t Column ', j, self.matrix[i][j] \
                                        .getElementAt(k).values()[0].getLeft() 
                                        
# END ADDITION FUNCTIONS
################################################################################                            