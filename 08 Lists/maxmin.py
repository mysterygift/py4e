# Write a program that stores user-entered numbers in a list and use max() and min() to compute and output these values.
numbuffer = list()
print('DEBUG: numbuffer list initialised.')
inp = 'empty'

try :
    while(inp != 'done') :
        try :
                inp = input('Enter a number: ')
                float_inp = float(inp)
                numbuffer.append(float_inp)
        except :
            print('Invalid input. Please input a NUMBER.')

    print("User entered 'done'.")
    print('Calculating...')
    print('...')
    print('...')
    print(f'Maximum:', max(numbuffer))
    print(f'Minimum:', min(numbuffer))

except :
    print('EXCEPTION: You did not enter any numbers. Try again.')