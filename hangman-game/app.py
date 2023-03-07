import random

animal_list = ["lion", "tiger", "elephant", "giraffe", "hippopotamus", "rhinoceros", "leopard", "cheetah", "zebra",
               "gazelle", "kangaroo", "koala", "wombat", "platypus", "crocodile", "alligator", "snake", "spider", "scorpion", "octopus"]
word_list = ["apple", "banana", "coffee", "dinner", "family", "happy", "jacket", "kitchen", "laptop",
             "money", "music", "phone", "pizza", "school", "sleep", "smile", "table", "toilet", "water", "window"]


animal_hints = {
    "lion": "It's a big cat with a mane",
    "tiger": "It's a striped big cat",
    "elephant": "It's a large gray mammal with a trunk",
    "giraffe": "It's a tall mammal with a long neck",
    "hippopotamus": "It's a large gray mammal with a big mouth",
    "rhinoceros": "It's a large gray mammal with a horn",
    "leopard": "It's a spotted big cat",
    "cheetah": "It's a spotted big cat known for its speed",
    "zebra": "It's a striped mammal similar to a horse",
    "gazelle": "It's a fast, slender-horned antelope",
    "kangaroo": "It's a marsupial with a long tail that hops",
    "koala": "It's a cute, furry marsupial that eats eucalyptus leaves",
    "wombat": "It's a furry burrowing marsupial",
    "platypus": "It's a unique, egg-laying mammal with a bill",
    "crocodile": "It's a large reptile with a long snout and sharp teeth",
    "alligator": "It's a large reptile similar to a crocodile",
    "snake": "It's a long, legless reptile that crawls",
    "spider": "It's an eight-legged arachnid that spins webs",
    "scorpion": "It's an arachnid with a stinger on its tail",
    "octopus": "It's a sea creature with eight arms and a bulbous head",
}

word_hints = {
    "apple": "It's a round fruit that is usually red or green",
    "banana": "It's a yellow fruit that is long and curved",
    "coffee": "It's a drink made from roasted beans",
    "dinner": "It's a meal that is usually eaten in the evening",
    "family": "It's a group of people who are related to each other",
    "happy": "It's a feeling of joy or contentment",
    "jacket": "It's a type of outerwear worn over a shirt",
    "kitchen": "It's a room where food is prepared and cooked",
    "laptop": "It's a portable computer that can be used on your lap",
    "money": "It's a medium of exchange used to purchase goods and services",
    "music": "It's an art form that involves sounds arranged in a pleasing way",
    "phone": "It's a device used for communication",
    "pizza": "It's a flat bread topped with tomato sauce, cheese, and other ingredients",
    "school": "It's a place where students go to learn",
    "sleep": "It's a state of rest where you are unconscious and unaware of your surroundings",
    "smile": "It's a facial expression that shows happiness or pleasure",
    "table": "It's a piece of furniture with a flat top and one or more legs",
    "toilet": "It's a fixture used for human waste disposal",
    "water": "It's a clear, colorless liquid that is essential for life",
    "window": "It's an opening in a wall or door that allows light and air to enter",
}

word = ""
hint_counter = 0
big_hint_counter = 0
used_char = []
none_used_char = []
chances = 0


def check_category():
    
    global word, chances
    
    try:
        choice = int(input("which category do you want to choose? (1) animals or (2) words: "))

        if choice == 1:
            print("you chose animals")
            word = random.choice(animal_list)
            
            

        elif choice == 2:
            print("you chose words")
            word = random.choice(word_list)
            
            
        else:
            print("please enter a valid choice")
            check_category()
    

    except ValueError:
        print("please enter a number")
        check_category()
    
    
    chances = len(word) + 1

    


def hint():
    global hint_counter
    hint_counter += 1
    print(random.choice(word))


def big_hint(word):
    global big_hint_counter 
    big_hint_counter += 1
    print(animal_hints[word] if word in animal_hints.keys() else word_hints[word])
    
    


def main_game():
    global chances
    result = ("-" * len(word))
    
    while chances > 0:
        print(result)

        char = input("Enter a character: ")
        
        if char == "i'm_stupid":
            #chances += 1
            hint()
        elif char == "i'm_really_stupid":
            big_hint(word)

        elif len(char) > 1:
            print("Enter only 1 character")

        elif char in used_char or char in none_used_char:
            print("you already used this character")
            print(f"{chances} chances  left")
            continue

        else:
            used_char.append(char)

        if char in word:
            chars = [i for i, letter in enumerate(word) if letter == char]

            # needed this to handle a word like tree which has two e's
            for item in chars:
                result = result[:item] + char + result[item + 1:]

            if result == word:
                print(f"""
             :D     you won
             \|/    your word was {word}
              |     you said you're stupid {hint_counter} times...
             /|\\   and you said you're really stupid {big_hint_counter} times...
              """)
                exit()

        else:
            chances -= 1
            if char in none_used_char:
                chances += 1

            none_used_char.append(char)
            print(f"{chances} chances  left")
            
    else:
        print(f"""
              D:    you lost
             \|/    your word was {word}
              |     you said you're stupid {hint_counter} times...
             /|\\   and you said you're really stupid {big_hint_counter} times...
              """)



print("Welcome to Hangman!")
print("You have to guess the word by guessing one character at a time")
print("you can use << im_stupid >> to get a random and maybe already suggested letter :D ")
print("you can use << im_really_stupid >> to get a description for the word :D ")


check_category()
print(f"you word has {len(word)} characters and you get {chances} chances to guess")
    
main_game()