__author__ = 'Kaike'

from types import *
from rules_dictionary import *

NEW_BLOCK_RULE = 30
END_BLOCK_RULE = 10
IDD_RULE = 29
IDU_RULE = 28

class analyser():
    label = 0
    nFuncs = 0

    def __init__(self, lexicAnalyser):
        self.currentLevel = -1
        self.SymbolTable = []
        self.SymbolTableLast = []
        self.la = lexicAnalyser

    def newLabel(self):
        ++analyser.label
        return analyser.label

    def analize(self, action, token, secundaryToken):
        if action == r_NB:
            self.new_block()

        if action == END_BLOCK_RULE:
            self.end_block()

        if action == r_IDD:
            if self.search_in_current_scope(secundaryToken) is not None:
                print "Scope Error. Id already exists"
            else:
                self.define(token)

        if action == r_IDU:
            if self.find_by_name(secundaryToken) is None:
                print "Scope Error. Id does not exists"
                self.define(token)


    def new_block(self):
        self.SymbolTable[++self.currentLevel] = None
        self.SymbolTableLast[self.currentLevel] = None
        return self.currentLevel

    def end_block(self):
        return --self.currentLevel

    def define(self, name):
        newObj = {}
        newObj.name = name

        if self.SymbolTable[self.currentLevel] is None:
            self.SymbolTable[self.currentLevel] = newObj
            self.SymbolTableLast[self.currentLevel] = newObj
        else:
            self.SymbolTableLast[self.currentLevel].next = newObj
            self.SymbolTableLast[self.currentLevel] = newObj

        return newObj

    def search_in_current_scope(self, name):
        newObj = self.SymbolTable[self.currentLevel]
        while newObj is not None:
            if newObj.name == name:
                break
            else:
                newObj = newObj.next
        return newObj


    def find_by_name(self, name):
        newObj = {}
        for i in range(self.currentLevel, 0, -1):
            newObj = self.SymbolTable[i]
            while newObj is not None:
                if newObj.name == name:
                    break
                else:
                    newObj = newObj.next
            if newObj is not None:
                break

        return newObj

    def semantics(self,rule):
        tokenSecundario = {}
        name = 0
        n = 0
        l= 0
        l1 = 0
        l2 = 0
        p = {}
        t = {}
        f = {}
        IDD_ = {}
        IDU_ = {}
        ID_ = {}
        T_ = {}
        LI_ = {}
        LI0_ = {}
        LI1_ = {}
        TRU_ = {}
        FALS_ = {}
        STR_ = {}
        CHR_ = {}
        NUM_ = {}
        DC_ = {}
        DC0_ = {}
        DC1_ = {}
        LP_ = {}
        LP0_ = {}
        LP1_ = {}
        E_ = {}
        E0_ = {}
        E1_ = {}
        L_ = {}
        L0_ = {}
        L1_ = {}
        R_ = {}
        R0_ = {}
        R1_ = {}
        K_ = {}
        K0_  = {}
        K1_ = {}
        F_ = {}
        F0_ = {}
        F1_ = {}
        LV_ = {}
        LV0_ = {}
        LV1_ = {}
        MC_ = {}
        LE_ = {}
        LE0_ = {}
        LE1_={}
        MT_={}
        ME_ = {}
        MW_ = {}
        MA_ = {}
        curFunction = {}

        self.stack = []

        if(rule == r_IDD):
            name = tokenSecundario
            IDD_.nont = IDD
            IDD_._.ID.name = name
            p = self.search_in_current_scope(name)
            if( p != None):
                print "variable already exists"

            else:
                p = self.define(name)

            p.eKind = Kinds.NO_KIND_DEF_
            IDD_._.ID.obj = p
            self.stack.append(IDD_)

        elif(rule == r_IDU):
            name = tokenSecundario
            IDU_.nont = IDU
            IDU_._.ID.name = name
            p = self.find_by_name(name)
            if(p == None):
                print "Not declared yet"
                p = self.define(name)

            IDU_._.ID.obj = p
            self.stack.append(IDU_)

        elif(rule == r_ID):
            ID_.nont = ID
            name = tokenSecundario
            ID_._.ID.name = name
            ID_._.ID.obj = None
            self.stack.append(ID_)


        elif(rule==r_T_IDU ):
            IDU_ = self.stack.__getitem__(self.stack.__len__()-1)
            p = IDU_._.ID.obj
            self.stack.pop()

            if(IS_TYPE_KIND(p.eKind) or p.eKind == Kinds.UNIVERSAL_):
                T_._.T.type = p
                T_.nSize = p._.Alias.nSize

            else:
                T_._.T.type = universal_
                T_.nSize = 0
                print "Type Expected"

            T_.nont = T
            self.stack.append(T_)

        elif(rule==r_T_INTEGER ):
            T_._.T.type = int_
            T_.nont = T
            T_.nSize = 1
            self.stack.append(T_)

        elif(rule==r_T_CHAR ):
            T_._.T.type = char_
            T_.nont = T
            T_.nSize = 1
            self.stack.append(T_)

        elif(rule==r_T_BOOL ):
            T_._.T.type = bool_
            T_.nont = T
            T_.nSize = 1
            self.stack.append(T_)

        elif(rule==r_T_STRING ):
            T_._.T.type = string_
            T_.nont = T
            T_.nSize = 1
            self.stack.append(T_)

        elif( rule ==r_LI_IDD ):
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            LI_._.LI.list = IDD_._.ID.obj
            LI_.nont = LI
            self.stack.pop()
            self.stack.append(LI_)

        elif(rule==r_LI_COMMA ):
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LI1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LI0_._.LI.list = LI1_._.LI.list
            LI0_.nont = LI
            self.stack.append(LI0_)

        elif(rule==r_DV_VAR ):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            t = T_._.T.type
            self.stack.pop()
            LI_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            p = LI_._.LI.list
            n = curFunction._.Function.nVars

            while(p != None and p.eKind == Kinds.NO_KIND_DEF_):
                p.eKind = Kinds.VAR_
                p._.Var.pType = t
                p._.Var.nSize = T_.nSize
                p._.Var.nIndex = n

                n += T_.nSize
                p = p.pNext


            curFunction._.Function.nVars = n

        elif(rule==r_TRUE ):
            TRU_.nont = TRU
            TRU_._.TRU.val = True
            TRU_._.TRU.type = bool_
            self.stack.append(TRU_)

        elif(rule==r_FALSE ):
            FALS_.nont = FALS
            FALS_._.FALS.val = False
            FALS_._.FALS.type = bool_
            self.stack.append(FALS_)

        elif(rule==r_CHR ):
            CHR_.nont = CHR
            CHR_._.CHR.type = char_
            CHR_._.CHR.pos = tokenSecundario
            CHR_._.CHR.val = self.la.getCharConst(tokenSecundario)
            self.stack.append(CHR_)

        elif(rule==r_STR ):
            STR_.nont = STR
            STR_._.STR.type = string_
            STR_._.STR.pos = tokenSecundario
            STR_._.STR.val = self.la.getStringConst(tokenSecundario)
            self.stack.append(STR_)

        elif(rule==r_NUM ):
            NUM_.nont = Kinds.NUM
            NUM_._.NUM.type = int_
            NUM_._.NUM.pos = tokenSecundario
            NUM_._.NUM.val = self.la.getIntConst(tokenSecundario)
            self.stack.append(NUM_)

        elif(rule==r_DT_ARRAY ):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            NUM_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = IDD_._.ID.obj
            n = NUM_._.NUM.val
            t = T_._.T.type

            p.eKind = Kinds.ARRAY_TYPE_
            p._.Array.nNumElems = n
            p._.Array.pElemType = t
            p._.Array.nSize = n * T_.nSize


        elif(rule == r_DT_ALIAS):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = IDD_._.ID.obj
            t = T_._.T.type

            p.eKind = Kinds.ALIAS_TYPE_
            p._.Alias.pBaseType = t
            p._.Alias.nSize = T_.nSize

        elif(rule==r_NB ):
            self.newBlock()

        elif(rule==r_DC_LI ):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LI_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = LI_._.LI.list
            t = T_._.T.type
            n = 0
            while( p != None and p.eKind == Kinds.NO_KIND_DEF_):
                p.eKind = Kinds.FIELD_
                p._.Field.pType = t
                p._.Field.nSize = T_.nSize
                p._.Field.nIndex = n
                n = n + T_.nSize
                p = p.pNext

            DC_._.DC.list = LI_._.LI.list
            DC_.nSize = n
            DC_.nont = DC
            self.stack.append(DC_)

        elif(rule==r_DC_DC ):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LI_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            DC1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = LI_._.LI.list
            t = T_._.T.type
            n = DC1_.nSize

            while( p != None and p.eKind == Kinds.NO_KIND_DEF_):
                p.eKind = Kinds.FIELD_
                p._.Field.pType = t
                p._.Field.nIndex = n
                p._.Field.nSize = T_.nSize
                n = n + T_.nSize
                p = p.pNext


            DC0_._.DC.list = DC1_._.DC.list
            DC0_.nSize = n
            DC0_.nont = DC
            self.stack.append(DC0_)

        elif(rule== r_DT_STRUCT ):
            DC_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = IDD_._.ID.obj
            p.eKind =Kinds.STRUCT_TYPE_
            p._.Struct.pFields = DC_._.DC.list
            p._.Struct.nSize = DC_.nSize
            self.endBlock()

        elif(rule==r_LP_EPSILON ):
            LP_._.LP.list = None
            LP_.nont = LP
            LP_.nSize = 0
            self.stack.append(LP_)

        elif(rule==r_LP_IDD ):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = IDD_._.ID.obj
            t = T_._.T.type
            p.eKind = Kinds.PARAM_
            p._.Param.pType = t
            p._.Param.nIndex = 0
            p._.Param.nSize = T_.nSize
            LP_._.LP.list = p
            LP_.nSize = T_.nSize
            LP_.nont = LP

            self.stack.append(LP_)

        elif(rule==r_LP_LP ):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LP1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = IDD_._.ID.obj
            t = T_._.T.type
            n = LP1_.nSize

            p.eKind = Kinds.PARAM_
            p._.Param.pType = t
            p._.Param.nIndex = n
            p._.Param.nSize = T_.nSize

            LP0_._.LP.list = LP1_._.LP.list
            LP0_.nSize = n + T_.nSize
            LP0_.nont = LP
            self.stack.append(LP0_)

        elif(rule==r_NF ):
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            f = IDD_._.ID.obj
            f.eKind = Kinds.FUNCTION_
            f._.Function.nParams = 0
            f._.Function.nVars = 0
            f._.Function.nIndex = ++analyser.nFuncs
            self.newBlock()

        elif(rule==r_MF ):
            T_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LP_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            IDD_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            f = IDD_._.ID.obj
            f.eKind = Kinds.FUNCTION_
            f._.Function.pRetType = T_._.T.type
            f._.Function.pParams = LP_._.LP.list
            f._.Function.nParams = LP_.nSize
            f._.Function.nVars = LP_.nSize
            curFunction = f

            print "BEGIN_FUNC {0} {1} {2}".format(f._.Function.nIndex, f._.Function.nParams,f._.Function.nVars-f._.Function.nParams)

        elif(rule==r_DF ):
            self.endBlock()
            print "END_FUNC"

        elif(rule==r_S_BLOCK ):
            self.endBlock()

        elif(rule==r_S_E_SEMICOLON):
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            print " POP"

        elif(rule==r_MT ):
            l = self.newLabel()
            MT_._.MT.label = l
            MT_.nont = MT
            print " TJMP_FW L {0}".format(l)
            self.stack.append(MT_)

        elif(rule==r_S_IF ):
            self.stack.pop()
            MT_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            t = E_._.E.type
            if( not CheckTypes(t,bool_)):
                print"Bool Type Expected"

            print "L {0}".format(MT_._.MT.label)


        elif(rule==r_ME ):
            MT_ = self.stack.__getitem__(self.stack.__len__()-1)
            l1 = MT_._.MT.label
            l2 = self.newLabel()
            ME_._.ME.label = l2
            ME_.nont = ME
            self.stack.append(ME_)

            print " TJMP_FW L {0}".format(l2)
            print "L {0}".format(l1)

        elif(rule==r_S_IF_ELSE ):
            ME_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            MT_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            l = ME_._.ME.label

            t = E_._.E.type
            if( not CheckTypes(t,bool_)):
                print "Bool Type Expected"

            print " L {0}".format(l)

        elif(rule==r_MW ):
            l = self.newLabel()
            MW_._.MW.label = l
            self.stack.append(MW_)
            print " L {0}".format(l)

        elif(rule==r_S_WHILE ):
            MT_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            MW_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            l1 = MW_._.MW.label
            l2 = MT_._.MT.label

            t = E_._.E.type
            if( not CheckTypes(t,bool_)):
                print "Bool Type Expected"


            print "JMP_BW L{0}".format(l1)
            print "L{0}".format(l2)

        elif(rule==r_S_DO_WHILE ):
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            MW_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            l = MW_._.MW.label

            t = E_._.E.type
            if( not CheckTypes(t, bool_)):
                print "Bool Type Expected"


            print " NOT"
            print " TJMP_BW L{0}".format(l)

        elif(rule == r_S_BREAK):
            MT_ = self.stack.__getitem__(self.stack.__len__()-1)

        elif(rule==r_S_RETURN ):
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            if(not CheckTypes(curFunction._.Function.pRetType,E_._.E.type)):
                print "Types does not match"

            print " RET"

        elif(rule==r_E_AND ):
            L_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            E1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            if( not CheckTypes(E1_._.E.type,bool_)):
                print "Bool Type Expected"


            if( not CheckTypes(L_._.L.type,bool_)):
                print "Bool Type Expected"


            E0_._.E.type = bool_
            E0_.nont = E
            self.stack.append(E0_)
            print " AND"

        elif(rule==r_E_OR ):
            L_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            E1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            if( not CheckTypes(E1_._.E.type,bool_)):
                print "Bool Type Expected"


            if( not CheckTypes(L_._.L.type, bool_)):
                print "Bool Type Expected"


            E0_._.E.type = bool_
            E0_.nont = E
            self.stack.append(E0_)
            print " OR"

        elif(rule==r_E_L ):
            L_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            E_._.E.type = L_._.L.type
            E_.nont = E
            self.stack.append(E_)

        elif(rule==r_L_LESS_THAN ):
            R_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            L1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(L1_._.L.type,R_._.R.type)):
                print "Types does not match"

            L0_._.L.type = bool_
            L0_.nont = L
            self.stack.append(L0_)

            print " LT"

        elif(rule == r_L_GREATER_THAN ):
            R_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            L1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(L1_._.L.type,R_._.R.type)):
                print "Types does not match"

            L0_._.L.type = bool_
            L0_.nont = L
            self.stack.append(L0_)
            print " GT"

        elif(rule==r_L_LESS_EQUAL ):
            R_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            L1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(L1_._.L.type,R_._.R.type)):
                print "Types does not match"

            L0_._.L.type = bool_
            L0_.nont = L
            self.stack.append(L0_)
            print " LE"

        elif(rule==r_L_GREATER_EQUAL ):
            R_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            L1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(L1_._.L.type,R_._.R.type)):
                print "Types does not match"

            L0_._.L.type = bool_
            L0_.nont = L
            self.stack.append(L0_)
            print " GE"

        elif(rule==r_L_EQUAL_EQUAL ):
            R_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            L1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(L1_._.L.type,R_._.R.type)):
                print "Types does not match"

            L0_._.L.type = bool_
            L0_.nont = L
            self.stack.append(L0_)
            print " EQ"

        elif(rule==r_L_NOT_EQUAL ):
            R_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            L1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(L1_._.L.type,R_._.R.type)):
                print "Types does not match"

            L0_._.L.type = bool_
            L0_.nont = L
            self.stack.append(L0_)
            print " NE"

        elif(rule==r_L_R ):
            R_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            L_._.L.type = R_._.R.type
            L_.nont = L
            self.stack.append(L_)

        elif(rule==r_R_PLUS ):
            K_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            R1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(R1_._.R.type,K_._.K.type)):
                print "Types does not match"


            if( not CheckTypes(R1_._.R.type,int_) and not CheckTypes(R1_._.R.type,string_)):
                print "Invalid Type"


            R0_._.R.type = R1_._.R.type
            R0_.nont = R
            self.stack.append(R0_)
            print " ADD"

        elif(rule==r_R_MINUS ):
            K_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            R1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(R1_._.R.type,K_._.K.type)):
                print "Types does not match"


            if( not CheckTypes(R1_._.R.type,int_)):
                print "Invalid Type"


            R0_._.R.type = R1_._.R.type
            R0_.nont = R
            self.stack.append(R0_)
            print " SUB"

        elif(rule==r_R_K ):
            K_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            R_._.R.type = K_._.K.type
            R_.nont = R
            self.stack.append(R_)

        elif(rule==r_K_TIMES ):
            F_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            K1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(K1_._.K.type,F_._.F.type)):
                print "Types does not match"


            if( not CheckTypes(K1_._.K.type,int_)):
                print "Invalid Type"


            K0_._.K.type = K1_._.K.type
            K0_.nont = K
            self.stack.append(K0_)
            print " MUL"

        elif(rule==r_K_DIVIDE ):
            F_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            K1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            if( not CheckTypes(K1_._.K.type,F_._.F.type)):
                print "Types does not match"


            if( not CheckTypes(K1_._.K.type,int_)):
                print "Invalid Type"


            K0_._.K.type = K1_._.K.type
            K0_.nont = K
            self.stack.append(K0_)
            print " DIV"

        elif(rule==r_K_F ):
            F_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            K_._.K.type = F_._.F.type
            K_.nont = K
            self.stack.append(K_)

        elif(rule==r_F_LV ):
            LV_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            n = LV_._.LV.type._.Type.nSize

            F_._.F.type = LV_._.LV.type
            F_.nont = F
            self.stack.append(F_)
            print " DE_REF {0}".format(n)

        elif(rule==r_F_LEFT_PLUS_PLUS ):
            LV_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            t = LV_._.LV.type
            if( not CheckTypes(t,int_)):
                print "Invalid Type"


            F_._.F.type = int_
            F_.nont = F
            print " DUP"
            print " DUP"
            print " DE_REF 1"
            print " INC"
            print " STORE_REF 1"
            print " DE_REF 1"
            self.stack.append(F_)

        elif(rule==r_F_LEFT_MINUS_MINUS ):
            LV_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            t = LV_._.LV.type
            if( not CheckTypes(t,int_)):
                print "Invalid Type"


            F_._.F.type = LV_._.LV.type
            F_.nont = F
            self.stack.append(F_)
            print " DUP"
            print " DUP"
            print " DE_REF 1"
            print " DEC"
            print " STORE_REF 1"
            print " DE_REF 1"

        elif(rule==r_F_RIGHT_PLUS_PLUS ):
            LV_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            t = LV_._.LV.type
            if( not CheckTypes(t,int_)):
                print "Invalid Type"

            F_._.F.type = LV_._.LV.type
            F_.nont = F
            self.stack.append(F_)
            print " DUP"
            print " DUP"
            print " DE_REF 1"
            print " INC"
            print " STORE_REF 1"
            print " DE_REF 1"
            print " DEC"

        elif(rule==r_F_RIGHT_MINUS_MINUS ):
            LV_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            t = LV_._.LV.type
            if( not CheckTypes(t,int_)):
                print "Invalid Type"


            F_._.F.type = t
            F_.nont = F
            self.stack.append(F_)
            print " DUP"
            print " DUP"
            print " DE_REF 1"
            print " DEC"
            print " STORE_REF 1"
            print " DE_REF 1"
            print " INC"

        elif(rule==r_F_PARENTHESIS_E ):
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            F_._.F.type = E_._.E.type
            F_.nont = F
            self.stack.append(F_)

        elif(rule==r_F_MINUS_F ):
            F1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            t = F1_._.F.type
            if( not CheckTypes(t,int_)):
                print "Invalid Type"


            F0_._.F.type = t
            F0_.nont = F
            self.stack.append(F0_)
            print " NEG"

        elif(rule==r_F_NOT_F ):
            F1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            t = F1_._.F.type
            if( not CheckTypes(t,bool_)):
                print "Invalid Type"


            F0_._.F.type = t
            F0_.nont = F
            self.stack.append(F0_)
            print " NOT"

        elif(rule==r_F_TRUE ):
            TRU_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            F_._.F.type = bool_
            F_.nont = F
            self.stack.append(F_)
            print " LOAD_TRUE"

        elif(rule==r_F_FALSE ):
            FALS_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            F_._.F.type = bool_
            F_.nont = F
            self.stack.append(F_)
            print " LOAD_FALSE"

        elif(rule==r_F_CHR ):
            CHR_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            F_._.F.type = char_
            F_.nont = F
            self.stack.append(F_)
            n = tokenSecundario
            print "LOAD_CONST {0}".format(n)

        elif(rule==r_F_STR ):
            STR_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            F_._.F.type = string_
            F_.nont = F
            self.stack.append(F_)
            n = tokenSecundario
            print " LOAD_CONST {0}".format(n)

        elif(rule==r_F_NUM ):
            STR_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            F_._.F.type = int_
            F_.nont = F
            self.stack.append(F_)
            n = tokenSecundario
            print " LOAD_CONST {0}".format(n)

        elif(rule==r_LV_DOT ):
            ID_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LV1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            t = LV1_._.LV.type
            if( t. eKind !=Kinds.STRUCT_TYPE_):
                if(t.eKind !=Kinds.UNIVERSAL_):
                    print "Struct Type Expected"

                LV0_._.LV.type = universal_

            else:
                p = t._.Struct.pFields
                while(p!=None):
                    if(p.nName == ID_._.ID.name):
                        break
                    p = p.pNext

                if(p == None):
                    print "Field not declared"
                    LV0_._.LV.type = universal_

                else:
                    LV0_._.LV.type = p._.Field.pType
                    LV0_._.LV.type._.Type.nSize = p._.Field.nSize



            LV0_.nont = LV
            self.stack.append(LV0_)
            print " ADD {0}".format(p._.Field.nIndex)

        elif(rule==r_LV_SQUARE ):
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LV1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            t = LV1_._.LV.type
            if(t == string_):
                LV0_._.LV.type = char_

            elif(t.eKind !=Kinds.ARRAY_TYPE_):
                if(t.eKind !=Kinds.UNIVERSAL_):
                    print "Array Kind Expected"

                LV0_._.LV.type = universal_

            else:
                LV0_._.LV.type = t._.Array.pElemType
                n = t._.Array.nSize/t._.Array.nNumElems
                print " MUL {0}".format(n)
                print " ADD"

            if( not CheckTypes(E_._.E.type,int_)):
                print "Index should be int"

            LV0_.nont = LV
            self.stack.append(LV0_)

        elif(rule==r_LV_IDU ):
            IDU_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()

            p = IDU_._.ID.obj
            if(p.eKind != Kinds.VAR_ and p.eKind != Kinds.PARAM_):
                if(p.eKind !=Kinds.UNIVERSAL_):
                    print "Expected var"

                LV_._.LV.type = universal_

            else:
                LV_._.LV.type = p._.Var.pType
                LV_._.LV.type._.Type.nSize = p._.Var.nSize

            LV_.nont = LV
            self.stack.append(LV_)
            print " LOAD_REF {0}".format(p._.Var.nIndex)

        elif(rule==r_MA ):
            print " DUP"

        elif(rule==r_E_LV_EQUAL ):
            E1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LV_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            if( not CheckTypes(LV_._.LV.type,E1_._.E.type)):
                print "Types does not match"


            E0_._.F.type = E1_._.E.type
            self.stack.append(E0_)
            print " STORE_REF {0}".format(t._.Type.nSize)
            print " DE_REF {0}".format(t._.Type.nSize)

        elif(rule==r_MC ):
            IDU_ = self.stack.__getitem__(self.stack.__len__()-1)
            f = IDU_._.ID.obj

            if(f.eKind != Kinds.FUNCTION_):
                print "Expected function"
                MC_._.MC.type = universal_
                MC_._.MC.param = None
                MC_._.MC.err = True

            else:
                MC_._.MC.type = f._.Function.pRetType
                MC_._.MC.param = f._.Function.pParams
                MC_._.MC.err = False

            MC_.nont = MC
            self.stack.append(MC_)

        elif(rule==r_LE_E ):
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            MC_ = self.stack.__getitem__(self.stack.__len__()-1)

            LE_._.LE.param = None
            LE_._.LE.err = MC_._.MC.err
            n = 1
            if( not MC_._.MC.err):
                p = MC_._.MC.param
                if(p == None):
                    print "Expected more arguments"
                    LE_._.LE.err = True

                else:
                    if(not CheckTypes(p._.Param.pType,E_._.E.type)):
                        print "Invalid Parameter Type"

                    LE_._.LE.param = p.pNext
                    LE_._.LE.n = n+1


            LE_.nont = LE
            self.stack.append(LE_)

        elif(rule==r_LE_LE ):
            E_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LE1_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            LE0_._.LE.param = None
            LE0_._.LE.err = L1_._.LE.err

            n = LE1_._.LE.n
            if(not LE1_._.LE.err):
                p = LE1_._.LE.param
                if(p == None):
                    print "Expected more arguments"
                    LE0_._.LE.err = True

                else:
                    if(not CheckTypes(p._.Param.pType,E_._.E.type)):
                        print "Invalid Parameter Type"

                    LE0_._.LE.param = p.pNext
                    LE0_._.LE.n = n + 1

            LE0_.nont = LE
            self.stack.append(LE0_)

        elif(rule==r_LE_EPSILON ):
            MC_ = self.stack.__getitem__(self.stack.__len__()-1)
            if(MC_._.MC.param != None):
                LE_._.LE.err = True

            else:
                LE_._.LE.err = False

            LE_._.LE.n = 0
            LE_._.LE.param = MC_._.MC.param
            LE_._.LE.type = universal_
            LE_.nont = LE
            self.stack.append(LE_)

        elif(rule==r_F_IDU_MC ):
            LE_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            MC_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            IDU_ = self.stack.__getitem__(self.stack.__len__()-1)
            self.stack.pop()
            f = IDU_._.ID.obj
            F_._.F.type = MC_._.MC.type
            if(not LE_._.LE.err):
                if(LE_._.LE.n-1 < f._.Function.nParams):
                    print "Expected more arguments"
                elif(LE_._.LE.n-1 > f._.Function.nParams):
                    print "Expected more arguments"

            F_.nont = F
            self.stack.append(F_)
            print " CALL {0}".format(f._.Function.nIndex)




