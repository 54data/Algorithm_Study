import string 
alp = input()

result = ''
alpha = string.ascii_lowercase
for i in alpha:
    result += str(alp.count(i)) + ' '
    
print(result)