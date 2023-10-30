import time
import random


def speed_typing_test():
    words = ['computer', 'network', 'generating', 'codeclause', 'security', 'python', 'code', 'speed', 'typing', 'test']
    random_word = random.choice(words)

   
    print("Your word is: " + random_word)
    input("Press Enter when you are ready to start typing...")

   
    start_time = time.time()
    user_input = input("\nType the word: ")

    end_time = time.time()

    
    speed = end_time - start_time

   
    if user_input == random_word:
        print("\nCorrect! You typed '", random_word, "' correctly.")
        print("Your typing speed is: " + str(speed) + " seconds")
    else:
        print("\nIncorrect! You made a mistake typing '", random_word, "'.")


speed_typing_test()
