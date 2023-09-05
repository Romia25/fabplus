

from arpeggio import PTNodeVisitor


class CalcVisitor(PTNodeVisitor):

    def visit_number(self, node, children):
        """
        Converts node value to float.
        """
        return float(node.value)
    
    def visit_factor(self, node, children):
        """
        Applies a sign to the expression or number.
        """
        if len(children) == 1:
            return children[0]
        sign = -1 if children[0] == '-' else 1
        return sign * children[-1]
    
    def visit_term(self, node, children):
        """
        Divides or multiplies factors.
        Factor nodes will be already evaluated.
        """
        term = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "*":
                term *= children[i]
            else:
                term /= children[i]
        return term
    
    def visit_expression(self, node, children):
        """
        Adds or subtracts terms.
        Term nodes will be already evaluated.
        """
        expr = 0
        start = 0
        # Check for unary + or - operator
        if str(children[0]) in "+-":
            start = 1

        for i in range(start, len(children), 2):
            if i and children[i - 1] == "-":
                expr -= children[i]
            else:
                expr += children[i]

        return expr
