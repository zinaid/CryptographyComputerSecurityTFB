import math

def findModInverse(a, m): 
        # Returns modulo inverse of a % m where a*x % m = 1
        for x in range(1, m):
            if (((a%m) * (x%m)) % m == 1):
                return x
        return -1