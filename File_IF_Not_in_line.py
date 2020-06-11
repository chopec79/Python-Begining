z=input('what is it')
x = open(z)
for line in x:
    line=line.rstrip()
    if not 'file.' in line:
        continue
    print(line)
        
        