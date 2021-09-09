from collections import deque
def flood_fill(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    rows = len(image)
    cols = len(image[0])
    
    old_color = image[pixel_row][pixel_column]
    if old_color != new_color:
        
        q = deque([(pixel_row,pixel_column)])
        #visited = set()
        #visited.add((pixel_row,pixel_column))
        
        image[pixel_row][pixel_column]=new_color
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            row,col = q.popleft()
            
            for dx, dy in dirs:
                r = row +dx
                c = col +dy
                
                if 0<=r<rows and 0<=c<cols and image[r][c]==old_color :
                    image[r][c]=new_color
                    #visited.add((r,c))
                    q.append((r,c))
            
    return image