print('This is my calculator')

x = input('Give a number: ')
operator = input('Would you like to +, -, *, /: ')
y = input('Give another number: ')

# Check if the inputs can be converted to integers
try:
    x = int(x)
    y = int(y)
except ValueError:
    print('Invalid input. Please enter valid numbers.')
    exit()

if operator == '+':
    answer = x + y
elif operator == '-':
    answer = x - y
elif operator == '*':
    answer = x * y
elif operator == '/':
    # Check for division by zero
    if y == 0:
        print('Error: Division by zero.')
        exit()
    answer = x / y
else:
    print('Invalid operator. Please enter +, -, *, or /.')
    exit()

print('Answer:', answer)
