from typing import Any
from tokenizer import Token, Tokenizer


class ParserHelper:
    def consume(self, l: "list[Token]") -> "list[Token]":
        return l[1:]

class Single(ParserHelper):
    def __init__(self, s:str) -> None:
        self.s = s
    def consume(self, l: "list[Token]") -> "list[Token] | bool":
        if len(l) > 0:
            print("l[0].name:", l[0].name)
            print("self.s:",self.s)
            if l[0].name == self.s:
                return l[1:]
        print("failing to consume because l is", l)
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
            print("before, inputLine is", inputLine)
            t = param.consume(inputLine)
            if not t:
                return False
            inputLine = t
            print("inputLine is now", inputLine)
        print("at end, inputLine:", inputLine)
        return len(inputLine) == 0
class AST:
    def __init__(self, name: str, value: Any, children: "list[AST]") -> None:
        self.name = name
        self.value  = value
        self.children = children
myRule = ParserRule(["digit", "operator", "digit"], "expression")

class Parser:
    def __init__(self, rules: "list[ParserRule]", tokenizer: Tokenizer) -> None:
        self.rules = rules
        self.tokenizer = tokenizer
    def runParser(self, tokens: "list[Token]") -> AST:
        if len(tokens) == 1:
            return AST(tokens[0].name, None, [])
        print("runParser called with tokens", tokens)
        ast = None
        for t in range(len(tokens)):
            i = t+1
            for rule in self.rules:
                test= tokens[0:i]
                if rule.doesMatch(test):
                    print("rule matches")
                    print("test is",test)
                    print("i is", i)
                    # print("Token(name=rule.output, value=test)", Token(name=rule.output, value=test).show())
                    # print("tokens matching", "\n".join(list(map(lambda x :x.show(), test))))
                    # print("tokens remaining",  tokens[i:])
                    # rest_of_tokens = tokens[i:]
                    # if len(rest_of_tokens) == 1:
                    #     e = rest_of_tokens[0]
                    #     return AST(e.name, None, [])
                    tree = AST(rule.output, None, test)
                    # print("rest_of_tokens = ", rest_of_tokens)
                    remaining_tokens  = [rule.output] + tokens[i:]
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
        
