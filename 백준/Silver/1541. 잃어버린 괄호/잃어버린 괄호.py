import re

exp = input()
exp = re.sub(r'\b0+(\d+)\b', r'\1', exp)

idxFirst = 0

while True:
    idxFirst = exp.find('-', idxFirst)
    if idxFirst == -1:
        break
    idxSecond = exp.find('-', idxFirst+1)
    
    if idxSecond == -1:
        exp = exp[0:idxFirst+1] + '(' + exp[idxFirst+1:] + ')'
        break
    else:
        exp = exp[0:idxFirst+1] + '(' + exp[idxFirst+1:idxSecond] + ')' + exp[idxSecond:]
    idxFirst = idxSecond+1

a = eval(exp)
print(a)