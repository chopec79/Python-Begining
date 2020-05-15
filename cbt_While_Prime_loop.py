#Broken-Doenst work
num = 87
test = 2
while test < num:
    if num % test == 0 and num != test:
        print(num, 'equals', test, '*' , num/test)
        print(num, 'is not a prime number')
        test=test +1
        break
else:
    print(num, 'is not a prime number')
        