# merging line segments
# there is an array of line segments named S
# two line segments can be merger together if they have exactly one point of intersection (when they are touching each other in one point)

# a. is it possible to obtain a line segment [a,b] by merging some line segments together
def does_path_exist(S, a, b):
    G = [[] for _ in range(max(max(S, key=lambda x:x[0])[0], max(S, key=lambda x:x[1])[1])+1)]
    for el in S:
        G[el[0]].append(el[1])
    
    visited = [False] * len(G)
    queue = []

    visited[a] = True
    queue.append(a)
    while len(queue) > 0:
        actual = queue.pop()
        for neighbour in G[actual]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

        if visited[b]:
            return True
        
    return False

print(does_path_exist([[1,3],[1,2],[2,3],[3,5]],1,5))

# b. as above, but by merging together at most k line segments
def does_shorter_than_k_path_exist(S, a, b, k):
    G = [[] for _ in range(max(max(S, key=lambda x:x[0])[0], max(S, key=lambda x:x[1])[1])+1)]
    for el in S:
        G[el[0]].append(el[1])
    
    n = len(G)
    visited = [False] * n
    distance = [float("inf")] * n
    queue = []

    distance[a] = 0
    visited[a] = True
    queue.append(a)
    while len(queue) > 0:
        actual = queue.pop()
        for neighbour in G[actual]:
            if not visited[neighbour]:
                distance[neighbour] = distance[actual] + 1
                visited[neighbour] = True
                queue.append(neighbour)

        if visited[b]:
            return distance[b]<=k
        
    return False

print(does_shorter_than_k_path_exist([[1,3],[1,2],[2,3],[3,5]],1,5,1))

# c. as above, but each line segment has a positive price and we minimise the sum of the prices of the line segments used
from queue import PriorityQueue
def shorter_than_k_path_cost(S, a, b):
    G = [[] for _ in range(max(max(S, key=lambda x:x[0])[0], max(S, key=lambda x:x[1])[1])+1)]
    for el in S:
        G[el[0]].append((el[1], el[2]))

    distance = [float("inf")] * len(G)
    queue = PriorityQueue()

    queue.put((0, a))

    while not queue.empty():
        predicted_distance, actual = queue.get()
        if distance[actual] == float("inf"):
            distance[actual] = predicted_distance
            for neighbour, n_distance in G[actual]:
                if distance[neighbour] == float("inf"):
                    queue.put((distance[actual] + n_distance, neighbour))
            if actual == b:
                return distance[b]
    return distance[b]

print(shorter_than_k_path_cost([[1,3,5],[1,2,1],[2,3,1],[3,5,2]],1,5))

# d. what is the longest line segment we can obtain by gluing together at most k line segments
def longest_line_segment(S, k):
    G = [[] for _ in range(max(max(S, key=lambda x:x[0])[0], max(S, key=lambda x:x[1])[1])+1)]
    for el in S:
        G[el[0]].append(el[1])
    
    n = len(G)
    
    def max_distance_for_lower_than_k_segments_from_point_s(G, k, s):
        visited = [False] * n
        distance = [float("inf")] * n
        queue = []

        distance[s] = 0
        visited[s] = True
        queue.append(s)
        while len(queue) > 0:
            actual = queue.pop()
            for neighbour in G[actual]:
                if not visited[neighbour]:
                    distance[neighbour] = distance[actual] + 1
                    visited[neighbour] = True
                    queue.append(neighbour)

        i = n-1
        while i>s:
            if distance[i]<=k:
                return i-s
            i-=1
        
        return -float("inf")
    
    return max(max_distance_for_lower_than_k_segments_from_point_s(G, k, s) for s in range(n-1))

print(longest_line_segment([[1,3],[1,2],[7,18],[2,3],[3,5]],2))