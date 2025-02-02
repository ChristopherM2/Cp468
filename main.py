import multiprocessing



from puzzle import Puzzle
from solver import Solver
import threading

FUNNYONE = False # Change to true to see the terrible 1 work (or not)
lite = False #only uses one heuristic, for testing purposes

puzzleSize = 4 # 3 or 4 supported, change for either 3x3 or 4x4 puzzle
number_of_puzzles = 100 # Number of puzzles to solve
max_threads = 1000 # Number of threads to use, if > number of puzzles, will use number of puzzles

"Uses a lot of memory, if limited lower number of puzzles or threads <3"

randomize = 5 # Number of random moves to make on the puzzle before solving
# more random moves = harder puzzle, = more ram, = bad idea
def solve_puzzle(index,lock,results):
    #Function to solve a puzzle and store results in a shared dictionary between threads.
    puzzle = Puzzle(puzzleSize)
    puzzle.randomize(randomize)
    solver = Solver(puzzle,puzzleSize)

    output = f"puzzle {index + 1}\n{puzzle}"

    if lite:
        heuristics = ['manhattan']
    elif FUNNYONE:
        heuristics = ['manhattan', 'misplaced','euclidian', 'goingFishing']
    else:
        heuristics = ['manhattan', 'misplaced','euclidian']
    for heuristic in heuristics:
        solution, moves = solver.solve(heuristic)
        if solution:
            output += f"\nHeuristic:{heuristic}, Path Length: {moves}, Number of nodes explored: {solver.nodes_explored}"

    with lock:
        results[index] = output

if __name__ == '__main__':
    puzzles = []
    print("This will take some time, please wait")
    print("-----------------------------------------")

    results = multiprocessing.Manager().dict()
    threads = []



    lock = multiprocessing.Lock()

    x = 0
    for i in range(number_of_puzzles):
            while len(threads) >= max_threads:
                for thread in threads:
                    if not thread.is_alive():
                        thread.join()
                        threads.remove(thread)
                        x += 1
                        print(f"Thread finished {x/number_of_puzzles*100:.2f}%")
            thread = multiprocessing.Process(target=solve_puzzle, args=(i, lock, results))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()


    for i in range(number_of_puzzles):
        print(results[i])
        print("\n-----------------------------------------")
