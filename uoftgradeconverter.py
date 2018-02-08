##########
### The below Python code is copyrighted by Lusi Yang. ###
### Contact: lusiyang@gmail.com or lusi.yang@mail.utoronto.ca ###
### Actual Program: http://bit.ly/2ER1p6g ###
### Copyright © 2017 ###
##########

def grade_cal():
    # Program instructions
    print('-------------')
    print('This is a grade converter. It follows the grade system of the University of Toronto. It accepts 4.0 scale, letter, and percentage grades. The program is case sensitive, so please make sure you capitalize you letter grade.')
    print('\n')
    print('You have 3 choices for the grade format:')
    print('\n')
    print('Enter 4 to convert from 4.0 sacle to letter and percentage.')
    print('Enter L to convert from letter to 4.0 scale and prcentage.')
    print('Enter P to convert from percentage to 4.0 scale and letter.')
    print('\n')
    # Get the grade to convert
    while True:
        try:
            grade_format = input('Enter a grade format: ')
            if grade_format != '4' and grade_format != 'L' and grade_format != 'P':
                print('Please enter 4, L or P.')
                continue
        except ValueError:
            print('Please enter 4, L or P.')
            continue
        else:
            break
    if grade_format == '4':
        while True:
            try:
                grade = float(input('Enter a grade to convert: '))
                if grade > 4 or grade < 0:
                    print('Please enter a number between 0 and 4.')
                    continue
            except ValueError:
                print('Please enter a 4.0 scale grade.')
                continue
            else:
                break
    elif grade_format == 'L':
        while True:
            try:
                grade = input('Enter a grade to convert: ')
                if grade != 'A+' and grade != 'A' and grade != 'A-' and grade != 'B+' and grade != 'B' and grade != 'B-' and grade != 'C+' and grade != 'C' and grade != 'C-' and grade != 'D+' and grade != 'D' and grade != 'D-' and grade != 'F':
                    print('Please enter a letter grade.')
                    continue
            except ValueError:
                print('Please enter a letter grade.')
                continue
            else:
                break
    elif grade_format == 'P':
        while True:
            try:
                grade = float(input('Enter a grade to convert: '))
                if grade > 100 or grade < 0:
                    print('Please enter a number between 0 and 100.')
                    continue
            except ValueError:
                print('Please enter a percentage grade.')
                continue
            else:
                break       
    else:
        print('Please enter 4, L or P.')

    # The grade system
    if grade_format == '4':
    # Convert from 4.0 to letter and percentage
        if grade >= 3.85:
            print('The letter grade is A/A+.')
            print('The percentage grade is between 85-100.')
        elif grade >= 3.5:
            print('The letter grade is A-.')
            print('The percentage grade is between 85-89.')
        elif grade >= 3.15:
            print('The letter grade is B+.')
            print('The percentage grade is between 77-79.')
        elif grade >= 2.85:
            print('The letter grade is B.')
            print('The percentage grade is between 73-76.')
        elif grade >= 2.5:
            print('The letter grade is B-.')
            print('The percentage grade is between 70-72.')
        elif grade >= 2.15:
            print('The letter grade is C+.')
            print('The percentage grade is between 67-69.')
        elif grade >= 1.85:
            print('The letter grade is C.')
            print('The percentage grade is between 63-66.')
        elif grade >= 1.5:
            print('The letter grade is C-.')
            print('The percentage grade is between 60-62.')
        elif grade >= 1.151:
            print('The letter grade is D+.')
            print('The percentage grade is between 57-59.')
        elif grade >= 0.85:
            print('The letter grade is D.')
            print('The percentage grade is between 53-56.')
        elif grade >= 0.35:
            print('The letter grade is D-.')
            print('The percentage grade is between 50-52.')
        elif grade < 0.35:
            print('The letter grade is F.')
            print('The percentage grade is between 0-49.')
        else:
            print('Please enter a 4.0 scale grade.')
    elif grade_format =='L':
    # Convert from letter to 4.0 and percentage
        if grade == 'A+':
            print('The 4.0 scale grade is 4.')
            print('The percentage grade is between 90-100.')
        elif grade == 'A':
            print('The 4.0 scale grade is 4.')
            print('The percentage grade is between 85-98.')
        elif grade == 'A-':
            print('The 4.0 scale grade is 3.7.')
            print('The percentage grade is between 80-84.')
        elif grade == 'B+':
            print('The 4.0 scale grade is 3.3.')
            print('The percentage grade is between 77-79.')
        elif grade == 'B':
            print('The 4.0 scale grade is 3.')
            print('The percentage grade is between 73-76.')
        elif grade == 'B-':
            print('The 4.0 scale grade is 2.7.')
            print('The percentage grade is between 70-72.')
        elif grade =='C+':
            print('The 4.0 scale grade is 2.3.')
            print('The percentage grade is between 67-69.')
        elif grade =='C':
            print('The 4.0 scale grade is 2.')
            print('The percentage grade is between 63-66.')
        elif grade == 'C-':
            print('The 4.0 scale grade is 1.7.')
            print('The percentage grade is between 60-62.')
        elif grade =='D+':
            print('The 4.0 scale grade is 1.3.')
            print('The percentage grade is between 57-59.')
        elif grade == 'D':
            print('The 4.0 scale grade is 1.')
            print('The percentage grade is between 53-56.')
        elif grade =='D-':
            print('The 4.0 scale grade is 0.7.')
            print('The percentage grade is between 50-52.')
        elif grade == 'F':
            print('The 4.0 scale grade is 0.')
            print('The percentage grade is between 0-49.')
        else:
            print('Please enter a letter grade!')
    elif grade_format =='P':
    # Convert from percentage to 4.0 and letter
        if grade >= 90:
            print('The letter grade is A+.')
            print('The 4.0 scale grade is 4.')
        elif grade >= 85:
            print('The letter grade is A.')
            print('The 4.0 scale grade is 4.')
        elif grade >= 80:
            print('The letter grade is A-.')
            print('The 4.0 scale grade is 3.7.')
        elif grade >= 77:
            print('The letter grade is B+.')
            print('The 4.0 scale grade is 3.3.')
        elif grade >= 73:
            print('The letter grade is B.')
            print('The 4.0 scale grade is 3.')
        elif grade >= 70:
            print('The letter grade is B-.')
            print('The 4.0 scale grade is 2.7.')
        elif grade >= 67:
            print('The letter grade is C+.')
            print('The 4.0 scale grade is 2.3.')
        elif grade >= 63:
            print('The letter grade is C.')
            print('The 4.0 scale grade is 2.')
        elif grade >= 60:
            print('The letter grade is C-.')
            print('The 4.0 scale grade is 1.7.')
        elif grade >= 57:
            print('The letter grade is D+.')
            print('The 4.0 scale grade is 1.3.')
        elif grade >= 53:
            print('The letter grade is D.')
            print('The 4.0 scale grade is 1.')
        elif grade >= 50:
            print('The letter grade is D-.')
            print('The 4.0 scale grade is 0.7.')
        elif grade <= 49:
            print('The letter grade is F.')
            print('The 4.0 scale grade is 0.')
        else:
            print('Please enter a percentage grade.')
    else:
        print('No mark!')
grade_cal()

# To continue the program?
print('\n')
while True:
    response = input('Would you like to check out another grade? (y/n): ')
    while response !='y' and response != 'n':
        response = input("Please enter 'y' or 'n': ")
    if response == 'y':
        grade_cal()
    elif response == 'n':
        print('Thanks for using the U of T grade converter!')
        exit()
