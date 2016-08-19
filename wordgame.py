"""
Word game:
Play has limited number of guesses
Player guesses letter
Returns word with letters filled in
Repeat
Player can guess word at any time, but uses up two guesses if incorrect
"""
import random



raw = open("words.txt", "r")
dic = (raw.read()).split()
raw.close()
randomNum = random.randint(1,len(dic))

word = (dic[randomNum - 1])
word = list(word)
chances = len(word) * 2 - 2
if(chances > 10):
    chances = 10
    
print("This is a word game. A word has been generated, and it is up to you to guess what it is.")
print("This round the word has " + str(len(word)) + " characters.")
print("You may guess letters, or you may guess words. Letters utilise one guess, words two. You have " + str(chances) + " guesses.")

#letter guessing
Board = str("_" * len(word))
Board = list(Board)
Guessed = []
for chance in range(10000):
    if(chances == 0):
        print("Game over. The word was " + "".join(word))
        break
    elif("".join(Board) == word):
        print("Congratulations, you found the word!")
        break
    else:    
        Guess = input("Take your guess: ")
        iteration = 0
        for letter in word:
            if(letter == Guess and Guess not in Guessed):
                Board[iteration] = Guess
                iteration += 1 
                print("You got a letter!")
                continue
            elif(Guess in Guessed):
                print("You have already guessed that. \n")
                break
            elif(letter != "_"):
                iteration += 1
                continue
            elif(Guess in Guessed):
                print("You have already guessed that letter.")
                print(Guessed)
                break
            else:
                print("The word does not contain that letter.")
                chances -= 1
                Guessed.append(Guess)
                break
        Guessed.append(Guess)
 
            
            
        print(" ".join(Board))
        print("You have " + str(chances) + " chances remaining.")
        

        

        