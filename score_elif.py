y=input('Enter a numer between 0.0 and 1.0')
x=float(y)
if x>1.0:
    print('Greater than 1')
elif x>=0.9:
    print('A')
elif x>=0.8:
    print('B')
elif x>=0.7:
    print('C')
elif x>=0.6:
    print('D')
elif x>=0.0:
    print('F')
elif x<=0.0:
    print('less than 0.0')