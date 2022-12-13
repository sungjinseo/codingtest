# 소스코드를 작성하는 공간입니다. 코딩을 하기 위해서는 writefile 라인을 주석처리해주세요
# 주피터노트북에서는 입력시 input()을 사용하고 제출시 sys.stdin.readline() 으로 변경하세요~성능차이남
board = [];
board.append([1,1,1,0,1,0,0,0,0,0])
board.append([1,0,0,0,1,0,0,0,0,0])
board.append([1,1,1,0,1,0,0,0,0,0])
board.append([1,1,0,0,1,0,0,0,0,0])
board.append([0,1,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0,0])
board.append([0,0,0,0,0,0,0,0,0,0])

visited = [[False]* m for _ in range(n)]

# 시계방향으로 검색
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n = len(board)
m = len(board)

jobQ = [];
#jobQ.append(x,y)
jobQ.append([0,0])
visited[0][0] = True
while(len(jobQ)>0):
    cursor = jobQ.pop()
    for idx in range(4):
        nx = cursor[0] + dx[idx]
        ny = cursor[1] + dy[idx]
        if(nx < 0 or nx >= n or ny < 0 or ny >= m): 
            continue
        if(visited[nx][ny] == True or board[nx][ny] != 1): 
            continue
        visited[nx][ny] = True
        jobQ.append([nx, ny])
        
for i in visited:
    print(i)
