x = open('test1.txt')
for line in x:
    line=line.rstrip()
    if line.startswith('Man'):
        print(line)
        