import random

dict = {
    0: "rock",
    1: "paper",
    2: "scissor"
}

def computer_choice():
    num = random.randint(0, 2)
    return dict[num]

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except:
            print("Invalid input. Enter 0,1,2 only")
            continue
        
        if value <0 or value >2:
            print("Invalid input. Enter 0,1,2 only")
            continue
        else:
            break
    return value

human_choice = get_input("Enter 0 for rock, 1 for paper and 2 for scissor ")
print(f"u choose {dict[human_choice]}")
print(f"computer select {computer_choice()}")

