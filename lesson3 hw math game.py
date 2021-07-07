import random
gt = 0
number = random.randint(1, 20)
print("I'm thinking of a number.")

while gt < 6:
    print("Guess a number between 1 and 20!")
    guess = int(input())
    
    gt = gt + 1
    
    if guess < number:
        print("Your guess is too low")
        
    if guess > number:
        print("Your guess is too high")
        
    if guess > 20 or guess < 1:
        print("You wasted a guess!")
        
    if guess == number:
        break
    
if guess == number:
    print("Good game! You guess my number with", str(gt), "guesses!")
    
if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was", str(number))
    