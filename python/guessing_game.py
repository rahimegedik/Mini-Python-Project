from random import randint
print("This program allows you to guess random numbers. \nI will think of a number between 1 and 100 \nand you will try to guess it. \nAfter each guess, I will give you a clue about \nwhether the correct number is higher or lower.")

def guessing_game():
    print("\nI'm thinking of a number between 1 and 100...")
    num = randint(1,10)
    gues = 0
    count = 0
    total_game=0
    total_guesses=0
    while(num != gues):
        gues=int(input("Your guess?"))
        count = count + 1
        if(gues<num):
            print("It's higher.")
        if(gues>num):
            print("It's lower.")
        if (num==gues):
            print("You got it right in " + str(count)+" guesses!")
        total_game = total_game + 1
        total_guesses += count 
    answer=input("Do you want to play again? ")
    
    if answer.startswith("Y") or answer.startswith("y"):
        guessing_game()
         
    else:
        print("Overall results: ")
        print("Total games   = " + str(total_game))
        print("Total guesses = " + str(total_guesses))
     
guessing_game()
