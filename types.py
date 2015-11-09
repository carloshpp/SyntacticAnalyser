__author__ = 'Kaike'
from models import *
from enum import Enum

## kind

tKinds = ["NO_KIND_DEF", "VAR_", "PARAM_", "FUNCTION_", "FIELD_", "ARRAY_TYPE_", "STRUCT_TYPE_",
          "ALIAS_TYPE_", "SCALAR_TYPE_" , "UNIVERSAL_"]

Kinds = Enum._create_('Kinds', tKinds, None, int)

int_ = Object(-1, None, Kinds.SCALAR_TYPE_)
char_ = Object(-1, None, Kinds.SCALAR_TYPE_)
bool_ = Object(-1, None, Kinds.SCALAR_TYPE_)
string_ = Object(-1, None, Kinds.SCALAR_TYPE_)
universal_ = Object(-1, None, Kinds.SCALAR_TYPE_)


def IS_TYPE_KIND(k):
    return k == Kinds.ARRAY_TYPE_ or k == Kinds.STRUCT_TYPE_ or k == Kinds.ALIAS_TYPE_ or k == Kinds.SCALAR_TYPE_

def CheckTypes(self, t1, t2):
    if(t1 == t2):
        return True
    elif(t1 == universal_ or t2 == universal_):
        return True

    elif(t1.eKind == Kinds.UNIVERSAL_ or t2.eKind == Kinds.UNIVERSAL_):
        return True

    elif(t1.eKind == Kinds.ALIAS_TYPE_ and t2.eKind != Kinds.ALIAS_TYPE_):
        return CheckTypes(t1._.Alias.pBaseType,t2)

    elif(t1.eKind != Kinds.ALIAS_TYPE_ and t2.eKind == Kinds.ALIAS_TYPE_):
        return CheckTypes(t1,t2._.Alias.pBaseType)

    elif(t1.eKind == t2.eKind):
        if(t1.eKind == Kinds.ALIAS_TYPE_):
            return CheckTypes(t1._.Alias.pBaseType,t2._.Alias.pBaseType)

        elif(t1.eKind == Kinds.ARRAY_TYPE_):
            if(t1._.Array.nNumElems == t2._.Array.nNumElems):
                return CheckTypes(t1._.Array.pElemType,t2._.Array.pElemType)
        elif(t1.eKind == Kinds.STRUCT_TYPE_):
            f1 = t1._.Struct.pFields
            f2 = t2._.Struct.pFields

            while( f1 != None and f2 != None):
                if( not CheckTypes(f1._.Field.pType,f2._.Field.pType)):
                        return False
            return (f1 == None and f2 == None)
        return False