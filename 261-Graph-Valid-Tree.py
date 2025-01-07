class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
      """
      build an adjacency list
      for each node do a dfs until:
          if that node is visited return False
          if that node is in prev continue
          if that node is valid: 
              do a dfs
              add to visited list
          return True
      
      return dfs and len(visited) == len(n)
      """
      par = list(range(n))
      rank = [0] * n
      if n == 0:
            return False
        
      if len(edges) != n - 1:
          return False
      
      def find(n1):
        while n1 != par[n1]:
          par[n1] = par[par[n1]]
          n1 = par[n1]
        return n1
      
      def union(n1,n2):
        res_n1, res_n2 = find(n1),find(n2)
        if res_n1 == res_n2:
          return False
        if rank[res_n1] >= rank[res_n2]:
          rank[res_n1] += rank[res_n2]
          par[res_n2] = par[res_n1]
        else:
          rank[res_n2] += rank[res_n1]
          par[res_n1] = par[res_n2]
        return True

      for a, b in edges:
        if not union(a,b):
          return False
      return True



        