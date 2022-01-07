import random

option = {
    0: (1,6),
    1: (1,12),
    2: (1,24)
}

# to reuse rock,paper,scissor validation
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

dice_type = get_input("Enter 0 for 6-sided dice, 1 for 12-sided dice and 2 for 24-sided dice ")
range= option[dice_type]

print(f"The dice rolled {random.randint(range[0], range[1])}")