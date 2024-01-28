class Syntax_analyzer:
    def __init__(self):
        self.grammar = ['final', 'int', 'identifier', '=', 'digit', ';']
        self.errors = []

    def add_error(self, error):
        return self.errors.append(error)

    def analyzer(self, tokens):
        if tokens[0] != self.grammar[0]:
            self.add_error('некорректное начало модификатора, ожидалось "final"')

        if tokens[1] != self.grammar[1]:
            self.add_error('некорректно определен тип переменной, ожидалось "int"')

        if tokens[2] != self.grammar[2]:
            self.add_error('некорректно заданная переменная')

        if tokens[3] != self.grammar[3]:
            self.add_error('отсутствует знак присваивания (=) после переменной')

        if tokens[4] != self.grammar[4]:
            self.add_error('некорректное выражение в правой части метода')

        if tokens[5] != self.grammar[5]:
            self.add_error('пропущено окончание выражения (;)')

        return self.errors
