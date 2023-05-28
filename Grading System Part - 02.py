
#Part 04-  Dictionary
print("Grading System!/n")

# initializing variables
total_outcomes = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0

#creating an empty dictionary
dictionary = {}
condition = True


def user_data(prompt):
    while True:
        try:
            credits_ = int(input(prompt))
        except ValueError:
            print('Integer required.\n')
            continue
        else:
            if credits_ not in range(0, 121, 20):
                print('Out of range. \n')
                continue

            return credits_


def id_dictionary():
    print('-' * 60)
    print('PART 04\n') 
    for key, value in dictionary.items(): #displaying entered data
        print(key, value, end=' ')


while condition:
    student_id = input('Enter your student ID number: ')
    if student_id not in dictionary:  #validation to prevent user id repeating
        pass_credits = user_data('Please enter credits at pass: ')
        defer_credits = user_data('Please enter credits at defer: ')
        fail_credits = user_data('Please enter your credits at fail: ')
    else:
        print('ID number already exists!\n Please enter again!')
        continue

    if (pass_credits + defer_credits + fail_credits) != 120:
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
            print('Do not progress-module retriever\n')
            outcome = 'retriever'
            retriever += 1
            total_outcomes += 1

        else:
            print('Total incorrect')

        dictionary[student_id] = ':' + outcome + ' - ' + str(pass_credits) + ',' + str(defer_credits) + ',' + str(fail_credits) #updating user inputs into a dictionary

        while True:
            print('Would you like another one?')
            choice = input('Enter "y" to add another one or "q" to end and view the summary: ')
            choice = choice.lower()

            if choice == 'y':
                print('\n')
                break

            elif choice == 'q':
                id_dictionary()  # calling functions
                condition = False
                print()
                print('-' * 60)
                break

            else:
                print('Try again!')

    










