from random import randint as r

with open ("names.txt") as f:
    names = f.readlines()
    
word = names[r(1,len(names))].lower()

chance = len(word) + (len(word) // 2 ) - 1

print(f"you have {chance} chances to guess the word: ")
output = list("_" * (len(word) -1) )
print(output,"\n")
#print(word)

guess = input("guess: ")

while range(0,chance):
    if guess in word:
        
        index = str.index(word,guess)
        output[index] = guess
        print(*output, sep='')
        if "_" not in output:
            print("you win")
            break
        guess = input("guess: ")
    else:
        print(f"wrong!")
        chance -= 1
        if chance == 0:
            continue
        print(f"{chance} chances left")
        
        guess = input("guess: ")
        
else:     
    print("you lose :D !!!")
