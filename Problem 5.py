def gcd(a,b):
    if b>a: return gcd(b,a)
    if b == 0: return a
    return gcd(b, a-b*(a//b))

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

def maxLcm(num):
    prod = 1
    for i in range(1,num+1):
        prod = lcm(i,prod)
    return prod

print(maxLcm(20))