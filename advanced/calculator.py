from parserFile import Parser, ParserRule
from parserFile import AST
from tokenizer import Token, Tokenizer
from typing import List
import re
rule: ParserRule = ParserRule(["digit", "operator", "digit"], "expression")
rules = [rule]
tokenizer = Tokenizer({
    re.compile("\d"):"digit",
    re.compile("\+"):"operator"

})
myParser = Parser(rules, tokenizer)

def parseExpression(value:Token, children: List[AST]) -> int:
    return children[0] + children[2]
def parseDigit(value: Token, children: List[AST]) -> str:
    return int(value.value)
def parseOperator(value:Token, children: List[AST]) -> None:
    return None
def solve(problem:str) -> int:
    result: AST = myParser.parse(problem)
    evalled = result.evaluate({
        "expression": parseExpression,
        "digit": parseDigit,
        "operator": parseOperator

    })
    return evalled
