# Write a program for instructions on
# How to assemble an Acme laundry dryer

# The main function performs programs main logic
def step0():
    # Display the start-up message.
    startup_message()
    input('Press Enter to see Step 1.')
    # Display step 1.
    step1()
    input('Press enter to see Step 2.')
    # Display Step 2.
    step2()
    input('Press enter to see Step 3.')
    # Display step 3.
    step3()
    input('Press enter to see Step 4.')
    step4()

# The startup_message function displays the
# program's initial message on the screen.
def startup_message():
    print('This program tells you how to,')
    print('disassemble an ACME laundry dryer.')
    print('There are 4 steps in the process.')
    print()

# The step1 function displays the instructions
# for Step 1.

def step1():
    print('Step 1: Unplug the dryer and')
    print('move it away from the wall.')
    print()

# The step2 function displays the instruction
# for Step 2.
def step2():
    print('Step 2: Unscrew the 6 screws')
    print('from the back of the dryer.')
    print()

# The step3 function displays the instruction
# for Step 3.
def step3():
    print('Step 3: Remove back panel')
    print('from the dryer.')
    print()

# The step4 function displays the instruction
# for Step 4.
def step4():
    print('Step 4: Pull the top of the dryer')
    print('straight up')

# Call the main function to begin the program
step0()