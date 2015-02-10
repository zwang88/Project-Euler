total = 0
n0 = 0
n1 = 1
while ( total < 4000000 ):
    n2 = n1;
    n1 = n0 + n1;
    n0 = n2;
    if n1 % 2 == 0:
        total = total + n1
print (total)
