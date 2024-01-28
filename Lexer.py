import re


class Lexer:
    def __init__(self):
        self.grammar = ['final', 'int', 'identifier', '=', 'digit', ';']
        self.terminal_symbol = {'final', 'int', '=', ';'}
        self.identifier = r'[a-zA-Z][a-zA-Z0-9_]*'
        self.digit = r'\d+'
        self.tokens = []

    def check_tokens(self, tokens):
        self.tokens = ['-' if i not in tokens else i for i in self.grammar]
        return self.tokens

    def add_tokens(self, input_code):
        index = 1
        for word in re.findall(r'\w+|\S', input_code):
            if word in self.terminal_symbol:
                self.tokens.append(word)
                index += 1
            elif re.fullmatch(self.identifier, word):
                self.tokens.append('identifier')
                index += 1
            elif re.fullmatch(self.digit, word):
                self.tokens.append('digit')
                index += 1
            else:
                self.tokens.append('no match')

        self.check_tokens(self.tokens)

        return self.tokens
