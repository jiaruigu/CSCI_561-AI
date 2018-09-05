import queue

def Traverse_Main(blocks, method, n, p, segments):
    if method == 'BFS':
        Tree = queue.Queue(n**n)
    elif method == 'DFS':
        Tree = queue.LifoQueue(n**n)
    else:
        return SA(blocks, n, p, segments)
    BlankSpace = len(segments) - p
    for i in range(BlankSpace + 1):
        for newNode in segments[i]:
            Tree.put((i, i, [], newNode))
    while 1:
        if Tree.empty():
            return []
        blanks, segNo, preNodes, currNode = Tree.get()
        newpreNodes = preNodes+[currNode]
        if not attack(blocks, preNodes, currNode):
            if len(newpreNodes) < p:
                for i in range(blanks, BlankSpace + 1):
                    for newNode in segments[segNo + i - blanks + 1]:
                        Tree.put((i, segNo + i - blanks + 1, newpreNodes, newNode))
            else:
                return newpreNodes

def attack(blocks, preNodes, currNode):
    attack0 = True
    attack1 = True
    for i in range(len(preNodes)):
        attack0 = True
        attack1 = True
        x1 = preNodes[i][0]
        x2 = currNode[0]
        y1 = preNodes[i][1]
        y2 = currNode[1]
        if abs(y1 - y2) == abs(x1 - x2):
            for blk in blocks:
                if (x1<blk[0]<x2 or x2<blk[0]<x1) and (y1<blk[1]<y2 or y2<blk[1]<y1) and abs(blk[0] - x1) == abs(blk[1] - y1):
                    attack0 = False
                    break
            if attack0 == True:
                return True
        if y1 == y2:
            for blk in blocks:
                if (x1<blk[0]<x2 or x2<blk[0]<x1) and y1 == blk[1]:
                    attack1 = False
                    break
            if attack1 == True:
                return True
    if (attack0 and attack1) or (not attack0 and not attack1):
        return False
    else:
        return True
