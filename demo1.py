fruits={'apple','orange','pear','grape'}
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case 'appple',10:
            print('10 apples')
        case 'orange',3:
            print('3 oranges')
        case 'pear',4:
            print('4 pears')
        case 'grape',5:
            print('5 grapes')