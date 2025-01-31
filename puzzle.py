import random
import sys

class Puzzle:
    def __init__(self):
        self.board = [[0 for x in range(3)] for y in range(3)]
        self.board_solved()

    def __str__(self):
        meow ="--------------\n\n"
        for x in range (3):
            for y in range(3):
                meow += (str(self.board[x][y]) +" ")
            meow += "\n"
        return meow
    def board_solved(self):
        self.board[0][1] = 1
        self.board[0][2] = 2

        self.board[1][0] = 3
        self.board[1][1] = 4
        self.board[1][2] = 5

        self.board[2][0] = 6
        self.board[2][1] = 7
        self.board[2][2] = 8

    def openSpot(self):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    return x, y
        return -1

    def up(self):
        y, x = self.openSpot()
        if y == 0 or y==1:
            self.board[y][x] = self.board[y+1][x]
            self.board[y+1][x] = 0

        elif y==2:
            pass
        else:
            print('error invalid')

    def down(self):
        y, x = self.openSpot()

        if y == 2 or y == 1:
            self.board[y][x] = self.board[y - 1][x]
            self.board[y - 1][x] = 0

        elif y == 0:
            pass
        else:
            print('error invalid')

    def right(self):

        y, x = self.openSpot()

        if x == 0:
            pass
        elif x == 1 or x==2:
            self.board[y][x] = self.board[y][x-1]
            self.board[y][x-1] = 0
        else:
            print('meow')

    def left(self):

        y,x= self.openSpot()

        if x == 2:
            pass
        elif x ==1 or x==0:
            self.board[y][x] = self.board[y][x+1]
            self.board[y][x+1] = 0
        else:
            print('meow')

    def randomize(self, number=2000):
        for x in range(number):
            what = random.randint(1, 4)
            match what:
                case 1:
                    self.up()
                case 2:
                    self.down()
                case 3:
                    self.right()
                case 4:
                    self.left()


if __name__ == '__main__':
    meow = Puzzle()
