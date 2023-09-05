from arpeggio import PTNodeVisitor
from app.modeles.upload_file import *
# from .csv_parsing_test import filename

class CsvVisitor(PTNodeVisitor):

    def visit_csv(self, node, children):
        # par_list = []
        # for child in children :
            # if child != '\n':
            #     par_list.append(child)

            # new version
            
        return "INsert {} records . This rule's name is {} !!!".format(len(children), node.rule_name)
    
    def visit_record(self, node, children):
        in_list = []
        for child in children :
            in_list.append(child)

        #new code goes there and use the list created by the last version
        # the loop bellow use enumerate function to get index as well as 
        # element value in a list and attribute it dynamically to variable    
        for i, elem in enumerate(in_list):
            globals()[f"l_{i}"] = elem

        # after creating variables which are accessible globaly
        # we'll use theme to make insert into table
        CSVSave2.insert_create2(l_0, l_1, l_2, l_3, l_4, name=self.filename)

        # return a
    
    def visit_field(self, node, children):
        return node.value
    
    
