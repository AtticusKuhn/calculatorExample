import re
from typing import Any, Callable, Pattern

class Token:
    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value
    def show(self) -> str:
        return f'''
        name:{self.name}
        value: {self.value}
        '''
class Tokenizer:
    def __init__(self, tokens: "dict[Pattern[str], str]"):
        self.tokens = tokens
    def tokenize(self, string: str)-> "list[Token]":
        returning_tokens: "list[Token]" = []
        while len(string) > 0:
            correct  = False
            for (pattern, tokenName) in self.tokens.items():
                match = pattern.match(string, 0)
                if match is not None:
                    returning_tokens.append(Token(tokenName, match.group(0)))
                    string = string[match.end(0):]
                    correct = True
            if not correct:
                return returning_tokens
        return returning_tokens


            