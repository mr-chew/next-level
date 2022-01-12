import random

#word list
wordlist = ["scarys", "ginger", "sportys", "baby", "poshs"]
#randomly choose a word and print the ----- to represent the length
word = wordlist[random.randint(0, 4)]
blanks = "-"*len(word)
print(blanks)

def replace(str, position, char):
    return str[:position] + char + str[position+1:]

strikes = 0
found = False

# check if input in word
while strikes <5 and not found:
    guess = input("Guess a letter of the word -> ")
    if guess in word:
        index = [n for n in range(len(word)) if word.find(guess, n) == n]
        for i in index:
            blanks = replace(blanks, int(i), guess)
    else:
        strikes +=1
        print(f"you have {strikes} strikes")
    print(blanks)
    if "-" not in blanks:
        found = True