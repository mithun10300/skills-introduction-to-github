import random

Com_Guess= random.randint(1,10)
attempt = 0
print( " i am  thinking a number between 1 to 10, can you guess that ?")
while(True):
    user_guess= (input ("guess:"))
    
    
    if not user_guess.isdigit():
        print(" enter a valid number")
        continue
    user_guess=int(user_guess)
    attempt += 1
        
      
    
    if user_guess > Com_Guess:
     print("a bit high, try again:")

     
     
    
    elif user_guess < Com_Guess:
     print (" a bit low, try again")

    else:

     print(f"Congrats,  you guessed it right on your {attempt} attempts.")
     break
     

        
    
    
    