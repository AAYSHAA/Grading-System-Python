print("Grade Management System\n")
# Intializing Variables
total_outcomes = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0

# Creating an empty list.
outcome_list = []

# open for writing - (if it already exists its content will be deleted).
file = open('file.txt', 'w')
condition = True

#defining functions to get user input for credits.
def user_data(prompt):
    while True:
        try:
            credits_ = int(input(prompt))
        except ValueError:
            print('Integer required.\n')
            continue                  #After execution anything after the continue statement goes to next iteration.
        else:
            if credits_ not in range(0, 121, 20):
                print('Out of range. \n')
                continue

            return credits_


# Print histogram of outcomes
def histogram():
    print('\n')
    print('-' * 60)
    print('Histogram\n')
    print('Progress', progress, ' :', '*' * progress)
    print('Trailer', trailer, '  :', '*' * trailer)
    print('Retriever', retriever, ':', '*' * retriever)
    print('Excluded', exclude, ' :', '*' * exclude)
    total_outcomes = progress + trailer + retriever + exclude
    print('\n')
    print(total_outcomes, 'outcomes in total.')
    print('-' * 60)


# list for part 02 - Printing the outcome list
def get_list():
    print('PART 02\n')
    for i in outcome_list:     #count control loops till condtition is satisfied.
        print(i)


# text file for part 03 - Write outcomes to a text file
def text_file():
    print('-' * 60)
    print('PART 03\n')
    try:
        file = open('file.txt') #opens file in read mode.
        for line in file:
            print(line.rstrip('\n')) #print line at a time

    except FileNotFoundError:
        print('File not found please check the file')
    print('-' * 60)


while condition:  #Asking for user inputs and calling user_data functions to check user inputs
    pass_credits = user_data('Please enter credits at pass: ')
    defer_credits = user_data('Please enter credits at defer: ')          #Condition controlled iterates till condition is satisfied
    fail_credits = user_data('Please enter your credits at fail: ')       

    if pass_credits + defer_credits + fail_credits != 120:
        print('Total incorrect.\n')
        

    else:
        if pass_credits == 100:
            print('Progress (module trailer)\n')
            outcome = 'progress (module trailer)'
            trailer += 1
            total_outcomes += 1

        elif pass_credits == 120:
            print('progress\n')
            outcome = 'progress'
            progress += 1
            total_outcomes += 1

        elif fail_credits == 80 or fail_credits == 100 or fail_credits == 120:
            print('Exclude\n')
            outcome = 'Exclude'
            exclude += 1
            total_outcomes += 1

        elif pass_credits < 100 and fail_credits <= 100:
            print('Module retriever\n')
            outcome = 'retriever'
            retriever += 1
            total_outcomes += 1

        else:
            print('Total incorrect.\n')

        # PART 02
        outcome_list.append(f'{outcome} - {pass_credits}, {defer_credits}, {fail_credits}') #used to traverse a string by accessing each string character one at a time.(Transversing a string)
        
        # PART 03
        file = open('file.txt', 'a')
        file.write(f'{outcome}-{pass_credits},{defer_credits},{fail_credits}\n')  #Appending data to the formatted string on to the file.
        file.close()

    while True:
        print('Would you like another one?')
        choice = input('Enter "y" to add another one or "q" to end and view the summary: ')
        choice = choice.lower()
        if choice == 'y':
            print('\n')
            break       #Breakout of the loop,execute from the above loop

        elif choice == 'q':
            histogram()            # calling functions
            get_list()
            text_file()
            condition = False
            break

        else:
            print('Try again!')



























