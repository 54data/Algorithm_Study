strings = input()
stack = []
str_dict = {')':'(', ']':'['}
value_dict = {')':2, ']':3}

for i in strings:
    if i not in ['(', ')', '[', ']']:
        break
    if stack and i in str_dict.keys():
        if type(stack[-1]) == str and stack[-1] == str_dict[i]:
            stack.pop(-1)
            stack.append(value_dict[i])
        elif type(stack[-1]) == int and len(stack)>=2 and stack[-2] == str_dict[i]:
            stack.pop(-2)
            stack.append(stack.pop(-1) * value_dict[i])
        else:
            stack.append(i)
    else:
        stack.append(i)
    if len(stack)>=2 and type(stack[-1]) == int and type(stack[-2]) == int:
        stack.append(stack.pop(-1)+stack.pop(-1))

if len(stack)==1 and type(stack[-1]) == int:
    print(stack[-1])
else:
    print(0)