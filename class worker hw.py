import random
op = input('Do you need my help? (y / n)')
workers = {}

class Pay:
    hourlypay = 1000
    workinghour = 0
    workera = ''
    workerid = 'A' + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
        
    def getname(self, n):
        self.workera = n
        return self.workera
    
    def gethour(self, gh):
        self.workinghour = self.workinghour + gh
        return self.workinghour

    def getid(self):
        workers[self.workera] = self.workerid
        return workers
    
    def payraise(self, ra):
        self.hourlypay = self.hourlypay + ra
        return self.hourlypay
    
    def caculatedaypay(self):
        return self.hourlypay * self.workinghour
        
    def caculatemonthpay(self):
        return self.caculatedaypay() * 30
    
    def caculatemonthhour(self):
        return self.workinghour * 30

num = 1
worker1 = Pay()
while op == 'y':
    n = input("What is the worker's name?")
    if n in workers.keys():
        print('The worker is', n + ', and his / her id is', workers[n])
    else:
        print('This is an unknown worker, we will set an id and name record for him / her.')
        worker1.getname(n)
        worker1.getid()
        print('This is his / her id :', workers[n])
    print('Does he want to increase his / her working hour?')
    print('His / Her working hours is', worker1.workinghour, 'hours a day. (y / n)')
    h = input()
    if h == 'y':
        gh = int(input('How many hours does he / she wants to increase?'))
        worker1.gethour(gh)
        print('Now, he / she needs to work', worker1.workinghour, 'hours a day.')
    r = input('Do you want to increase the salary? (y / n)')
    if r == 'y':
        ra = int(input('How much would you like the salary increase?'))
        worker1.payraise(ra)
        print("Now, the worker's salary is", worker1.hourlypay)
        print('==========================')       
    print(worker1.workera + "'s hourly pay :", worker1.hourlypay, 'dollars')
    print('==========================')
    x = worker1.caculatedaypay()
    print(worker1.workera + "'s daily pay :", x, 'dollars')
    print('==========================')
    y = worker1.caculatemonthpay()
    w = worker1.caculatemonthhour()
    print(worker1.workera + "'s monthly pay :", y, 'dollars')
    print(worker1.workera + "'s total hours :", w, 'hours')
    print('')
    print('Do you want to check', n + "'s system again? (y / n)")
    op = input()

if op == 'n':
    print('')
    print('Bye!')