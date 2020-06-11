file = open("romeo.txt", "r")
words = ['HopeCox', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
romeo1 =(file.read())
romeo= romeo1.split()

for x in words:
    if x in romeo:
        continue
    romeo.append(x)
print(sorted(romeo))
