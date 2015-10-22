__author__ = 'Kaike'
from enum import Enum


possible_tokens = ['ARRAY', 'BOOLEAN', 'BREAK', 'CHAR', 'CONTINUE', 'DO', 'ELSE', 'FALSE', 'FUNCTION', 'IF', 'INTEGER', 'OF', 'STRING',
           'STRUCT', 'TRUE', 'TYPE', 'VAR', 'WHILE',
           'COLON', 'SEMI_COLON', 'COMMA', 'EQUALS', 'LEFT_SQUARE', 'RIGHT_SQUARE', 'LEFT_BRACES', 'RIGHT_BRACES',
           'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', 'AND', 'OR', 'LESS_THAN', 'GREATER_THAN', 'LESS_OR_EQUAL',
           'GREATER_OR_EQUAL', 'NOT_EQUAL', 'EQUAL_EQUAL', 'PLUS', 'PLUS_PLUS', 'MINUS', 'MINUS_MINUS', 'TIMES', 'DIVIDE',
           'DOT', 'NOT', 'CHARACTER', 'NUMERAL', 'STRINGVAL', 'ID',
           'UNKNOWN']

possible_tokens_ids = ['array', 'boolean', 'break', 'char', 'continue', 'do', 'else', 'false', 'function', 'if', 'integer', 'of', 'string',
             'struct', 'true', 'type', 'var', 'while', ':', ';', ',', '=', '[', ']', '"', '"', '(', ')', '&&', '||', '<', '>', '<=',
             '>=', '!=', '==', '+', '++', '-', '--', '*', '/', '.', '!', 'character', 'numeral', 'stringval', 'id']


Tokens = Enum._create_('Tokens', possible_tokens, None, int)