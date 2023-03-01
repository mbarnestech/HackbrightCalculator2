"""CLI application for a prefix-notation calculator."""

from arithmetic import add, subtract, multiply, divide, square, cube, \
    power, mod

# Run program until 'break' is called
while True:

    # Get input
    user_input = input("Enter your equation: ")

    # Check if input contains 'q' or 'quit'
    if user_input.lower()[0] == 'q':
        print('Thank you for using the calculator. Goodbye.')
        break

    # Tokenize input
    tokens = user_input.split(' ')

    # create variables for operator and operands
    operator = tokens[0]
    num1 = int(tokens[1])
    if len(tokens) > 2:
        num2 = int(tokens[2])
    
    # Execute appropriate function

    # For '+', add num1 and num2
    if operator == '+':
        answer = add(num1, num2)

    # For '-', subtract num2 from num1
    elif operator == '-':
        answer = subtract(num1, num2)

    # For '*', multiply num1 and num2
    elif operator == '*':
        answer = multiply(num1, num2)

    # For '/', divide num1 by num2
    elif operator == '/':
        answer = divide(num1, num2)
        
    # For 'square', square num1
    elif operator == 'square':
        answer = square(num1)
        
    # For 'cube', cube num1
    elif operator == 'cube':
        answer = cube(num1)

    # For 'power', raise num1 to the num2 power
    elif operator == 'power':
        answer = power(num1, num2)

    # For 'mod', provide the remainder of num1 divided by num2
    elif operator == 'mod':
        answer = mod(num1, num2)

    # For anything else, provide error statement
    else:
        answer = 'You didn\'t provide the right values'
    
    # Print result
    print(answer)