'''
Created on 16-12-2011

@author: hoangnm
'''
from earley.datastructure.dsRule import Rule

if __name__ == '__main__':
    rule = Rule("NP",[],['NP', 'PP'])
    print 'Fist'
    print '1 ', rule.getRightOne()
    print '2 ', rule.getRightTwo()
    rule.moveToRightOne()
    print 'After'
    print '1 ', rule.getRightOne()
    print '2 ', rule.getRightTwo()
    rule.moveToRightOne()
    print 'After'
    print '3 ', rule.getRightOne()
    print '4 ', rule.getRightTwo()
    