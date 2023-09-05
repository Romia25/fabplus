from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython, visit_parse_tree

from visitor_calc import *
# from doc_things.calc_visit import *


def number():     return _(r'\d*\.\d*|\d+')
def factor():     return Optional(["+","-"]), [number, ("(", expression, ")")]
def term():       return factor, ZeroOrMore(["*","/"], factor)
def expression(): return term, ZeroOrMore(["+", "-"], term)
def calc():       return OneOrMore(expression), EOF

#visitor
parser = ParserPython(calc, debug=False)   # calc is the root rule of your grammar

input =  "-(4-1)*5+(2+4.67)+5.89/(.2+7)"                        
parse_tree = parser.parse("2+5+3-4")

print(parse_tree.tree_str())

result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))



print(result)

# print(" helo", "\n \n", 'hi')

