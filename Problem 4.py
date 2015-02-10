

def find_max_palindrome(min=100,max=999):
    max_palindrome = 0
    i = 999
    while i > 99:
        b = 999
        while b >= i:
            prod = i*b
            if prod > max_palindrome and str(prod)==(str(prod)[::-1]):
                max_palindrome = prod
            b -= 1
        i -= 1
    return max_palindrome

L = find_max_palindrome()
print (L)