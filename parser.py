from scanner import Scanner
from parsingtable import parsingTable


class grammar:
    def __init__(self,RHS_s,LHS_s):
        
        self.RHS = RHS_s.strip()
        self.LHS = LHS_s.split()
        
    

class parser:
    
    def __init__(self, tokens, Tables, grammarF):
        
        self._tokens = []
        for token in tokens:
            self._tokens.append(token)
        self._tokens.append("$")
        self._parsTbl = Tables

        self.stack = []
        self.action=[]

        self.grammarlist = []

        for line in grammarF.readlines():
            prod = line.split('->')
            RHS = prod[0].strip()

            if RHS == "word":
                LHS = "alpha"
            elif RHS == "num":
                LHS = "number"
            else:
                LHS = prod[1]

            for syms in LHS.split('|'):
                gram = grammar(RHS,syms)
                self.grammarlist.append(gram)
        
        self.parse()
        
    def parse(self):

        cur = 0
        state = 0
        self.stack.append(state)
        symbol = ""

        while(True):
            
            inFirst = self._tokens[cur]
            state = self.stack.pop(-1)

            
            if inFirst not in self._parsTbl.nonterminals:
                if inFirst not in self._parsTbl.terminals:
                    if inFirst.isdigit():

                        inFirst = "number"
                    else:

                        inFirst = "alpha"  
                      
            try:
                (action, target) = self._parsTbl.Action[(state,inFirst)]
            except KeyError:
                print("No Action defined on state : " + str(state) + " input : " + inFirst)
                return 0

            if action == "R":
                gramIdx = target - 1
                symbol = self.grammarlist[gramIdx].RHS
                try:
                    self.stack.append(self._parsTbl.GOTO[( state ,symbol)])
                except KeyError:
                    print("No GOTO defined on state : " + str(state) + " symbol : " + symbol)
                    return 0

            elif action == "S":
                self.stack.append(target)
                symbol = inFirst
                cur += 1

        

    

    def shift(self, state):
        
        self.stack.append(state)

    def reduce(self, grammar):
        pass


gramF = open("grammar.txt","rt")

scanner = Scanner("test.txt")
parseTbl = parsingTable()
myParser  = parser(scanner.tokens,parseTbl,gramF)

    
    