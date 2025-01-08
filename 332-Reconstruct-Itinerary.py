class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_list = defaultdict(list)
        for src, destination in tickets:
            adj_list[src].append(destination)

        path = ['JFK']
        def dfs(cur_node):
            if len(path) == len(tickets) + 1:
                return True
            if cur_node not in adj_list:
                return False
            temp_list = list(adj_list[cur_node])
            for neighbor in temp_list:
                adj_list[cur_node].remove(neighbor)
                path.append(neighbor)
                if dfs(neighbor):
                    return True
                adj_list[cur_node].append(neighbor)
                path.pop()
            return False 
        dfs(\JFK\)
        return path
     

