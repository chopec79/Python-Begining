user_input = 'Random'
#list
data = []

#function
def show_menu():
    print('Menu')
    print('1 Add an item')
    print('2 Marks as done')
    print('3 view items')
    print('4 Exit')

#While Loop
while user_input != '4':

    #using function
    show_menu()
    user_input = input('Enter your choice. ')
    
    if user_input == '1':
        item = input('What is to be done? ')
        data.append(item)
        print('added item', item)
    elif user_input == '2':
        item = input('What is to be marked as done? ')
        #new if statement
        if item in data:
            data.remove(item)
            print('removed item:', item)
        else:
            print('Item does nto exsit')
    elif user_input == '3':
        print('List of to do items:')
        
        #for loop
        for item in data:
            print(item)
    elif user_input == '4':
        print('Goddbye')        
        
        
        
        