from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Create adjacency list for reverse graph
        adj_list = defaultdict(list)
        for i, neigh in enumerate(graph):
            for node in neigh:
                adj_list[node].append(i)

        # Track the number of outgoing edges (parents)
        parents = [len(neigh) for neigh in graph]

        # Initialize queue with nodes having no outgoing edges
        q = deque([i for i in range(len(parents)) if parents[i] == 0])

        # Process the queue
        while q:
            node = q.popleft()
            for parent in adj_list[node]:
                parents[parent] -= 1
                if parents[parent] == 0:  # Push only when no outgoing edges remain
                    q.append(parent)

        # Collect nodes with no outgoing edges
        res = [i for i in range(len(parents)) if parents[i] == 0]
        return sorted(res)  # Return in sorted order
