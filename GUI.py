def wheretoshot():
    row = input("Input row to shoot: ")
    column = input("Input column to shoot: ")
    if row.isdigit() and column.isdigit():
        return int(row), int(column)
    else:
        return 0, 0

def askforboardsize():
    xDimension = input("Provide how many cells should be horizontally: ")
    yDimension = input("Provide how many cells should be vertically: ")
    if xDimension.isdigit() and yDimension.isdigit():
        print("Now lets place the Ships!")
        return xDimension, yDimension
    else:
        return 10, 10

def askforshiptoplace():
    print("If any parameter will be wrong the ship places on 0,0 with size 1")
    size = input("Provide size of ship 1-4: ")
    xPos = input("Provide X position of ship nose: ")
    yPos = input("Provide Y position of ship nose: ")
    allign = input("Should be horizontal/vertical? Type 0/1 respectively: ")
    print("==========================================")
    if size.isdigit() and xPos.isdigit() and yPos.isdigit() and allign.isdigit():
        if allign == 0:
            return size, xPos, yPos, True
        elif allign == 1:
            return size, xPos, yPos, False
    else:
        return 1, 0, 0, True

def printboard(board):
    print(end="   ")
    for i in range(0, len(board.getships())):
        print(str(i),end=" ")
    print()
    print("  "+ "_"*2*len(board.getships()[0]),end="")
    print()
    for row in range(0,len(board.getships())):
        print(str(row)+"|", end =" ")
        for column in range(0,len(board.getships()[row])):
            print(board.getships()[row][column].tostring(row, column), end=" ")
        print()