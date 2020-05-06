y= input('enter a number between 0.0 and 1.0')
x=float(y)
if x >1.0:
    print('this Greater than 1')
else:
    if x <0.0:
        print ('This is not a correct number')
    else:
        if x<0.6:
             print('F')
        else:
            if x>=0.9:
                print('A')
            else:
                if x>= 0.8:
                    print('B')
                else:
                    if x>=0.7:
                        print('C')
                    else:
                        if x>=0.6:
                            print('D')
                        else:
                            print('weird error')