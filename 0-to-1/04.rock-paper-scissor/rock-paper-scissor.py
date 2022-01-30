import random

result = [['Tie', 'Human win', 'Computer win'], ['Computer win', 'Tie', 'Human win'], ['Human win', 'Computer win', 'Tie']]
dict = {
    0: "rock",
    1: "paper",
    2: "scissor"
}

def computer_choice():
    num = random.randint(0, 2)
    return num

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

hc = get_input("Enter 0 for rock, 1 for paper and 2 for scissor ")
cc = computer_choice()

print(f"computer select {dict[cc]}")
print(f"u choose {dict[hc]}")
print(f"-->> {result[cc][hc]} <<--")
