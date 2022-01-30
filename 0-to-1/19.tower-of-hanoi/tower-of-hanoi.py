def display():
    global counter
    counter = counter + 1
    print(f"Step  : {counter}")
    print("~~~~~~~~~~~~~~~~~~~~")
    print(f"Source: {r_source}")
    print(f"Temp  : {r_temp}")
    print(f"Target: {r_target} \n")
    # print(f"Step  : {counter} \n")

def move_tower(disks, actual, target, temporary):
    if disks == 1:
        display()
        actual.pop()
        target.append(1) #shift Disk 1 to target
        return
    elif disks == 2:
        display()
        actual.pop()
        temporary.append(1) #shift Disk 1 to temporary
        display()
        
        actual.pop()
        target.append(2) #shift Disk 2 to target
        display()
        
        temporary.pop()
        target.append(1) # shift Disk 1 to target
        return
    else:
        move_tower(disks - 1, actual, temporary, target)
        display()
        actual.pop()
        target.append(disks) #shift last Disk to target
        move_tower(disks - 1, temporary, target, actual)
        
counter = -1
total_disk = 4
r_source = list(range(total_disk, 0, -1))
r_temp = []
r_target = []

move_tower(total_disk, r_source, r_target, r_temp)
display()