import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$','?']
temp_SYMBOLS = SYMBOLS.copy()

li = list()
#generate 8 chars from first 3 lists
for i in range(8):
    pass
    li.append(random.choice(UPCASE_CHARACTERS+LOCASE_CHARACTERS+DIGITS))

#2nd condition : each of symbols must be in li(password) AT RANDOM POSITION AND RANDOM IN ORDER
for ini in range(4):
    #get each random from SYMBOLS as i
    for i in random.choice(temp_SYMBOLS):
        #if i is not in li then insert at RANDOM POSITION RANDOM SYMBOL
        #RANDOM POSITION : random.randint(0,len(li)) > RANDOM ELEMENT = i
        #then REMOVE i (random symbol) from SYMBOL list
        if i not in li:
            li.insert(random.randint(0,len(li)),i)
            temp_SYMBOLS.remove(i)
        else:
            break

print(''.join(li))
print(temp_SYMBOLS,SYMBOLS)