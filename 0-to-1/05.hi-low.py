import random

def computer_choice():
    num = random.randint(1, 100)
    return num

# to reuse some of rock paper scissor while loop
def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except:
            print("Invalid input. Enter 1 to 100 only")
            continue
        
        if value <1 or value >100:
            print("Invalid input. Enter 1 to 100 only")
            continue
        else:
            break
    return value

cc = computer_choice()


attempt = True
while attempt:
    guess = get_input("Guess the number, Enter 1 to 100 -> ")
    if guess < cc:
        print("Your guess is too low")
    elif guess > cc:
        print("Your guess is too high")
    else:
        print(f"You got it, the number is {cc}")    
        attempt = False