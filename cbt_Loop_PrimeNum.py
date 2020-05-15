rawnum = input()
num = int(rawnum)
prime = True
for testrange in range(2,num):
    
    if num % testrange == 0 and num != testrange:
        print(num, 'equals', testrange, '*', num/testrange)
        prime = False
        break
    
if prime:
    print(num, 'is a prime number!')
else:
    print(num, 'is not a prime number')
