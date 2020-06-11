fname = input('Name of the file')
try: 
    file1 = open(fname)
except:
    print('Cannot openfile:',  fname)
    quit()
#file1 = open(fname)
count= 0
for line in file1:
    if line.startswith('Maybe'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
