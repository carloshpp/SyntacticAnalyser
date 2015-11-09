__author__ = 'Kaike'
from syntactic_analyser import *
from lexic_analyser import *

la = lexicAnalyser()
filename = "Code.txt"
code = open(filename,'r')
la._setCode(code.read())
sa = SyntaxAnalyser(la, 'actions.csv', 'rules.csv', 1)

sa.analyse()