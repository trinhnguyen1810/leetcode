from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
      direction = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
      q = deque([(0,0,1)])
      visited = set([(0, 0)])
      n = len(grid)
      if grid[0][0] == 1:  # Add this check
        return -1

      while q:
        r,c,l = q.popleft()
        if r == n-1 and c == n-1:
          return l
        for dx,dy in direction:
          new_r,new_c = r + dx, c + dy
          if 0<=new_r<n and 0 <= new_c<n and grid[new_r][new_c] == 0 and (new_r,new_c) not in visited:
            q.append((new_r,new_c,l+1))
            visited.add((new_r,new_c))
      return -1


      