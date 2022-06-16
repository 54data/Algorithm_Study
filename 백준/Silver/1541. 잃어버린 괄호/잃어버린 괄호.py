num_list = input()
num_list = num_list.split('-')

result = ''

for i in num_list:
    n_sum = 0
    for x in i.split('+'):
        n_sum += int(x)
    result += str(n_sum)
    result += '-'
        
if result[-1] == '-':
    result = result[:-1]
    
print(eval(result))