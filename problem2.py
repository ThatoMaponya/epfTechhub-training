

i = 0
sum = 0
num1 = 0
num2 = 1

while i < 4000000:
    i = num1 + num2 
    num1 = num2
    num2 = i

if (i % 2 == 0):
   sum += i

   print(sum)