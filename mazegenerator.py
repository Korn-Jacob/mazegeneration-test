from random import randint
from sys import setrecursionlimit

# this is what we programmers call a really good idea with no possible unintended side effects whatsoever
setrecursionlimit(10**7)


class Node: 
    connections: set
    def __init__(self):
        self.connections = set([])
    
    def connect(self, node):
        self.connections.add(node)


def exists(a: int, b: int, board: list) -> bool:
    return a >= 0 and a < len(board) and b >= 0 and b < len(board[0])

def neighbours(a: int, b: int, board: list) -> list:
    out = []
    for d in [(0,1),(1,0),(0,-1),(-1,0)]:
        if exists(a+d[0],b+d[1], board):
            out.append((a+d[0],b+d[1]))
    return out


def connect(a: Node, b: Node) -> None:
    a.connect(b)
    b.connect(a)


def randomized_dfs(a: int, b: int, board: list, visited_cells: set):
    visited_cells.add((a,b))
    nbs = neighbours(a,b, board)

    while True:
        n = 0
        while n < len(nbs):
            if (nbs[n][0], nbs[n][1]) in visited_cells:
                del nbs[n]
                n -= 1
            n += 1
        if not len(nbs):
            return
        
        nb = nbs[randint(0,len(nbs)-1)]

        connect(board[a][b], board[nb[0]][nb[1]])
        randomized_dfs(nb[0], nb[1], board, visited_cells)


def randomized_dfs_maze(size: int):
    board = []
    for n in range(size):
        board.append([])
        for m in range(size):
            board[-1].append(Node())
    
    randomized_dfs(0, 0, board, set())

    out = []
    out.append(list("#." + "#" * (size*2 - 1)))
    for n in range(len(board)):
        out.append([])
        out[-1].append("#")
        for m in range(len(board[n])-1):
            out[-1].append(".")
            out[-1].append("." if board[n][m+1] in board[n][m].connections else "#")
        out[-1].append(".")
        out[-1].append("#")
        if n == len(board)-1: break
        out.append([])
        out[-1].append("#")
        for m in range(len(board[n])):
            out[-1].append("." if board[n+1][m] in board[n][m].connections else "#")
            if m != len(board[n])-1:
                out[-1].append("#")
        out[-1].append("#")
    out.append(list("#" * (size*2 - 1) + ".#"))
    return out
