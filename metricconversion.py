##########
### The below Python code is copyrighted by Lusi Yang. ###
### Contact: lusiyang@gmail.com or lusi.yang@mail.utoronto.ca ###
### Actual Program: http://bit.ly/2EcGCJd ###
### Copyright © 2017 ###
##########

def temp_metric_converter():
    # Program instructions
    print('----------')
    print('This calculator converts the following:')
    print('\n')
    print('(1) Temperature: Celsius (C) and Fahrenheit (F) (2) Length: kilometers (K) and miles (M) (3) Volume: gallons (G) and liters (L)')
    print('The converter is case sensitive, so please make sure you capitalize you letter grade.')
    print('\n')
    print('You have 3 choices of conversion.')
    print('\n')
    print('Enter T to convert temperature. Then enter C or F to convert.')
    print('Enter L to convert length or distance. Then enter K or M to convert.')
    print('Enter V to convert volume. Then enter G or L or convert.')
    print('\n')
              
   # Enter the conversion choices 
    while True:
        try:
            convert_format = input('What do you want to convert?: ')
            if convert_format != 'T'and convert_format != 'L' and convert_format != 'V':
                print('Please enter T, L or V.')
                continue
        except ValueError:
            print('Please enter T, L or V.')
            continue
        else:
            break
        
    # Temperature conversion
    if convert_format == 'T':
        while True:
            try:
                temp_format = input('Enter F or C to convert: ')
                if temp_format != 'F' and temp_format != 'C':
                    print('Please enter F or C.')
                    continue
            except ValueError:
                print('Please enter F or C.')
                continue
            else:
                break
        while True:
            try:
                temp = float(input('Enter temperature to convert: '))
            except ValueError:
                print ("Please enter a number.")
                continue
            else:
                break
        if temp_format == 'F':
          converted_temp = format((temp - 32)/(9/5), '.2f')
          print(temp, 'degrees Fahrenheit is equal to', converted_temp, 'degrees Celsius.')
        elif temp_format == 'C':
          converted_temp = format(temp * 1.8 +32, '.2f')
          print(temp, 'degrees Celsius is equal to', converted_temp, 'degrees Fahrenheit.')
        else:
            print('INVALID INPUT.')
        return

    # Length conversion         
    elif convert_format == 'L':
        while True:
            try:
                leng_format = input('Enter K or M to convert: ')
                if leng_format != 'K' and leng_format != 'M':
                    print('Please enter K or M.')
                    continue
            except ValueError:
                print('Please enter K or M.')
                continue
            else:
                break
        while True:
            try:
                leng = float(input('Enter length to convert: '))
            except ValueError:
                print ("Please enter a number.")
                continue
            else:
                break

        if leng_format == 'K':
          converted_leng = format(leng *(1/1.609344), '.2f')
          print(leng, 'kilometers is equal to', converted_leng, 'miles.')
        elif leng_format == 'M':
          converted_leng = format(leng * 1.609344, '.2f')
          print(leng, 'miles is equal to', converted_leng, 'kilometers')
        else:
            print('INVALID INPUT.')
        return

    # Volume conversion
    elif convert_format == 'V':
        while True:
            try:
                vol_format = input('Enter G or L to convert: ')
                if vol_format != 'G' and vol_format != 'L':
                    print('Please enter G or L.')
                    continue
            except ValueError:
                print('Please enter G or L.')
                continue
            else:
                break
        while True:
            try:
                vol = float(input('Enter volume to convert: '))
            except ValueError:
                print ("Please enter a number.")
                continue
            else:
                break
        if vol_format == 'G':
          converted_vol = format(vol * 3.785411784, '.2f')
          print(vol, 'gallons is equal to', converted_vol, 'liters.')
        elif vol_format == 'L':
          converted_vol = format(vol / 3.785411784, '.2f')
          print(vol, 'liters is equal to', converted_vol, 'gallons.')
        else:
            print('INVALID INPUT.')
        return
    else:
        print('INVALID INPUT.')

temp_metric_converter()

# To continue the program?
print('\n')
while True:
    response = input('Would you like to do another conversion? (y/n): ')
    while response !='y' and response != 'n':
        response = input("Please enter 'y' or 'n': ")
    if response == 'y':
        temp_metric_converter()
    elif response == 'n':
        print('Thanks for using the converter!')
        exit()
