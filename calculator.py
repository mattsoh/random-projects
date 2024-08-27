def isNumber(num):
    if num == '' or num == '-':
        return False
    return num.isdigit() or num[0] == '-' and num[1:].isdigit()

def findB(exp):
    stack = []
    for i,c in enumerate(exp):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 1:
                return stack.pop(), i
            stack.pop()
    return -1, -1

def brackets(exp):
    while findB(exp) != (-1, -1):
        firstB, lastB = findB(exp)
        if firstB != -1:
            exp[firstB] = eval(exp[firstB+1:lastB])
            del exp[firstB+1:lastB+1]
    return exp

def simplify(exp):
    i = 0
    while i < len(exp):
        print(exp)
        if exp[i] == '-' and exp[i+1] == '-':
            exp.pop(i+1)
            if i > 0:
                exp[i] = '+'
            else:
                exp.pop(i)
        elif exp[i] == '-':
            exp[i+1] = -float(exp[i+1])
            if type(exp[i-1]) == float and i > 0:
                exp[i] = '+'
            else:
                exp.pop(i)
        elif type(exp[i]) != float and isNumber(exp[i]):
            exp[i] = float(exp[i])
        i+=1
    return exp

def MoD(exp):
    i = 0
    while i < len(exp):
        if exp[i] == '*':
            exp[i-1] = float(exp.pop(i-1)) * float(exp.pop(i))
        elif exp[i] == '/':
            exp[i-1] = float(exp.pop(i-1)) / float(exp.pop(i))
        else:
            i += 1
    return exp

def AoS(exp):
    i = 0
    while i < len(exp):
        if exp[i] == '-':
            exp[i-1] = float(exp.pop(i-1)) - float(exp.pop(i))
        elif exp[i] == '+':
            exp[i-1] = float(exp.pop(i+1)) + float(exp.pop(i-1))
        else:
            i += 1
    return exp

def eval(exp):
    return AoS(MoD(simplify(brackets(re.findall(r'-?\d*\.?\d+|\S', exp)))))[0]
