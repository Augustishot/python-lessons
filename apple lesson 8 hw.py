a = 0
print("Hello! Press P to purchase apples. Press W to sell apples.", \
      "Press A to emphasize today's deal.", \
          "Press S to end this system.")
s = input()
def get_apple():
    global a
    m = float(input('How much money would an apple cost for you?'))
    ml = float(input('How much money would you prepare for buying the apples?'))
    ml2 = ml
    ma = (int(ml) - int(m))

    if ma >= 0:
        print('Would you like to purchase some apples? You already have', \
                  str(a), 'apples. (y / n)')
    else:
        print("Sorry, you don't have enough money.", \
              "Would you like to prepare more money for buying the apples? (y / n)")
        nem = input()
        if nem == 'y':
            ml3 = ml
            ml = input('How much money would you prepare for buying the apples?')
            ml = ml + ml3
            ml2 = ml2 + ml3
            print('Would you like to purchase some apples? You already have', \
                  str(a), 'apples. (y / n)')
            
        else:
            print("Sorry, you can't buy more apples now, but you can get money from selling them", \
                  "Press W to sell apples.", \
                      "Press S to end this system.")
    
    c = input()
    while c == 'y' and ml > m:
        c2 = int(input('How many apples would you want to purchase?'))
        a = a + c2
        m = int(m)
        ml = int(ml)
        ml = ml - (m * c2)
        print('Now you have', str(a), 'apples and', str(ml), 'dollars left.')
        if ml >= m:
            c = input('Would you like some more? (y / n)')
        else:
            print("Sorry, you can't buy more apples now, but you can get money from selling them.", \
                  "Press W to sell apples.", \
                      "Press S to end this system.")
    if c =='n':
        print("Now, press W to sell apples. Press A to emphasize today's deal.", \
              ' Press S to end this system.')
    
    return c
def sell_apple():
    global ml
    global a
    cl = []
    cm = []
    ac = int(input('How much money would an apple cost to your customers?'))
    if a >= 1:
        sa = input('Would you want to sell apples to your customers?( y / n)')
    else:
        print('Sorry, you have no more apples left.', \
              "Press P to purchase apples. Press A to emphasize today's deal.", \
                      "Press S to end this system.")
    while sa =='y' and a >= 1:
        ba = int(input('How many apples would this customer buy?'))
        if ba <= a:
            cl.append(ba)
            bm = ac * ba
            cm.append(bm)
            print('This customer needs to pay', str(bm), 'dollars.')
            sa = input('Would you want to sell apples to your customers?(y / n)')
        else:
            print('Sorry, this customer has bought too many apples.', \
                  "Press P to purchase apples. Press A to emphasize today's deal.", \
                      "Press S to end this system.")
            break
    if sa == 'n':
        print("Now, press P to purchase apples. Press A to emphasize today's deal.", \
                      "Press S to end this system.")

def emphasize_apple():
    global a
    global cl
    global m
    global ac
    global ml2
    global cm
    c = 0
    cl2 = sum(cl)
    cm2 = sum(cm)
    cl3 = cl
    print('There are', str(a), 'apples left.')
    print('Today, you sold', str(cl2), 'apples and got', str(cm2), 'dollars.')
    print('This is your list of the apples you sold.')
    while len.cl3 >=c:
        cl.pop[c], print('apples')
        c = c + 1
    if ml2 < cm2:
        print('You earned more money than you payed for the apples')
    elif ml2 == cm2:
        print("You didn't pay, but you didn't earn any money too.")
    else:
        print('You payed.')
    print("Now, you can press D to see how many apples are left. Press S to end this system.")
        
while s != 'S' or s != 's':
    if s == 'P' or s == 'p':
        get_apple()
        s = input()

    if s == 'W' or s == 'w':
        sell_apple()
        s = input()
    
    if s == 'A' or s == 'a':
        emphasize_apple()
        s = input