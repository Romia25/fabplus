from arpeggio import OneOrMore, EOF, \
    ZeroOrMore 
from arpeggio import RegExMatch as _

def csv():
    return OneOrMore([record, '\n']), EOF

def record():
    return field, ZeroOrMore(",", field)

def field():
    return [quoted_field, field_content]

def field_content():
    return _(r'([^,\n])+')

