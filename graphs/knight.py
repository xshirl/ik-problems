# Complete the function below.
from collections import deque
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # Write your code here.
    visited = [[0]*cols for _ in range(rows)]
    q = deque([(start_row, start_col, 0)])
    visited[start_row][start_col] = 1
    
    while q:
        ux, uy, level = q.popleft()
        if ux == end_row and uy == end_col: return level
        for dx, dy in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]:
            vx, vy = ux+dx, uy+dy
            if not (0<=vx<rows and 0<=vy<cols): continue
            if not visited[vx][vy]: 
                q.append((vx,vy,level+1))
                visited[vx][vy] = 1
    return -1