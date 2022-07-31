def solution(n):
    import numpy as np
    if n == int(np.sqrt(n)) ** 2:
        return (int(np.sqrt(n)) + 1) ** 2
    else: return -1