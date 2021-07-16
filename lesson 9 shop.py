fd = {}
fd['A001'] = 'gummy bear : $20'
fd['A002'] = 'popsticles : $25'
fd['A003'] = 'chiken noodles : $10'
fd['A004'] = 'coke : $30'
f = input("Are you finding something? Please insert 'y' or 'n'. answer : ")
while f == 'y':
    print('What are you finding? Please insert the item number')
    f2 = input('(A___) number : ')
    if f2 in fd.keys():
        print(fd[f2])
    else:
      af = input("This is an unknown item number, please check again. If you really need this food, I can add it on the list so you can buy it. (y / n)")
      if af == 'y':
        c = input('What is the food you want called? food : ')
        c2 = int(input('How much does the food cost in the market? (__) cost : '))
        c2 = c2 + (c2 % 10)
        n = 5
        fd['A00' + str(n)] = c +' : $'+ str(c2)
        n = n + 1
        print('Thank you!')
      else:
        print("Sorry, we can't help you now.")
    f = input("Are you finding something? Please insert 'y' or 'n'. answer : ")

if f == 'n':
  print('Bye, your welcome to use this system anytime!')