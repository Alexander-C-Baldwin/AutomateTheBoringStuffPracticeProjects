# This program takes a list value as an argument and returns a string with all th items separated by comma
# and a space, with 'and' inserted before the last item

def commaCode(listValue):
    cheese = ''

    if (len(listValue)) == 0:
        return('Your list is not valid.')

    elif (len(listValue)) == 1:
        return listValue[0]

    elif (len(listValue)) == 2:
        return (listValue[0] + ' and ' + listValue[-1])

    elif (len(listValue)) > 2:
        for i in range(len(listValue)- 1):
            cheese += (listValue[i] + ', ')
        cheese += ('and ' + listValue[-1])

        return cheese


spam = ['dog', 'cat', 'whale', 'zebra']

cheese = commaCode(spam)

print(cheese)

        
