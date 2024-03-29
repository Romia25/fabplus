#######################################################################
# Name: calc.py
# Purpose: Simple expression evaluator example
# Author: Igor R. Dejanovic <igor DOT dejanovic AT gmail DOT com>
# Copyright: (c) 2009-2015 Igor R. Dejanovic <igor DOT dejanovic AT gmail DOT com>
# License: MIT License
#
# This example demonstrates grammar definition using python constructs as
# well as using semantic actions to evaluate simple expression in infix
# notation.
#######################################################################

from __future__ import unicode_literals, print_function
try:
    text=unicode
except:
    text=str

from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF, \
    ParserPython, PTNodeVisitor, visit_parse_tree
from arpeggio import RegExMatch as _

def number():     return _(r'\d*\.\d*|\d+')
def factor():     return Optional(["+","-"]), [number,
                          ("(", expression, ")")]
def term():       return factor, ZeroOrMore(["*","/"], factor)
def expression(): return term, ZeroOrMore(["+", "-"], term)
def calc():       return OneOrMore(expression), EOF


class CalcVisitor(PTNodeVisitor):

    rules_list = []
    rule_occurrences = {}

    def visit_number(self, node, children):
        """
        Converts node value to float.
        """
        if self.debug:
            print("Converting {}.".format(node.value))
        self.rules_list.append(node.rule_name)
        self._update_occurrences(node.rule_name)
        return float(node.value)

    def visit_factor(self, node, children):
       """
       Applies a sign to the expression or number.
       """
       if self.debug:
           print("Factor {}".format(children))
       if len(children) == 1:
           return children[0]
       sign = -1 if children[0] == '-' else 1
       self.rules_list.append(node.rule_name)
       self._update_occurrences(node.rule_name)
       return sign * children[-1]

    def visit_term(self, node, children):
        """
        Divides or multiplies factors.
        Factor nodes will be already evaluated.
        """
        if self.debug:
            print("Term {}".format(children))
        term = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "*":
                term *= children[i]
            else:
                term /= children[i]
        if self.debug:
            print("Term = {}".format(term))
        self.rules_list.append(node.rule_name)
        self._update_occurrences(node.rule_name)
        return term

    def visit_expression(self, node, children):
        """
        Adds or subtracts terms.
        Term nodes will be already evaluated.
        """
        if self.debug:
            print("Expression {}".format(children))
        expr = children[0]
        for i in range(2, len(children), 2):
            if i and children[i - 1] == "-":
                expr -= children[i]
            else:
                expr += children[i]
        if self.debug:
            print("Expression = {}".format(expr))
        self.rules_list.append(node.rule_name)
        self._update_occurrences(node.rule_name)
        return expr
    
    def _update_occurrences(self, rule_name):
        if rule_name in self.rule_occurrences:
            self.rule_occurrences[rule_name] += 1
        else:
            self.rule_occurrences[rule_name] = 1


def main(debug=False):
    # First we will make a parser - an instance of the calc parser model.
    # Parser model is given in the form of python constructs therefore we
    # are using ParserPython class.
    parser = ParserPython(calc, debug=debug)

    # rule_names = parser['calc'].get_ordered_rule_names()


    # An expression we want to evaluate
    input_expr = "1 + 2 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + ((((((11 * 12 * -13 * 14 * 15 + 16 * 17 + 18 * 19 * 20))))))"
    #"-(4-1)*5+(2+4.67)+5.89/(.2+7)"

    # We create a parse tree out of textual input_expr
    parse_tree = parser.parse(input_expr)

    # The result is obtained by semantic evaluation using visitor class.
    # visit_parse_tree will start semantic analysis.
    # In this case semantic analysis will evaluate expression and
    # returned value will be evaluated result of the input_expr expression.
    result = visit_parse_tree(parse_tree, CalcVisitor(debug=debug))

    # Check that result is valid
    #assert (result - -7.51194444444) < 0.0001

    print("{} = {}".format(input_expr, result))
    print("rules names are {}".format(CalcVisitor.rules_list))
    print("rules occurrence is {}".format(CalcVisitor.rule_occurrences))

if __name__ == "__main__":
    # In debug mode dot (graphviz) files for parser model
    # and parse tree will be created for visualization.
    # Checkout current folder for .dot files.
    main(debug=True)