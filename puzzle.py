import random
import sys

class Puzzle:

    def __init__(self, puzzleSize=3):
        self.board = [[0 for x in range(puzzleSize)] for y in range(puzzleSize)]

        self.sizeofpuzzle = puzzleSize
        self.board_solved()

    def __lt__(self, other):
        """For priority queue ordering: Compare based on heuristic value."""
        return sum(row.count(0) for row in self.board) < sum(row.count(0) for row in other.board)

    def __str__(self):
        meow ="--------------\n\n"
        for x in range (self.sizeofpuzzle):
            for y in range(self.sizeofpuzzle):
                if self.board[x][y] == 0:
                    meow += "  "
                else:
                    meow += str(self.board[x][y]) +" "
            meow += "\n"
        return meow

    def __eq__(self, other):
        if self.board == other.board:
            return True
        else:
            return False

    def board_solved(self):

        if self.sizeofpuzzle == 3:
            self.board[0][0] = 0
            self.board[0][1] = 1
            self.board[0][2] = 2

            self.board[1][0] = 3
            self.board[1][1] = 4
            self.board[1][2] = 5

            self.board[2][0] = 6
            self.board[2][1] = 7
            self.board[2][2] = 8
        elif self.sizeofpuzzle == 4:
            self.board[0][0] = 0
            self.board[0][1] = 1
            self.board[0][2] = 2
            self.board[0][3] = 3

            self.board[1][0] = 4
            self.board[1][1] = 5
            self.board[1][2] = 6
            self.board[1][3] = 7

            self.board[2][0] = 8
            self.board[2][1] = 9
            self.board[2][2] = 10
            self.board[2][3] = 11

            self.board[3][0] = 12
            self.board[3][1] = 13
            self.board[3][2] = 14
            self.board[3][3] = 15

    def openSpot(self):
        for x in range(self.sizeofpuzzle):
            for y in range(self.sizeofpuzzle):
                if self.board[x][y] == 0:
                    return x, y
        return -1,-1

    def up(self):
        y, x = self.openSpot()
        if y == 0 or y==1 or (y==2 and self.sizeofpuzzle==4):
            self.board[y][x] = self.board[y+1][x]
            self.board[y+1][x] = 0
            return True
        else:
            return False


    def down(self):
        y, x = self.openSpot()

        if y == 2 or y == 1 or (y==3 and self.sizeofpuzzle==4):
            self.board[y][x] = self.board[y - 1][x]
            self.board[y - 1][x] = 0
            return True

        else:
            return False

    def right(self):

        y, x = self.openSpot()

        if x == 0:
            pass
        elif x == 1 or x==2 or (x==3 and self.sizeofpuzzle==4):
            self.board[y][x] = self.board[y][x-1]
            self.board[y][x-1] = 0
            return True
        else:
            return False

    def left(self):

        y,x= self.openSpot()
        if x ==1 or x==0 or (x==2 and self.sizeofpuzzle==4):
            self.board[y][x] = self.board[y][x+1]
            self.board[y][x+1] = 0
            return True
        else:
            return False

    def find(self, num):
        for x in range(self.sizeofpuzzle):
            for y in range(self.sizeofpuzzle):
                if self.board[x][y] == num:
                    return x, y
        return -1, -1

    def randomize(self, number=200):
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
