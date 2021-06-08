from scanner import Scanner

scanner = Scanner('test.txt')
tokens = scanner.tokens

register = {}
print('.' + tokens[0].upper() + ':')

count = 0
index = 0
vtypeFlag = 0
plus = 0
plusindex = 0

for parse in tokens:
  if vtypeFlag == 1 :
    register[parse] = count
    vtypeFlag = 0
  if parse == "int" or parse == "char" :
    vtypeFlag = 1
    count += 1
  elif parse == '=':
    if tokens[index+2] != '+' and tokens[index+2] != '-': #선언 initialize
      print("    ADD $t", end='')
      print(register.get(tokens[index-1]), end='')
      if tokens[index+1].isalpha() == True:
        print(" $0 $t", end = '')
        print(register.get(tokens[index+1]))
      else:
        print(" $0 $" + tokens[index+1])
    else: #expr
      plusindex = index
      while(tokens[plusindex] != ';'):
        plusindex += 1
        if tokens[plusindex] == '-':
          tokens[plusindex] = '+'
          tokens[plusindex + 1] = '-' + tokens[plusindex + 1]
        if tokens[plusindex] == '+' or tokens[plusindex] == '-':
          plus += 1
      if plus > 1:
        print("    ADD $t", end='')
        count+=1
        print(count, end='')
        print(" $" + tokens[index+1] + " $" + tokens[index+3])
        if plus > 2:
          print("    ADD $t", end='')
          count+=1
          print(count, end='')
          print(" $t", end='')
          print(count-1, end='')
          print(" $" + tokens[index+5])
        if plus > 3 :
          for i in range(plus-3):
            print("    ADD $t", end='')
            count+=1
            print(count, end='')
            print(" $t", end='')
            print(count-1, end='')
            print(" $" + tokens[index+2*i+5])
        print("    ADD $t", end='')
        print(register.get(tokens[index-1]), end='')
        print(" $t", end = '')
        print(count, end = '')
        print(" $", end = '')
        print(tokens[index+2*plus+1])
      else:
        print("    ADD $t", end='')
        print(register.get(tokens[index-1]), end='')
        print(" $" + tokens[index+1] + " $" + tokens[index+3])
      plus = 0
  elif parse == "IF":
    print("    LT $t", end='')
    count+=1
    print(count)
    print("    JUMPF $t", end = '')
    print(count, end = '')
    print(" ELSE")
  elif parse == "ELSE":
    print(".ELSE")
  
  index += 1
