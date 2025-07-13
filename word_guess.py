import random



def guess_word():
    words = [
        "apple", "house", "chair", "table", "plant", "water", "green", "music", "light", "stone",
        "castle", "puzzle", "rocket", "python", "jungle", "magnet", "pencil", "silver", "pirate", "planet",
        "avalanche", "dinosaur", "galactic", "strategy", "vortex", "phantom", "equation", "umbrella", "frequent", "machine",
        "giraffe", "octopus", "tiger", "penguin", "zebra",
        "gravity", "neutron", "quantum", "voltage", "reaction"
    ]
    tryes:int = 10
    word = random.choice(words) 
    x = ['_' for _ in range(len(word))]
    word_list = list(word)
    print(f"Current word: {"".join(x)}")
    while tryes > 0:
        if '_' in x:
            letter = input("Guess a letter: ")
            if letter in word_list:
                print("Good guess!!")
                for i ,l in enumerate(word_list):
                    if l == letter: 
                        x[i] = letter
            else:
                tryes -= 1
                print("Wrong guess! Attempt left: " + str(tryes)) 
            print(f"Current word: {"".join(x)}")  
        else:
            print(f"Congratulation!! You guessed the word: {word}")
            break   
    else:
        print(f"Unfortunately you failed!! the word was: {word}")      



if __name__ == "__main__":
    guess_word()

  