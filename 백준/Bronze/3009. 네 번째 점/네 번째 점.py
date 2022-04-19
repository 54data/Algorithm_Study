result_x = []
result_y = []
for i in range(0, 3):
    a, b = map(int, input().split())
    result_x.append(a)
    result_y.append(b)

if result_x[0] == result_x[1]:
    num_x = result_x[2]
elif result_x[0] == result_x[2]:
    num_x = result_x[1]
else:
    num_x = result_x[0]
    
if result_y[0] == result_y[1]:
    num_y = result_y[2]
elif result_y[0] == result_y[2]:
    num_y = result_y[1]
else:
    num_y = result_y[0]
    
print(num_x, num_y)