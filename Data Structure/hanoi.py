# plate : number of plates you will move
# from_pos : starting point of the plate
# to_pos : ending point of the plate
# mid_pos : to move the plate, helper position.

def hanoi_tower(plate, from_pos, to_pos, mid_pos):
    if plate == 1:
        print(from_pos, "=>", to_pos)
        return

    # when it starts from " plate - 1 " plates to move
    hanoi_tower(plate - 1, from_pos, mid_pos, to_pos)
    # the biggest one goes to ending point
    print(from_pos, "=>", to_pos)
    # " plate - 1 " plates goes to " mid_pos " to " to_pos ".
    hanoi_tower(plate - 1, mid_pos, to_pos, from_pos)

print("only one plate")
hanoi_tower(1, 1, 3, 2)
print("two plates")
hanoi_tower(2, 1, 3, 2)
print("three plates")
hanoi_tower(3, 1, 3, 2)