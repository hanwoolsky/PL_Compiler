
class parsingTable:

    def __init__(self):
        self.Action = {
            #State 0
            (0,"int"):("S",5),
            (0,"char"):("S",6),
            (0,"IF"):("S",10),
            (0,"alpha"):("S",15),
            (0,"number"):("S",16),
            (0,"eps"):("S",3),
            (0,"{"):("S",7),
            (0,"EXIT"):("S",11),
            #State 1
            (1,"("):("S",17),
            (1,"ELSE"):("R",19),
            (1,"="):("S",18),
            #State 2
            (2,"int"):("S",5),
            (2,"char"):("S",6),
            (2,"eps"):("S",20),
            #State 3
            (3,"("):("R",2),
            (3,")"):("R",6),
            (3,"int"):("R",8),
            (3,"char"):("R",14),
            #State 4
            (4,"alpha"):("S",15),
            #state 5
            (5,"("):("R",4),
            #state 6
            (6,"("):("R",5),
            #state 7
            (7,"eps"):("S",23),
            #state 8
            (8,"IF"):("S",10),
            (8,"alpha"):("S",15),
            (8,"eps"):("S",26),
            (8,"EXIT"):("S",11),
            (8,"eps"):("S",26),
            #state 9
            (9,"("):("R",10),
            #state 10
            (10,"alpha"):("S",15),
            (10,"number"):("S",16),
            #state 11
            (11,"alpha"):("S",15),
            (11,"number"):("S",16),
            #state 12
            (12,"+"):("S",31),
            (12,">"):("S",30),
            #state 13
            (13 ,"("):("R",17),
            #state 14
            (14,"("):("R",18),
            #sate 15
            (15,"("):("R",21),
            #state 16
            (16,"("):("R",21),
            #state 17
            (17,")"):("S",32),
            #state 18
            (18,"alpha"):("S",15),
            (18,"number"):("S",16),
            #state 19
            (19,"("):("R",1),
            #state 20
            (20,"("):("R",6),
            #state 21
            (21,";"):("S",34),
            #state 22
            (22,"int"):("S",5),
            (22,"char"):("S",6),
            (22,"IF"):("S",10),
            (22,"eps"):("S",5),
            (22,"EXIT"):("S",11),
            #state 23
            (23,"("):("R",1),
            #state 24
            (24,"("):("R",6),
            #state 25
            (25,"="):("S",37),
            #state 26
            (26,"("):("R",14),
            #state 27
            (27,"THEN"):("S",38),
            #state 28
            (28,"("):("R",19),
            #state 29
            (29,"+"):("S",31),
            (29,";"):("S",39),
            #state 30
            (30,"alpha"):("S",15),
            (30,"number"):("S",16),
            #state 31
            (31,"alpha"):("S",15),
            (31,"number"):("S",16),
            #state 32
            (32,"eps"):("S",43),
            (32,"{"):("S",7),
            #state 33
            (33,"+"):("S",31),
            (33,">"):("S",30),
            (33,";"):("S",44),
            #state 34
            (34,"("):("R",3),
            #state 35
            (35,"IF"):("S",10),
            (35,"alpha"):("S",14),
            (35,"eps"):("S",26),
            (35,"}"):("S",45),
            (35,"EXIT"):("S",11),
            #state 36
            (36,"("):("R",6),
            (36,")"):("R",14),
            #state 37
            (37,"alpha"):("S",15),
            (37,"number"):("S",16),
            #state 38
            (31,"eps"):("S",43),
            (31,"{"):("S",7),
            #state 39
            (39,"("):("R",13),
            #state 40
            (40,"("):("R",15),
            (40,"+"):("S",31),
            #state 41
            (41,"("):("R",16),
            #state 42
            (42,"("):("R",0),
            #state 43
            (43,"("):("R",8),
            #state 44
            (44,"("):("R",12),
            #state 45
            (45,"("):("R",7),
            #state 46
            (46,"+"):("S",31),
            (46,";"):("S",48),
            #state 47
            (47,"ELSE"):("S",49),
            #state 48
            (48,"("):("R",12),
            #state 49
            (49,"+"):("eps",43),
            (49,"{"):("S",7),
            #state 50
            (50,"("):("R",11)
        }
        self.GOTO = {
            #state 0
            (0,"decls"):2,
            (0,"vtype"):4,
            (0,"slist"):8,
            (0,"stat"):9,
            (0,"expr"):12,
            (0,"fact"):13,
            (0,"word"):1,
            (0,"num"):14,
            #state 2
            (2,"decl"):19,
            (2,"vtype"):4,
            #state 4
            (4,"word"):21,
            #state 7
            (7,"decls"):22,
            #state 8
            (8,"stat"):24,
            (8,"word"):25,
            #state 10
            (10,"cond"):27,
            (10,"expr"):12,
            (10,"fact"):13,
            (10,"word"):28,
            (10,"num"):14,
            #state 11
            (11,"expr"):29,
            (11,"fact"):13,
            (11,"word"):28,
            (11,"num"):14,
            #state 18
            (18,"expr"):33,
            (18,"fact"):13,
            (18,"word"):28,
            (18,"num"):14,
            #state 22
            (22,"decl"):19,
            (22,"vtype"):4,
            (22,"slist"):35,
            (22,"stat"):9,
            (22,"word"):25,
            #state 30
            (30,"expr"):40,
            (30,"fact"):13,
            (30,"word"):28,
            (30,"num"):14,
            #state 31
            (31,"fact"):13,
            (31,"word"):28,
            (31,"num"):14,
            #state 32
            (32,"block"):42,
            #state 35
            (35,"stat"):24,
            (35,"word"):25,
            #state 37
            (37,"expr"):46,
            (37,"fact"):13,
            (37,"word"):28,
            (37,"num"):14,
            #state 38
            (38,"vtype"):47,
            #state 49
            (49,"vtype"):50
        }
        self.nonterminals = {
            "prog",
            "decls",
            "decl",
            "vtype",
            "block",
            "slist",
            "stat",
            "cond",
            "expr",
            "fact",
            "word",
            "num"
        }
        self.terminals = {
            "{",
            "}",
            "(",
            ")",
            "int",
            "char",
            "IF",
            "THEN"
            "ELSE",
            "ε",
            "$",
            "{",
            "}",
            "EXIT",
            "=",
            "+",
            ">",
            ";",

        }