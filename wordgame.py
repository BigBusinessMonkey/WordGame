"""
Word game:
Player has limited number of guesses
Player guesses letter
Returns word with letters filled in
Repeat
Intend to increase complexity by adding hint functionality, levels of difficulty, ability to guess words, etc
"""
import random




raw = open("words.txt", "r")
dic = (raw.read()).split()
raw.close()
randomNum = random.randint(1,len(dic))

hintDic = {}

word = (dic[randomNum - 1])
word = list(word)
chances = len(word) * 2 - 2
if(chances > 10):
    chances = 10
    
print("This is a word game. A word has been generated, and it is up to you to guess what it is.")
print("This round the word has " + str(len(word)) + " characters.")



Board = str("_" * len(word))
Board = list(Board)
Guessed = []
while True:
    if(chances == 0):
        print("Game over. The word was " + "".join(word))
        break
    elif(Board == word):
        print("Congratulations, you found the word!")
        print("tinyurl.com/mc7m96q")
        break
    else:
        #Actual guessing part of things
        Guess = (input("Take your guess: ")).lower()
        iteration = 0
        for letter in word:
            if(Guess == "hint"):
                print(Hint)
                chances -= 2
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

        Guessed.append(Guess)
 
            
            
        print(" ".join(Board))
        print("You have " + str(chances) + " chances remaining.")
        

        

        