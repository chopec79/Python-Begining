input = input('Enter file name')
handle = open(input)

counts = dict()
for line in handle:
    words = line.spit()
    for word in words:
        counts[word]= counts.get(word,0) + 1
        
print(counts)