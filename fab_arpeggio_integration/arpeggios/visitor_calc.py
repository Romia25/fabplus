from arpeggio import PTNodeVisitor


class CalcVisitor(PTNodeVisitor):


    def visit_number(self, node, children):
        return float(node.value)

    def visit_factor(self, node, children):
        if len(children) == 1:
            return float(children[0])
        sign = -1 if children[0] == '-' else 1
        return float(sign * children[-1])
        # return node

    # try to write remaining visitor methods for calc grammar
    def visit_term(self, node, children): #rajoujter egalement le test len de children
        if len(children) == 1:
            return float(children[0])
        child = children[0]
        if children[1] == '*' :
            return float(child * children[-1])
        if children[1] == '/' :
            return float(child / children[-1])
        # return node

    def visit_expression(self, node, children):
        # if len(children) == 1 :
        #     return children[0]
        a = self.node.rule_name
        terms = 0
        s = 0
        if str(children[0]) in "+-":
            s = 1
        
        n = len(children) 
        for i in range(s-1, n, 2):
            if children[i] == '-' :
                terms -= float(children[i+1])
            else :
                terms += float(children[i+1])
        return float(terms)
        # return node

    
