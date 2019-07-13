from numpy.random import choice
import time

class Cell:
    def __init__(self, state, neighbour_count):
        self.state = state
        self.neighbour_count = neighbour_count
        self.next_state = state

    # Assumes neighbour count can't be 0 (why would it ever be?)
    def evalState(self, cells):
        count = 0
        for cell in cells:
            if (cell.state == True):
                count += 1
                if count == self.neighbour_count:
                    self.next_state = True
                    return
        self.next_state = False
        return

    def update(self):
        self.state = self.next_state

    def __repr__(self):
        if self.state == True:
            return "#"
        return " "

# Takes width w, height h, steps, moore's number, neighbour count, true/false weight
def gen(w, h, steps, moores, neighbour_count, weight):
    board = []
    for y in range(h):
        row = []
        for x in range(w):
                row.append(Cell(choice([True,False],p=[weight,1-weight]), neighbour_count))
        board.append(row)

    for i in range(steps):
        print("\n\n\nITERATION", i)
        for line in board:
            print(line)
        for (y, row) in enumerate(board):
            for (x, cell) in enumerate(row):
                # We do one useless update at the start bcuz im too lazy to setup the iterator twice and an added conditional is dumb
                board[x][y].update()
                neighbours = get_neighbours(w, h, x, y, moores, board)
                board[x][y].evalState(neighbours)

        time.sleep(0.1)

    print("\n\n\n****FINAL RESULT****")
    for line in board:
        print(line)
    time.sleep(1)

# Takes size of board, position in array + moore's number, returns array of neighbour cells
def get_neighbours(w, h, x, y, moores, board):
    neighbours = []

    for shift_x in range(-moores, moores+1):
        for shift_y in range(-moores, moores+1):
            neighbours.append(board[(x+shift_x)%w][(y+shift_y)%h])
    del neighbours[pow(2*moores+1,2)//2]

    return neighbours


while True:
    gen(w=50, h=50, steps=15, moores=1, neighbour_count=5, weight=0.6)
