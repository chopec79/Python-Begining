hours=input('How many hours')
rate=input('what is your rate?')
# hours=('10')
# rate=('1')
Chours =int(hours)
try:
    Crate=float(rate)
except:
    float('1')
overtime =float(1.5*Crate)
if Chours >40 :
    y =Chours-40
else :
    y=1
overtimepay =(overtime*y)

pay= (Chours*Crate)
opay=((40*Crate)+overtimepay)
if Chours <=40:
    print('your pay will be' , pay)
elif Chours >40:
    print('your pay will be' , opay)
print(y)
print(overtime)
print(overtimepay)
print(pay)
print(totalpay)
