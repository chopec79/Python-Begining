def chop(list):
    del list[0]
    del list[-1]

def middle(list):
    return list[1:-1]
    

newlist = ['a', 'b', 'c', 'd']
x = chop(newlist)
print(x)
print(newlist)

newlist2 = ['a', 'b', 'c', 'd']
y = middle(newlist2)
print(y)