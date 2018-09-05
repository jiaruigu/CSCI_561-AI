import random
import itertools
from math import e

def SA_Main(blocks,n,p,segments):
    times = 0
    board = SA_init(segments, p)
    ConflictMin = attackNo(board,blocks)
    Temperature = 50
    while ConflictMin != 0:
        ConflictMin_New = p*(p-1)/2
        i = random.randint(0, len(segments)-1)
        record_i = board[i]
        if record_i == ():
            C = 1
            rand_i = random.choice(segments[i])
            board[i] = rand_i
            while 1:
                j = random.randint(0, len(segments)-1)
                if board[j] != ():
                    break
            record_j = board[j]
            board[j] = ()
            ConflictMin_New = attackNo(board,blocks)
            board[j] = record_j
        else:
            C = 2
            rand_i = random.choice(segments[i])
            board[i] = rand_i
            ConflictMin_New = attackNo(board,blocks)
        board[i] = record_i
        if times == 100:
            Temperature = Temperature * 0.9
            times = 0
        else:
            times = times + 1
        E = ConflictMin - ConflictMin_New
        if E >= 0:
            ConflictMin = ConflictMin_New
            if C == 1:
                board[i] = rand_i
                board[j] = ()
            if C == 2:
                board[i] = rand_i
        elif random.random() < e**(E/Temperature):
            ConflictMin = ConflictMin_New
            if C == 1:
                board[i] = rand_i
                board[j] = ()
            if C == 2:
                board[i] = rand_i
        if Temperature < 0.00000001:
            return []
    return board

def SA_init(segments, p):
    board = []
    placement = list(itertools.combinations(range(len(segments)), p))
    t = placement[random.randint(0,len(placement)-1)]
    for i in range(len(segments)):
        if i in t:
            rand = random.choice(segments[i])
            board.append(rand)
        else:
            board.append(())
    return board

def attackNo(board, blocks):
    Conflict = 0
    for i in range(len(board)):
        if board[i] == ():
            continue
        for j in range(i+1,len(board)):
            if board[j] == ():
                continue
            attack0 = True
            attack1 = True
            x1 = board[i][0]
            x2 = board[j][0]
            y1 = board[i][1]
            y2 = board[j][1]
            if abs(y1 - y2) == abs(x1 - x2):
                for blk in blocks:
                    if (x1<blk[0]<x2 or x2<blk[0]<x1) and (y1<blk[1]<y2 or y2<blk[1]<y1) and abs(blk[0] - x1) == abs(blk[1] - y1):
                        attack0 = False
                        break
                if attack0 == True:
                    Conflict = Conflict + 1
            if y1 == y2:
                for blk in blocks:
                    if (x1<blk[0]<x2 or x2<blk[0]<x1) and y1 == blk[1]:
                        attack1 = False
                        break
                if attack1 == True:
                    Conflict = Conflict + 1
    return Conflict
