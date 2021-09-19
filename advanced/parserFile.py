from re import escape
from typing import Any, Callable
from tokenizer import Token, Tokenizer


class ParserHelper:
    def consume(self, l: "list[Token]") -> "list[Token]":
        return l[1:]

class Single(ParserHelper):
    def __init__(self, s:str) -> None:
        self.s = s
    def consume(self, l: "list[Token]") -> "list[Token] | bool":
        if len(l) > 0:
            if l[0].name == self.s:
                return l[1:]
        return False


class ParserRule:
    def __init__(self, parameters: "list[str | ParserHelper]",output:str ) -> None:
        def helper(i: "str | ParserHelper") -> ParserHelper:
            if type(i) is str:
                i = Single(i)
            return i
        self.parameters = list(map(helper, parameters))
        self.output  = output
    def doesMatch(self, inputLine: "list[Token]") -> bool:
        for param in self.parameters:
            t = param.consume(inputLine)
            if t is False:
                return False
            inputLine = t
        return len(inputLine) == 0
class AST:
    def __init__(self, name: str, value: Token, children: "list[AST]") -> None:
        self.name = name
        self.value  = value
        self.children = children
    def evaluate(self, funcs:"dict[str, Callable]") -> Any:
        if self.name not in funcs:
            raise ValueError(f'unhandled name {self.name}')
        evalled_children = list(map(lambda x: x.evaluate(funcs), self.children))
        func = funcs[self.name]
        return func(self.value, evalled_children)
# myRule = ParserRule(["digit", "operator", "digit"], "expression")

class Parser:
    def __init__(self, rules: "list[ParserRule]", tokenizer: Tokenizer) -> None:
        self.rules = rules
        self.tokenizer = tokenizer
    def runParser(self, tokens: "list[Token]") -> AST:
        if len(tokens) == 1:
            return AST(tokens[0].name, tokens[0], [])
        ast = None
        for t in range(len(tokens)):
            i = t+1
            for rule in self.rules:
                test= tokens[0:i]
                if rule.doesMatch(test):
                    tree = list(map(lambda x: AST(x.name, x, []), test))
                    remaining_tokens  = [Token(name=rule.output, value="".join(list(map(lambda x:x.value, test))))] + tokens[i:]
                    ast = self.runParser(remaining_tokens)
                    if ast is None: 
                        return None
                    else:
                        ast.children = tree
                        return ast
        return ast
    def parse(self, inputString:str ) -> AST:
        tokens = self.tokenizer.tokenize(inputString)
        return self.runParser(tokens)
        
