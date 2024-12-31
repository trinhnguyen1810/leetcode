from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
      dist = [float('inf')]*n
      dist[src] = 0
      for _ in range(k+1):
        temp_dist = dist[:]
        for u,v,w in flights:
          if dist[u] != float('inf'):
            temp_dist[v] = min(dist[u]+w, temp_dist[v])
        dist = temp_dist
      return dist[dst] if dist[dst] != float('inf') else -1


      




        