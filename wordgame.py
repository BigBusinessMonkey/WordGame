"""
Word game:
Player has limited number of guesses
Player guesses letter
Returns word with letters filled in
Repeat
Intend to increase complexity by adding hint functionality, levels of difficulty, ability to guess words, etc
Opted not to include hint functionality due to abusable nature and simplicity of game.
"""
import random
def game():
    #difficulty = input("Which difficulty would you like to play on? (Available difficulties are: easy/medium/difficult/obscure)")
    #if(difficulty == easy):    


    raw = open("words.txt", "r")
    dic = (raw.read()).split()
    raw.close()
    randomNum = random.randint(1,len(dic))

    word = (dic[randomNum - 1])

    word = list(word)
    chances = int((len(word) ** (0.8)) + 7) 

        
    print("This is a word game. A word has been generated, and it is up to you to guess what it is. You may see a list of all previous guesses at any time by typing \'guessed\' as a guess.")
    print("This round the word has " + str(len(word)) + " characters. You have " + str(chances) + " chances.")



    Board = str("_" * len(word))
    Board = list(Board)
    Guessed = []
    while True:
        if(chances == 0):
            print("Sorry, you failed to guess correctly! The word was " + "".join(word) + ".")
            Quit = input("Would you like to play again? (y/n)")
            if(Quit == "y"):
                game()
            else:
                break
        elif(Board == word):
            print("Congratulations, you found the word!")
            print("tinyurl.com/mc7m96q")
            Quit = input("Would you like to play again? (y/n)")
            if(Quit == "y"):
                game()
            else:
                break
        else:
            #Guessing interface
            Guess = (input("Take your guess: ")).lower()
            iteration = 0
            for letter in word:
                if(Guess == "guessed"):
                    print(Guessed)
                    break
                elif(len(Guess) > 1 or len(Guess) < 1):
                    print("Remember, single characters only.\n")
                    break
                elif(Guess not in word and Guess not in Guessed):
                    chances -= 1
                    print("No instance of that letter in the word!\n")
                    break
                elif(letter == Guess and Guess not in Guessed):
                    Board[iteration] = Guess
                    iteration += 1 
                    print("You found a letter!\n")
                    continue
                elif(Guess in Guessed):
                    print("You have already guessed that. \n")
                    break
                elif(letter != "_"):
                    iteration += 1
                    continue

            if(Guess != "guessed"):
                Guessed.append(Guess)
     
                
                
            print(" ".join(Board))
            if(" ".join(Board) == word):
                pass
            else:
                print("You have " + str(chances) + " chances remaining.")
            
game()
            

            