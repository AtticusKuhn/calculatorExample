from parserFile import ParserRule
from parserFile import AST
from tokenizer import Tokenizer
import re
rule: ParserRule = ParserRule(["digit", "operator", "digit"], "expression")
rules = [rule]
tokenizer = Tokenizer({
    re.compile("\d"):"digit",
    re.compile("\+"):"operator"

})
e = rule.doesMatch(tokenizer.tokenize("1+1"))
print("e = ", e )
# myParser = Parser(rules, tokenizer)
# result: AST = myParser.parse("1+1")
# print("result =", result)