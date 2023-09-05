from .csv_grammar_line import *
from .csv_visitor import *
from arpeggio import ParserPython, visit_parse_tree
from pathlib import Path



# parser = ParserPython(csv, ws = '\t ', debug=True)

# fn = Path('/home/linda/Documents/flask_app_builder/fab_arpeggio_integration/arpeggios/test_data.csv')
# filename = str(fn.relative_to(fn.parent))

# test_data = open('/home/linda/Documents/flask_app_builder/fab_arpeggio_integration/arpeggios/test_data.csv', 
#     'r').read()

# pars_tree = parser.parse(test_data)

# restat = visit_parse_tree(pars_tree, CsvVisitor(), name=filename)

# print(restat)