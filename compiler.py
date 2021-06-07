from scanner import Scanner

scanner = Scanner('test.txt')
tokens = scanner.tokens

register = {}
print('.' + tokens[0].upper() + ':')

count = 0
index = 0
vtypeFlag = 0
#register.get(tokens[index-1])

for parse in tokens:
  if vtypeFlag == 1 :
    register[parse] = count
    vtypeFlag = 0
  if parse == "int" or parse == "char" :
    vtypeFlag = 1
    count += 1
  if parse == '=' and tokens[index+2] != '+':
    print("    ADD $" + tokens[index-1] + " $0 $" + tokens[index+1])

  index += 1

print(register)