
from arpeggio import EOF, OneOrMore, Optional, ParserPython, ZeroOrMore, \
    PTNodeVisitor, visit_parse_tree
from arpeggio import RegExMatch as _


def text() : return ZeroOrMore(paragraph), EOF

def paragraph() : return OneOrMore(line)

def line() : return _(r'[^\n]+')

def word() : return Optional("'"), _(r"\w+ "), Optional("'")

# quick test


# visitor

class TextVisitor(PTNodeVisitor):

    def visit_line(self, node, children) :
        return parser.pos_to_linecol(node.position) , ':' , str(node.value)
    


def main(debug=False):

    parser = ParserPython(text, debug=True)
    
    parse_tree = parser.parse("""install php \n
    sudo apt update \n
    
    """)

    result = visit_parse_tree(parse_tree, TextVisitor(debug=debug))

    print(result)





