ans = 0
i = 2
while i <600851475143:
    if 600851475143 % i == 0:
       oldans = ans;
       for j in range(2, i):
           if i % j == 0:
              ans = oldans;
              break
           else:
              ans = i;
    i = 1 + i;
print(ans)


