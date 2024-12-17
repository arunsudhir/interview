from collections import deque
# Have fun coding in Python!
def canComplete(numCourses, preRequisites):
    indegree = [0] * numCourses
    adj_list = [ [] for i in range(numCourses)]
    print(indegree)
    #form thr degrees of dependency
    # also form an adjacency list for the graph
    for src,dst in preRequisites:
        indegree[dst] += 1
        adj_list[src].append(dst)
    # populate a queue with the courses
    # that have no deps    
    q = deque()    
    for n in range(numCourses):
        if indegree[n] == 0:
            q.append(n)
    while q:
        node = q.popleft()
        for neighbour in adj_list[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                q.append(neighbour)
    return sum(indegree) == 0                    
                
print(canComplete(5,[(0,1),(1,2),(2,3),(0,3),(2,4)]))
