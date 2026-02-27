import re
from enum import Enum

# Token types enumeration
class TokenType(Enum):
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    OPERATOR = 'OPERATOR'
    PARENTHESIS = 'PARENTHESIS'
    WHITESPACE = 'WHITESPACE'
    COMMENT = 'COMMENT'
    EOF = 'EOF'

# Token class
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'

# Lexer class for tokenization
class Lexer:
    keywords = {'if', 'else', 'while', 'for', 'def', 'class', 'return', 'import', 'from', 'as', 'with'}

    def __init__(self, input_text):
        self.input_text = input_text
        self.position = 0
        self.current_char = self.input_text[self.position] if self.input_text else None

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.position += 1
        if self.position > len(self.input_text) - 1:
            self.current_char = None
        else:
            self.current_char = self.input_text[self.position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        token_type = TokenType.KEYWORD if result in self.keywords else TokenType.IDENTIFIER
        return Token(token_type, result)

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))

    def string(self):
        result = ''
        self.advance()  # skip starting quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # skip ending quote
        return Token(TokenType.STRING, result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self.identifier()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == '"':
                return self.string()

            if self.current_char in '+-*/=<>':
                token = Token(TokenType.OPERATOR, self.current_char)
                self.advance()
                return token

            if self.current_char == '(' or self.current_char == ')':
                token = Token(TokenType.PARENTHESIS, self.current_char)
                self.advance()
                return token

            self.error()

        return Token(TokenType.EOF, None)

# Example usage
if __name__ == '__main__':
    code = 'def my_function(a, b): return a + b'
    lexer = Lexer(code)
    token = lexer.get_next_token()
    while token.type != TokenType.EOF:
        print(token)
        token = lexer.get_next_token()