# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
num = int(input('Enter number : '))
binary = ''

while num:
    binary += str(num % 2)
    num //= 2

i = len(binary)

while i:
    print(binary[i-1], end='')
    i -= 1

# 2. Write a python script to check whether a given number is Prime or not
n = int(input('Enter a number : '))

i = 2
for i in range(2, n):
    if n % i == 0:
        print('Not prime')
        break
    i += 1
else:
    print('Prime Number')

# 3. Write a python script to print all Prime numbers under 100


for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)

# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
x, y = int(input('Enter a number 1 : ')), int(input('Enter a number 2 : '))

for n in range(x, y+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)

# 5. Write a python script to find next prime number of a given number
x = int(input('Enter a number : '))

while True:
    x += 1
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x)
        break

# 6. Write a python script to print first N prime numbers
x = int(input('Enter a number : '))

for n in range(2, x):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)

# 7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
x, y = int(input('Num 1 :')), int(input('Num 2 :'))

for i in range(2, max(x, y)):
    if x % i == 0 and y % i == 0:
        print('Not a Co-prime')
        break
else:
    print('Co-prime')

# 8. Write a python script to print first N terms of a Fibonacci series
n = int(input('Enter a number :'))

first = 0
second = 1
next = 0

for i in range(n):
    print(first, end=' ')
    next = first + second
    first = second
    second = next

# 9. Write a python script to calculate LCM of two numbers
x, y = int(input('Num 1 :')), int(input('Num 2 :'))

maxNum = max(x, y)

while True:
    if maxNum%x ==0 and maxNum%y==0:
        print(maxNum)
        break
    maxNum+=1
# 10. Write a python script to calculate HCF of two numbers
x, y = int(input('Num 1 :')), int(input('Num 2 :'))

i = 2
max = min(x, y)
while i <= max:
    if x % i == 0 and y % i == 0:
        print(i)
        break
    i += 1
else:
    print(1)