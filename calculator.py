"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Run program until 'break' is called
while True:

    # Get input
    user_input = input("Enter your equation: ")

    # Check if input contains 'q' or 'quit'
    if 'q' in user_input.lower() or 'quit' in user_input.lower():
        print('Thank you for using the calculator. Goodbye.')
        break

    # Tokenize input
    token = user_input.split(' ')

    # create variables for operator and operands
    operator = token[0]
    num1 = token[1]
    if len(token) > 2:
        num2 = token[2]
    
    # Execute appropriate function