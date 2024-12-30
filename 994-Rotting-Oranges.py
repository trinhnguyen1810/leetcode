class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS problem to calculate the time required for all oranges to rot.
        """
        from collections import deque

        # Initialize variables
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        minute = 0
        fresh_oranges = 0

        # Count fresh oranges and enqueue all initially rotten oranges
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # If there are no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0

        # Perform BFS
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and 
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2  # Mark orange as rotten
                        q.append((new_row, new_col))
                        fresh_oranges -= 1
            if q:  # Increment minute only if there are still oranges to process
                minute += 1

        # If there are still fresh oranges left, return -1
        return minute if fresh_oranges == 0 else -1
