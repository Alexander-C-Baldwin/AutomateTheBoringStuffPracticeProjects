# collatzSeq will execute a function named collatz() that has one parameter named number
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1

def collatz(num):
    global number

    if num % 2 == 0:
        number = num // 2
        print(number)

    elif num % 2 == 1:
        number = 3 * num + 1
        print(number)


print('Please input a number:')

try:

    number = int(input())

    if number == 1:
        print(number)

    else:
        while number != 1:
            collatz(number)

except ValueError:
    print('You must enter an integer.')
