__author__ = 'Kaike'
from enum import Enum


possible_tokens = ['ARRAY', 'BOOLEAN', 'BREAK', 'CHAR', 'CONTINUE', 'DO', 'ELSE', 'FALSE', 'FUNCTION', 'IF', 'INTEGER', 'OF', 'STRING',
           'STRUCT', 'TRUE', 'TYPE', 'VAR', 'WHILE',
           'COLON', 'SEMI_COLON', 'COMMA', 'EQUALS', 'LEFT_SQUARE', 'RIGHT_SQUARE', 'LEFT_BRACES', 'RIGHT_BRACES',
           'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', 'AND', 'OR', 'LESS_THAN', 'GREATER_THAN', 'LESS_OR_EQUAL',
           'GREATER_OR_EQUAL', 'NOT_EQUAL', 'EQUAL_EQUAL', 'PLUS', 'PLUS_PLUS', 'MINUS', 'MINUS_MINUS', 'TIMES', 'DIVIDE',
           'DOT', 'NOT', 'CHARACTER', 'NUMERAL', 'STRINGVAL', 'ID','DOLAR',
           'UNKNOWN']

possible_tokens_ids = ['array', 'boolean', 'break', 'char', 'continue', 'do', 'else', 'false', 'function', 'if', 'integer', 'of', 'string',
             'struct', 'true', 'type', 'var', 'while', ':', ';', ',', '=', '[', ']', '"', '"', '(', ')', '&&', '||', '<', '>', '<=',
             '>=', '!=', '==', '+', '++', '-', '--', '*', '/', '.', '!', 'character', 'numeral', 'stringval', 'id','$']


Tokens = Enum._create_('Tokens', possible_tokens, None, int)

def searchKeyWord(text):
    if possible_tokens_ids.__contains__(text.lower()):
        return possible_tokens_ids.index(text.lower())+1
    else:
        return Tokens.ID.value

def searchName(text):
    if possible_tokens.__contains__(text.upper()):
        return possible_tokens.index(text.upper())
    else:
        return -1


