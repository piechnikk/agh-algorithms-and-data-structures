# it creates n buckets and goes through the table A and element A[i] put in the buckets[floor(n*A[i]), each bucket it sorts by simple sorting 
# for evenly distributed data it will be O(n) complexity
def bucketsort(A):
    n = len(A)
    bucket_range = max(a) / n - 1
    buckets = [[] for i in range(n)]
    for i in range(n):
        bucket_i = int(A[i] / bucket_range)
        buckets[bucket_i] = A[i]
    for i in range(n):
        
