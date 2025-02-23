import sys

move = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

#x, y일지라도, 리스트 접근은 y -> x 순서로 해야함!!!
def DFS(x, y) :
    global cnt, result
    #print(*visited, sep='\n')
    #print(stack)
    for d in range(4):
        rx, ry = x + move[d][0], y + move[d][1]
        # rx, ry가 그래프 리스트 안일 경우
        if rx >= 0 and rx < C and ry >= 0 and ry < R:
            temp = graph[ry][rx]
            #print(rx, ry)
            #방문하지 않았고, stack에 graph가 없는 경우
            if (not visited[temp]):
                visited[temp] = 1
                cnt += 1
                if cnt > result:
                    result = cnt
                DFS(rx, ry)
                #백트래킹
                visited[temp] = 0
                cnt -= 1

R, C = map(int, sys.stdin.readline().rstrip().split(' '))
graph = []
#visited = [ [False for x in range(C)] for y in range(R) ]
#시간초과떠서.. 딕셔너리로 초기화
visited = { x: 0 for x in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] }
cnt = 1
result = 1
for _ in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))
else:
    visited[graph[0][0]] = 1
    DFS(0, 0)
    print(result)