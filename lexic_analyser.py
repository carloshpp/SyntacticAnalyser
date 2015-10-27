__author__ = 'Kaike'
import tokens

# add comments do the project
class lexicAnalyser():

    def __init__(self):
        self.code = ""
        self.i = 0
        self.names = []
        self.Consts = []


    def _setCode(self, _code):
        self.code = _code
        if len(self.code) == 0:
            self.nextChar = ""
        else:
            self.nextChar = " "
        i = 0;

    def compile(self,_code):
        self._setCode(_code)
        while self.i <= self.code.__len__():
            self.Consts.append(self.nextToken())



    def nextToken(self):
        tokenSec = "NO SECONDARY TOKEN"
        text = ""
        token = 0

        while(self.isSpace(self.nextChar) or self.nextChar == '\n'):
            self.nextChar = self.readChar()

        if self.nextChar.isalpha():
            while True:
                text += self.nextChar
                self.nextChar = self.readChar()
                if (not self.nextChar.isalnum()) and self.nextChar != "_":
                    break

            # Enum token goes from 1 to n, but an array goes from 0 to n-1
            token = tokens.searchKeyWord(text)

            if(token == tokens.Tokens.ID.value):
                tokenSec = self.searchName(text)
            print '{0} {1} {2}'.format(tokens.Tokens(token).name,token,tokenSec)


        elif self.isNumeric(self.nextChar):
            num = ""
            while True:
                num += self.nextChar
                self.nextChar = self.readChar()
                if not self.isNumeric(self.nextChar):
                    break

            token = tokens.Tokens.NUMERAL.value
            tokenSec = num
            print '{0} {1} {2}'.format(tokens.Tokens(token).name,token,tokenSec)

        elif self.nextChar == '"':
            text = ""
            self.nextChar = self.readChar()
            while True:
                text += self.nextChar
                self.nextChar = self.readChar()
                if self.nextChar == '"':
                    break
            token = tokens.Tokens.STRING.value
            tokenSec = text
            print '{0} {1} {2}'.format(tokens.Tokens(token).name,token, tokenSec)
            self.nextChar = self.readChar()
        else:
            if self.nextChar == '\'':
                self.nextChar = self.readChar()
                token = tokens.Tokens.CHARACTER.value
                tokenSec = self.addCharConst(self.nextChar)
                self.nextChar = self.readChar()
                self.nextChar = self.readChar()

            elif self.nextChar == ':':
                self.nextChar =self.readChar()
                token = tokens.Tokens.COLON.value
                print ': {0} {1}'.format(token, tokenSec)

            elif self.nextChar == ';':
                self.nextChar = self.readChar()
                token = tokens.Tokens.SEMI_COLON.value
                print '; {0} {1}'.format(token, tokenSec)

            elif self.nextChar == ',':
                self.nextChar = self.readChar()
                token = tokens.Tokens.COMMA.value
                print ', {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '=':
                self.nextChar = self.readChar()
                token = tokens.Tokens.EQUALS.value
                print '= {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '[':
                self.nextChar = self.readChar()
                token = tokens.Tokens.LEFT_SQUARE.value
                print '[ {0} {1}'.format(token, tokenSec)

            elif self.nextChar == ']':
                self.nextChar = self.readChar()
                token = tokens.Tokens.RIGHT_SQAURE.value
                print '] {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '{':
                self.nextChar = self.readChar()
                token = tokens.Tokens.LEFT_BRACES.value
                print "{ "+"{0} {1}".format(token, tokenSec)

            elif self.nextChar == '}':
                self.nextChar = self.readChar()
                token = tokens.Tokens.RIGHT_BRACES.value
                print "} "+ '{0} {1}'.format(token, tokenSec)

            elif self.nextChar == '(':
                self.nextChar = self.readChar()
                token = tokens.Tokens.LEFT_PARENTHESIS.value
                print '( {0} {1}'.format(token, tokenSec)

            elif self.nextChar == ')':
                self.nextChar = self.readChar()
                token = tokens.Tokens.RIGHT_PARENTHESIS.value
                print ') {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '&&':
                self.nextChar = self.readChar()
                token = tokens.Tokens.AND.value
                print '&& {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '||':
                nextChar = self.readChar()
                token = tokens.Tokens.OR.value
                print '|| {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '<':
                self.nextChar = self.readChar()
                token = tokens.Tokens.LESS_THAN.value
                print '< {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '>':
                self.nextChar = self.readChar()
                token = tokens.Tokens.GREATER_THAN.value
                print '> {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '<=':
                self.nextChar = self.readChar()
                token = tokens.Tokens.LESS_OR_EQUAL.value
                print '<= {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '>=':
                self.nextChar = self.readChar()
                token = tokens.Tokens.GREATER_OR_EQUAL.value
                print '>= {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '!=':
                self.nextChar = self.readChar()
                token = tokens.Tokens.NOT_EQUAL.value
                print '!= {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '==':
                self.nextChar = self.readChar()
                token = tokens.Tokens.EQUAL_EQUAL.value
                print '== {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '+':
                self.nextChar = self.readChar()
                if self.nextChar == '+':
                    token = tokens.Tokens.PLUS_PLUS.value
                    self.nextChar = self.readChar()
                    print '++ {0} {1}'.format(token, tokenSec)
                else:
                    token = tokens.Tokens.PLUS.value
                    print '+ {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '-':
                self.nextChar = self.readChar()
                if self.nextChar == '-':
                    token = tokens.Tokens.MINUS_MINUS.value
                    self.nextChar = self.readChar()
                    print '-- {0} {1}'.format(token, tokenSec)
                else:
                    token = tokens.Tokens.MINUS.value
                    print '- {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '*':
                self.nextChar = self.readChar()
                token = tokens.Tokens.TIMES.value
                print '* {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '/':
                self.nextChar = self.readChar()
                token = tokens.Tokens.DIVIDE.value
                print '/ {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '.':
                self.nextChar = self.readChar()
                token = tokens.Tokens.DOT.value
                print '. {0} {1}'.format(token, tokenSec)

            elif self.nextChar == '!':
                self.nextChar = self.readChar()
                token = tokens.Tokens.NOT.value
                print '! {0} {1}'.format(token, tokenSec)
            elif self.nextChar == '$':
                self.nextChar = self.readChar()
                token = tokens.Tokens.DOLAR.value
                print '! {0} {1}'.format(token, tokenSec)
            else:
                token = tokens.Tokens.UNKNOWN.value

        return token


    def isSpace(self, char):
        return " " == char

    def searchName(self, name):
        if not self.names.__contains__(name):
            self.names.append(name)
        return name

    def readChar(self):
        self.i += 1
        if self.i <= len(self.code):
            return self.code[self.i-1]
        return "\0"

    def isNumeric(self,ch):
        try:
            float(ch)
            return True
        except ValueError:
            return False

