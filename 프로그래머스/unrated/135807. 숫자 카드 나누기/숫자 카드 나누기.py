import math

def get_gcd(arr):       
    g = arr[0]
    for i in range(1, len(arr)):
        g = math.gcd(g, arr[i])     
    return g

def solution(arrayA, arrayB):
    answer = 0
    stat1, stat2 = True, True
    arrayA, arrayB = sorted(arrayA), sorted(arrayB)
    gcd_A, gcd_B = get_gcd(arrayA), get_gcd(arrayB) 
    
    for i in range(len(arrayB)):     
        if arrayB[i] % gcd_A == 0:
            stat1 = False
    if stat1:        
        answer = max(answer, gcd_A)

    for i in range(len(arrayA)):
        if arrayA[i] % gcd_B == 0:
            stat2 = False
    if stat2:
        answer = max(answer, gcd_B)

    return answer