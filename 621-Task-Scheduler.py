class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        \\\
        okay why is it actually hard??? i can never think this on my own for sure
        idea: whatever words have highest count goes first but there are constraints
        constraints: 
        - max heap to always get the highest word count
        - priority queue -> after poping from max heap put that word into priority queue(count,timestamp)
        - if its the time stamp push back to max heap
    
        \\\
        count = Counter(tasks)
        maxHeap = [-num for num in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        queue = deque()
        while maxHeap or queue:
            time +=1
            if maxHeap:
                num = 1 + heapq.heappop(maxHeap)
                if num:
                    queue.append([num,time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap,queue.popleft()[0])
                
        return time
                