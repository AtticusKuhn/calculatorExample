from parserFile import Parser, ParserRule
from parserFile import AST
from tokenizer import Token, Tokenizer
from typing import List
import re
rule: ParserRule = ParserRule(["number", "operator", "number"], "expression")
# rule: ParserRule = ParserRule(["expression"], "number")

rules = [rule]
tokenizer = Tokenizer({
    re.compile("\d+"):"number",
    re.compile("\+"):"operator"

})
myParser = Parser(rules, tokenizer)

def parseExpression(value:Token, children: List[AST]) -> int:
    return children[0] + children[2]
def parseDigit(value: Token, children: List[AST]) -> str:
    return int(value.value)
def parseOperator(value:Token, children: List[AST]) -> None:
    return children
def solve(problem:str) -> int:
    result: AST = myParser.parse(problem)
    evalled = result.evaluate({
        "expression": parseExpression,
        "number": parseDigit,
        "operator": parseOperator

    })
    return evalled
