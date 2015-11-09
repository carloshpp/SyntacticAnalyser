__author__ = 'Kaike'
from ctypes import *

class Var(Structure):
    def __init__(self):
        self.pType = {}
        self.nIndex = 0
        self.nSize = 0

class Param(Structure):
    def __init__(self):
        self.pType = {}
        self.nIndex = 0
        self.nSize = 0

class Field(Structure):
    def __init__(self):
        self.pType = {}
        self.nIndex = 0
        self.nSize = 0

class Function(Structure):
    def __init__(self):
        self.pRetType = {}
        self.pParams = {}
        nIndex = 0
        nParams = 0
        nVars = 0

class Array(Structure):
    def __init__(self):
        self.pElemType = {}
        self.nNumElems = 0
        self.nSize = 0

class Struct(Structure):
    def __init__(self):
        self.pFields = {}
        self.nSize = 0

class Alias(Structure):
    def __init__(self):
        self.pBaseType = {}
        self.nSize = 0

class _(Union):
    __field_ = [("Var", Var),("Param", Param), ("Field", Field), ("Function", Function),
                ("Array", Array), ("Struct", Struct), ("Alias", Alias)]

class Object():
    def __init__(self, name, next, kind):
        self.nName = name
        self.pNext = next
        self.ekind = kind
        self._ = _()

