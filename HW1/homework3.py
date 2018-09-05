import Traverse
import SA

def init():
    f = open('input.txt','r')
    input = f.read().splitlines()
    method = input[0]
    n = int(input[1])
    p = int(input[2])
    segments = [[]]
    segNo = 0
    blocks = []
    if n != 0:
        for i in range(n):
            for j in range(n):
                if input[i+3][j] == '0':
                    segments[segNo].append((i,j))
                elif input[i+3][j] == '2':
                    blocks.append((i,j))
                    if segments[segNo] != [] and not (i == n - 1 and j == n - 1):
                        segNo = segNo + 1
                        segments.append([])
            if i != n - 1 and segments[segNo] != []:
                segNo = segNo + 1
                segments.append([])
    return method, n, p, segments, blocks

def output(blocks, Track, n):
    f = open('output.txt','w')
    if Track == []:
        f.write('FAIL')
        return 0
    else:
        f.write('OK')
        for i in range(n):
            f.write('\n')
            for j in range(n):
                if (i,j) in Track:
                    f.write('1')
                elif (i,j) in blocks:
                    f.write('2')
                else:
                    f.write('0')
        return 1

method, n, p, segments, blocks = init()
if len(segments) < p-n:
    Track = []
elif segments == [[]] and p > 0:
    Track = []
else:
    if method == 'DFS' or method == 'BFS':
        Track = Traverse.Traverse_Main(blocks, method, n, p, segments)
    elif method == 'SA':
        Track = SA.SA_Main(blocks, n, p, segments)
    else:
        Track = []
output(blocks, Track, n)
