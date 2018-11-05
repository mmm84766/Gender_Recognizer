while True:
    name = input('Enter first name :')
    if name.find(' ') != -1:
        print('Entered name not valid, Enter first name only')       
    else:
        break

if name[-1] in ['a','e','i', 'A', 'E', 'I']:
    print('female')
else:
    print('male')
