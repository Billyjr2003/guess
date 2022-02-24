import random

def guess(x) :
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number :
    guess = int(input(f"guess a number between 1 and {x}"))
    if guess < random_number :
      print ("it is too low")
    elif guess > random_number : 
      print("it is too high ")  
    else : 
      print ("yaaaaay you guess the right number ")  
    print(guess)  
guess(10)  