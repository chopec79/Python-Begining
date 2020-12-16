fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        newline = line.split()
print(newline[1])

fhand = open(' mbox-short.txt') 
for line in fhand:
    line = line.rstrip() 
    if not line.startswith(' From '):
        continue 
    words = line.split() 
    print( words[ 2])


