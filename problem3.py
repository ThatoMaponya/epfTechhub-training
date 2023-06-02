i = 600851475143
n = 2

while(i != 1):
    num = i%n
    if (num==0):
        i = i/n
        print(n)
    else:
        n = n + 1

