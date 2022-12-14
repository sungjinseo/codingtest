# 소스코드를 작성하는 공간입니다. 코딩을 하기 위해서는 writefile 라인을 주석처리해주세요
# 주피터노트북에서는 입력시 input()을 사용하고 제출시 sys.stdin.readline() 으로 변경하세요~성능차이남
# 입력 부
rows, cols = input().split()
board = [];
rows = int(rows)
cols = int(cols)
for row_x in range(rows):
    board.append(input().split())

board = [[int(board[x][y]) for y in range(cols)] for x in range(rows)]

# 처리부
# 방문플래그
visited = [[False]* cols for _ in range(rows)]

# 시계방향으로 검색
dx = [0,1,0,-1]
dy = [1,0,-1,0]

jobQ = [];
paint_cnt, paint_size = 0, 0

# 2차원 배열의 전체를 탐색
for row_x in range(rows):
    for col_y in range(cols):
        if(visited[row_x][col_y] or board[row_x][col_y] != 1): 
            continue
        
        
        # 방문하지 않은 좌표를 입력하고 그림을 그린다.
        # 이게 시작일때는 사이즈를 찾을 수 있다.
        jobQ.append([row_x, col_y])
        visited[row_x][col_y] = True
        paint_cnt +=1
        temp_size = 1
            
        while(len(jobQ)>0):
            cursor = jobQ.pop()
            for ax in range(4):
                nx = cursor[0] + dx[ax]
                ny = cursor[1] + dy[ax]
                # 배열의 범위를 벗어나면 검색안함
                if(nx < 0 or nx >= rows or ny < 0 or ny >= cols): 
                    continue
                
                #방문지역이거나 방문이 필요없으면 스킵
                if(visited[nx][ny] or board[nx][ny] != 1): 
                    continue
                    
                # 방문 플래그를 남기고 미방문지역추가, 넓이 증가
                visited[nx][ny] = True
                jobQ.append([nx, ny])
                temp_size+=1
        
        if temp_size > paint_size : paint_size = temp_size
                
        
print(paint_cnt, paint_size) 
