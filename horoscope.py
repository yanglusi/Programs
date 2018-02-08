### The Horoscope Program ###

### Author: Lusi Yang (from Canada) ###
### Actual Program: http://bit.ly/2GWAw1j ###
### Copyright © 2017 ###

# Welcome display 
print('About this Horoscope Program: \n')
print('This program will display zodiac signs and their associated personality.')
print('It will also show the astrological element of the sign and its compatible signs.\n')

# The program
def horoscope():
    # Enter the date 
    while True:
            try:
                birth_month = int(input('Enter your month of birth (between 1 and 12): '))
                if birth_month not in range(1, 13, 1):
                     print('Please enter a month between 1 and 12.')
                     continue
            except ValueError:
                print('Please enter a valid birth month (number).')
                continue
            else:
                break

    month_31 = [1,3,5,7,8,10,12]
    month_30 = [4, 5, 9, 11]
    month_29 = [2]

    while True:
            try:
                birth_day = int(input('Enter your day of birth (between 1 and 31): '))
                if birth_month in month_31 and birth_day > 31:
                     print('Please enter a valid day of the month.')
                     continue
                elif birth_month in month_30 and birth_day > 30:
                    print('Please enter a valid day of the month.')
                    continue
                elif birth_month in month_29 and birth_day > 29:
                    print('Please enter a valid day of the month.')
                    continue
            except ValueError:
                print('Please enter a valid day (number) of the month.')
                continue
            else:
                break

    # The signs        
    ### Aquarius ###
    aqurius_charc = 'creative, progressive, affectionate, friendly, attractive, popular, and unpredictable \n'
    aqurius_astro = 'Aquarius belongs to the air signs with Gemini and Libra. These folks have creative and imaginative minds. \n'
    aqurius_comp = 'Leo, Sagittarius'

    if birth_month == 1 and birth_day in range(20, 32):
        print('Aqurius\n', 'Characteristics:', aqurius_charc, 'Astrological Element:', aqurius_astro, 'Greatest Compatible Signs:', aqurius_comp)

    if birth_month == 2 and birth_day in range(1, 19):
        print('Aqurius\n', 'Characteristics:', aqurius_charc, 'Astrological Element:', aqurius_astro, 'Greatest Compatible Signs:', aqurius_comp)

    ### Pisces ###
    pisces_charc = 'caring, loving, wise, loyal, artistic, compassionate, mystical, fearful, and overly trusting \n'
    pisces_astro = 'Pisces belongs to the water signs with Cancer and Scorpio. These folks tend to be emotional and ultra-sensitive. \n'
    pisces_comp = 'Virgo, Taurus'

    if birth_month == 2 and birth_day in range(19, 30):
        print('Pisces\n', 'Characteristics:', pisces_charc, 'Astrological Element:', pisces_astro, 'Greatest Compatible Signs:', pisces_comp)

    if birth_month == 3 and birth_day in range(1, 21):
        print('Pisces\n', 'Characteristics:', pisces_charc, 'Astrological Element:', pisces_astro, 'Greatest Compatible Signs:', pisces_comp)

    ### Aries ###
    aries_charc = 'spontaneous, daring, courages, energetic, action oriented, adventurous, impatient, and ruthless \n'
    aries_astro = 'Aries belongs to the fire signs with Leo and Sagittarius. These folks are intelligent and physically strong.\n'
    aries_comp = 'Libra, Leo'

    if birth_month == 3 and birth_day in range(21, 32):
        print('Aries\n', 'Characteristics:', aries_charc, 'Astrological Element:', aries_astro, 'Greatest Compatible Signs:', aries_comp)

    if birth_month == 4 and birth_day in range(1, 20):
        print('Aries\n', 'Characteristics:', aries_charc, 'Astrological Element:', aries_astro, 'Greatest Compatible Signs:', aries_comp)

    ### Taurus ###
    taurus_charc = 'trustworthy, artistic, practival, loyal, dedicated, generous, stubborn, possessive, and stubborn \n'
    taurus_astro = 'Taurus belongs to the earth signs with Virgo and Capricorn. These folks are conservative, realistic, and stick to their people. \n'
    taurus_comp = 'Scorpio, Cancer'

    if birth_month == 4 and birth_day in range(20, 31):
        print('Taurus\n', 'Characteristics:', taurus_charc, 'Astrological Element:', taurus_astro, 'Greatest Compatible Signs:', taurus_comp)

    if birth_month == 5 and birth_day in range(1, 21):
        print('Taurus\n', 'Characteristics:', taurus_charc, 'Astrological Element:', taurus_astro, 'Greatest Compatible Signs:', taurus_comp)

    ### Gemini ###
    gemini_charc = 'cheerful, gentle, curious, enthusiastic, versatile, intelligent, social, nervous, and indecisive \n'
    gemini_astro = 'Gemini belongs to the air signs with Libra and Aquarius. These folks are rational and social who enjoy giving advice. \n'
    gemini_comp = 'Sagittarius, Aquarius'

    if birth_month == 5 and birth_day in range(21, 32):
        print('Gemini\n', 'Characteristics:', gemini_charc, 'Astrological Element:', gemini_astro, 'Greatest Compatible Signs:', gemini_comp)

    if birth_month == 6 and birth_day in range(1, 21):
        print('Gemini\n', 'Characteristics:', gemini_charc, 'Astrological Element:', gemini_astro, 'Greatest Compatible Signs:', gemini_comp)

    ### Cancer ###
    cancer_charc = 'loyal, sympathetic, persuasive, unpredicatable, sensitive, emotional, indecisive, temperamental, and insecure \n'
    cancer_astro = 'Cancer belongs to the water signs with Scorpio and Pisces. These folks tend to be emotional and ultra-sensitive.\n'
    cancer_comp = 'Capricorn, Taurus'

    if birth_month == 6 and birth_day in range(21, 31):
        print('Cancer\n', 'Characteristics:', cancer_charc, 'Astrological Element:', cancer_astro, 'Greatest Compatible Signs:', cancer_comp)

    if birth_month == 7 and birth_day in range(1, 23):
        print('Cancer\n', 'Characteristics:', cancer_charc, 'Astrological Element:', cancer_astro, 'Greatest Compatible Signs:', cancer_comp)

    ### Leo ###
    leo_charc = 'majestic, optimistic, loyal, aristocratic, passionate, creative, humorous, arrogant, stubborn, and self-centered \n'
    leo_astro = 'Leo belongs to the fire signs with Aries and Sagittarius. These folks are both passionate and temperamental. \n' 
    leo_comp = 'Aquarius, Gemini'

    if birth_month == 7 and birth_day in range(23, 32):
        print('Leo\n', 'Characteristics:', leo_charc, 'Astrological Element:', leo_astro, 'Greatest Compatible Signs:', leo_comp)

    if birth_month == 8 and birth_day in range(1, 23):
        print('Leo\n', 'Characteristics:', leo_charc, 'Astrological Element:', leo_astro, 'Greatest Compatible Signs:', leo_comp)

    ### Virgo ###
    virgo_charc = 'feminine, duty-bound, sincere, caring, critical, analytical, shy, hardworking, kind, loyal, and pratical \n'
    virgo_astro = 'Virgo belongs to the earth signs with Taurus and Capricorn. These folks are conservative, realistic, and stick to their people. \n'
    virgo_comp = 'Pisces, Cancer'

    if birth_month == 8 and birth_day in range(23, 32):
        print('Virgo\n', 'Characteristics:', virgo_charc, 'Astrological Element:', virgo_astro, 'Greatest Compatible Signs:', virgo_comp)

    if birth_month == 9 and birth_day in range(1, 23):
        print('Virgo\n', 'Characteristics:', virgo_charc, 'Astrological Element:', virgo_astro, 'Greatest Compatible Signs:', virgo_comp)

    ### Libra ###
    libra_charc = 'balanced, calm, attractive, indecisive, diplomatic, gravious, social, avoids confrontations, and cooperative \n'
    libra_astro = 'Libra belongs to the air signs with Gemini and Aquarius. These folks are rational and social who enjoy giving advice. \n'
    libra_comp = 'Aries, Sagittarius'

    if birth_month == 9 and birth_day in range(23, 31):
        print('Libra\n', 'Characteristics:', libra_charc, 'Astrological Element:', libra_astro, 'Greatest Compatible Signs:', libra_comp)

    if birth_month == 10 and birth_day in range(1, 23):
        print('Libra\n', 'Characteristics:', libra_charc, 'Astrological Element:', libra_astro, 'Greatest Compatible Signs:', libra_comp)

    ### Scorpio ###
    scorpio_charc = 'mysterious, passionate, loyal, brave, robust, resourceful, jealous, stubborn, and distrusting \n'
    scorpio_astro = 'Scorpio belongs to the water signs with Cancer and Pisces. These folks tend to be emotional and ultra-sensitive. \n'
    scorpio_comp = 'Taurus, Cancer'

    if birth_month == 10 and birth_day in range(23, 32):
        print('Scorpio\n', 'Characteristics:', scorpio_charc, 'Astrological Element:', scorpio_astro, 'Greatest Compatible Signs:', scorpio_comp)

    if birth_month == 11 and birth_day in range(1, 22):
        print('Scorpio\n', 'Characteristics:', scorpio_charc, 'Astrological Element:', scorpio_astro, 'Greatest Compatible Signs:', scorpio_comp)

    ### Sagittarius ###
    sagittarius_charc = 'courageous, frank, creative, fearless, generous, self-dependent, over-confident, crude, boastful, and unperdictable \n'
    sagittarius_astro = 'Sagittarius belongs to the first signs with Aries and Leo. These folks are both passionate and temperamental. \n'
    sagittarius_comp = 'Gemini, Aries'

    if birth_month == 11 and birth_day in range(21, 31):
        print('Sagittarius\n', 'Characteristics:', sagittarius_charc, 'Astrological Element:', sagittarius_astro, 'Greatest Compatible Signs:', sagittarius_comp)

    if birth_month == 12 and birth_day in range(1, 22):
        print('Sagittarius\n', 'Characteristics:', sagittarius_charc, 'Astrological Element:', sagittarius_astro, 'Greatest Compatible Signs:', sagittarius_comp)

    ### Capricorn ###
    capricorn_charc = 'responsible, cautious, thoughtful, confident, hard working, disciplined, self-control, unforgiving, jealous, and gloomy \n'
    capricorn_astro = 'Capricorn belongs to the earth signs with Taurus and Virgo. These folks are conservative, realistic, and stick to their people. \n'
    capricorn_comp = 'Taurus, Cancer'

    if birth_month == 12 and birth_day in range(22, 32):
        print('Capricorn\n', 'Characteristics:', capricorn_charc, 'Astrological Element:', capricorn_astro, 'Greatest Compatible Signs:', capricorn_comp)

    if birth_month == 1 and birth_day in range(1, 20):
        print('Capricorn\n', 'Characteristics:', capricorn_charc, 'Astrological Element:', capricorn_astro, 'Greatest Compatible Signs:', capricorn_comp)

horoscope()

# To continue the program?

while True:
    response = input('Would you like to check out another sign? (y/n): ')
    while response !='y' and response != 'n':
        response = input("Please enter 'y' or 'n': ")
    if response == 'y':
        horoscope()
    elif response == 'n':
        print('Thanks for using my Horoscope program!')
        exit()
