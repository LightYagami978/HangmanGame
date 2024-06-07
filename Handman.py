import random
from collection import words
import string

def get_valid_word(words):               #getting a random valid word from words
    word = random.choice(words)
    while ' 'in word or '-'in word:
        word = random.choice(words)
    return word

def hangman():
    
    word=get_valid_word(words).upper()
    life = len(word)+5
    word_letters= set (word)
    alphabet = set(string.ascii_uppercase)
    used_letters=set()
    
    while len(word_letters)>0 and life>0:

        print("You have used these letters: " , " ".join(used_letters))


        word_list= [letter if letter in used_letters else '-' for letter in word ]
        print("Current word: " , " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else :
                life -=1
                

        elif user_letter in used_letters:
            print("It's already used, try another letter:  ")
        else :
            print ("Invalid input.")
        
        
    if life==0:
        print(f"Womp Womp you cant guess a single word, it was : {word}")
    else :
        print("You Won the Word was : ",word)

hangman()