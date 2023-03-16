# We are given an array that contains various elements (natural numbers) we are looking for the leader of the sequence (an element that occurs more than half of the cases) [1,2,3,2,5,2,2,3,2,2,2,5,7,2] (in that case it is "2")
def find_leader(T):
    n = len(T)
    actual_leader = T[0]
    leader_counter = 1
    for i in range(1, n):
        if T[i] == actual_leader:
            leader_counter += 1
        else:
            leader_counter -= 1
        if leader_counter < 0:
            actual_leader = T[i]
            leader_counter = 1
    counter = 0
    for i in T:
        if actual_leader == i:
            counter += 1

    if counter > n // 2:
        return actual_leader
    else:
        return False


print(find_leader([1, 2, 3, 2, 5, 2, 2, 3, 2, 2, 2, 5, 7, 2]))
