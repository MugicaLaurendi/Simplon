def dirReduc(arr):

    ns = 0
    we = 0

    for dir in arr :
        if dir == "NORTH" :
            ns += 1
        if dir == "SOUTH" :
            ns -= 1
        if dir == "WEST" :
            we += 1
        if dir == "EST" :
            we -= 1

    if ns > 0 :
        l =





aru = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(aru))
