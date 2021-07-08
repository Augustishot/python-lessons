counterchoice = int(input('How many stories do you want the star tower have?'))
a = 1
a2 = counterchoice
counterchoice = counterchoice + 1
counterchoice2 = counterchoice

for counter in range(1, counterchoice):
    if counterchoice > 2:
        print('*' * a)
        counterchoice = counterchoice - 1
        a = a + 1

for counter2 in range(1, counterchoice2):
    if counterchoice2 > 1:
        print('*' * a2)
        counterchoice2 = counterchoice2 - 1
        a2 = a2 - 1
        