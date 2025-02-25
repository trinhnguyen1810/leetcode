\\\
[]

[-1,0,1,2,-1,-4]
Step 1: phan loai 0,0,0, negative, positive
Step 2: if there are 3 zeros, put it in the res
Step 3: If there are positives, check if the oposite in the negative
Step 4: If there are negatives, check if the opposite in the positive
Step 5: REMEMBER THIS CASE #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
\t#   i.e. (-3, 0, 3) = 0
\\\





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n,p,z = [], [], []
        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
            else:
                z.append(i)

        if len(z) >= 3:
            res.add((0,0,0))

        P = set(p)
        N = set(n)
        
        if z:
            for num in N:
                if -1 * num in P:
                    res.add((num,0,-1*num))

        
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if -1*(n[i]+n[j]) in P:
                    res.add(tuple(sorted([n[i],n[j],-1*(n[i]+n[j])])))      
 
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if -1*(p[i]+p[j]) in N:
                    res.add(tuple(sorted([p[i],p[j], -1*(p[i]+p[j])])))
        

  
        res = [list(x) for x in res]
        return res
\\\
    class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
\\\   