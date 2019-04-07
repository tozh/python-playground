import re

string = '14+(24+8)/16+(45+55)*3'
# string = '2*(3+1)'
def to_polish(s):
    result = []
    stack = []
    pattern = r'[*+-/()]+'
    tempsplit = re.split(pattern, s)
    split = []
    for t in tempsplit:
        if t:
            split.append(t)
    print(split)
    j = len(split)-1
    i = len(s)-1
    while i >= 0 and j >= 0:
        if re.match(r'[0-9]', s[i]):
            result.append(split[j])
            j -= 1
            while not re.match(r'[*\-+/()]', s[i]):
                i -= 1
        else: # operator or parentheses
            if s[i] == '-' or s[i] == '+':
                while len(stack) != 0 and (stack[-1] == '*' or stack[-1] == '/'):
                    result.append(stack.pop())
                stack.append(s[i])
            elif s[i] == '*' or s[i] == '/':
                stack.append(s[i])
            elif s[i] == ')':
                stack.append(s[i])
            else:
                while len(stack) !=0 and stack[-1] != ')':
                    result.append(stack.pop())
                stack.pop()
            i -= 1
    while len(stack) != 0:
        result.append(stack.pop())
    print(result)
    return result[::-1]

def calculate_polish(p):
    stack = []
    print(p)
    result = 0
    for i in range(len(p)-1, -1, -1):
        if re.match('[0-9]+', p[i]):
            stack.append(p[i])
        else:
            left = int(stack.pop())
            right = int(stack.pop())
            if p[i]=='+':
                result = left+right
            elif p[i] == '-':
                result = left-right
            elif p[i]=='*':
                result = left*right
            else:
                result = left/right
            stack.append(result)
    print(result)
    return result

polish = to_polish(string)

calculate_polish(polish)

