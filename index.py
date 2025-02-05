

# 1. If-Else Statements

# A. Even/Odd
num = int(input('Enter number: '))
if num % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

# B. Voting
age = int(input('Enter your age: '))
if age <= 18:
    print('You are not eligible to vote.')
else:
    print('You are eligible to vote')

# C. Positive/Negative/Zero
integer = int(input('Enter a number: '))
if integer == 0:
    print('Number is zero.')
elif integer < 0:
    print('Number is negative.')
elif integer > 0:
    print('Number is positive.')
else:
    print('Input is not a number. I\'m very dissapointed in you.')

# 2. For/While Loops

# A. Numbers 1-10
for i in range(1,11,1):
    print(i)

# B. Numbers 1-5
i = 1
while i < 6:
    print(i)
    i += 1

# C. Factorial Loop
x = int(input('Input a number: '))
for i in range(1,x):
    x *= i
print(x)

# 3. Functions and Scope

# A. Greeting
name = input('Enter your name: ')
def greeting(name1):
    print('Hello my esteemed guest, ' + name1)
    print('If your name wasn\'t Karim, why are you here...')
greeting(name)

# B. Even/Odd
funcNum = input('Input a number: ')
def evenOdd(number):
    if number % 2 == 0:
        print('Number is even.')
    else:
        print('Number is odd.')
evenOdd(int(funcNum))

# C. Vowel/Strings
userString = input('Enter a string: ')
def vowelChecker(string):
    string = list(string)
    vowelNum = 0
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOU':
            vowelNum += 1
    print(vowelNum)
vowelChecker(userString)

# 4. Arrays & Objects

# A. Fruitloop
fruits = ['Orange', 'Apple', 'Banana', 'Durian', 'Mango']
for i in range(len(fruits)):
    print(fruits[i])

# B. Dictionary
grades = {'Angel':95 , 'Bianca':97 , 'Troy':93 , 'Marcus':87 }
for key in grades:
    print(str(key) + ': ' + str(grades[key]))

# C. Num Array
arrayNum = [[10,11,15],[14,24,65],[72,12,26]]
d = 0
for a in range(len(arrayNum)):
    b = arrayNum[a]
    for c in range(len(b)):
        if b[c] > d:
            d = b[c]
print(d)
