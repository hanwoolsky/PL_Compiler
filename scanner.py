import re

class Scanner:
    
    def __init__(self,target):

        self.f = open(target, "r")
        self.code = self.f.read()
        self.tokenzer()


    def tokenzer(self):

        self.code = self.code.replace("(", " ( ")
        self.code = self.code.replace(")", " ) ")
        self.code = self.code.replace("{", " { ")
        self.code = self.code.replace("}", " } ")
        self.code = self.code.replace(";", " ; ")
        self.code = self.code.replace("+", " + ")
        self.code = self.code.replace(">", " > ")
        self.code = self.code.replace("IF", " IF ")
        self.code = self.code.replace("THEN", " THEN ")
        self.code = self.code.replace("ELSE", " ELSE ")
        self.code = self.code.replace("EXIT", " EXIT ")

        self.tokens = self.code.split()

