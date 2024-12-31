import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize the board with infinite values
        board = [float('inf')] * n
        board[k - 1] = 0  # Starting point distance is 0
        
        # Create adjacency list
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u - 1].append((v - 1, w))
        
        # Priority queue for Dijkstra's algorithm
        q = [(0, k - 1)]  # (distance, node)
        while q:
            weight, u = heapq.heappop(q)
            
            # Iterate through neighbors of the current node
            for v, w in adj_list[u]:
                if board[v] > weight + w:
                    board[v] = weight + w
                    heapq.heappush(q, (board[v], v))
        
        # Find the maximum time it takes to reach any node
        max_time = max(board)
        return max_time if max_time != float('inf') else -1
