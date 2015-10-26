__author__ = 'Kaike'
from tokens import *

class SyntaxAnalyser():

    def __init__(self, lexicAnalyser, actionPath, rulesPath, finalState):
        self.actionTable = []
        self.rules = []
        self.actionPath = actionPath
        self.rulesPath = rulesPath
        self.finalState = finalState
        self.buildActionTable()
        self.buildRulesTable()
        self.lexicAnalyser = lexicAnalyser



    def analyse(self, chain):
        self.stack = []
        q = 0
        self.stack.append(0)
        a = Tokens[self.lexicAnalyser.nextToken()]

        while True:
            p = self.action[q][a]
            if p > 0:
                self.stack.append(p)
                a = Tokens[chain[self.lexicAnalyser.nextToken()]]
            elif p < 0:
                for i in range(1, self.rules[0][-p]):
                    self.stack.pop()
                self.stack.append(self.actionTable[self.stack[len(self.stack)-1]][self.rules[1][-p]])
            else:
                print('SyntaxError')
                pass
            q = self.stack.top()

            if q == self.finalState:
                print('Done!')
                break


    def buildActionTable(self):

        file = open(self.actionPath, 'U')
        actions = []

        for line in file.readlines():
            actions.append(line.strip('\n').split(','))

        line = {}
        for i in range(1, len(actions)):
            for j in range(1, len(actions[0])):
                if actions[i][j] == '':
                    actions[i][j] = 0
                line[actions[0][j]] = int(actions[i][j])
            self.actionTable.append(line)
            line = {}


    def buildRulesTable(self):
        file = open(self.rulesPath, 'U')
        for line in file.readlines():
            line = line.strip('\n')
            self.rules.append([line.split(',')[1], line.split(',')[2]])