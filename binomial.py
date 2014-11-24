from math import factorial
# def mult(a,b):
#     return a * b

def binomial(n,k):
    def numerator(n,k):
        return reduce(lambda x,y: x * y, range(n-k + 1, n+1))
    
    return numerator(n,k)/factorial(k)