from collections import defaultdict
from collections import deque

def course_schedule(n, prerequisites):
    """
    Args:
        n (int)
        prerequisites (List[List[int]])
    Returns:
        List[int]
    """
    # Write your code here.
    graph = defaultdict(list)
    indegree = [0] * n
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    queue = deque()
    for i, degree in enumerate(indegree):
        if degree==0:
            queue.append(i)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    for deg in indegree:
        if deg != 0:
            return [-1]
    return res