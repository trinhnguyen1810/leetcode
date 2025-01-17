class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
      """
       weights = [3,2,2,4,1,4], days = 3
       l,r = 1, 16 = 8

      """
      def feasible(k):
        count = 1
        current = 0
        for weight in weights:
          if current + weight > k:
            count += 1
            current = weight
          else:
            current += weight 
        if count > days:
          return False
        return True
        
      l, r = max(weights), sum(weights)
      res = r
      while l <= r:
        mid = l + (r-l) // 2
        if feasible(mid):
          res = min(res,mid)
          r = mid - 1
        else:
          l = mid + 1 
      
      return res

        