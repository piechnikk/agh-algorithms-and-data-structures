# We have a given set of tasks T = {t1, . . . , tn}. 
# Each task ti additionally has: 
#   a. a deadline d(ti) (a natural number) and 
#   b. a profit p(ti) for finishing on time (a natural number). 
# Each task takes a unit of time to complete. 
# If task ti is completed before its deadline d(ti) we get a reward p(ti) for it 
# (the first selected task is completed at time 0, the second selected task at time 1, the third at time 2, etc.). 
# Please provide an algorithm that finds a subset of tasks that can be completed in time and that leads to maximum profit. 

# T = [(deadline, profit), ....]

def select_optimal_tasks(T:list):
    max_time = max(T)[0]
    done = []
    for time in range(max_time, -1, -1):
        # if there are no more tasks, terminate the algorithm
        if len(T) == 0:
            break
        # gives list of tasks that have a deadline now or later than the time considered now
        possible_tasks = list(filter(lambda x: x[1][0]>=time, enumerate(T)))
        # if there are no tasks with that deadline
        if len(possible_tasks) == 0:
            continue
        # take the most profitable task add it to done array and remove it from T array
        i, best = max(possible_tasks, key=lambda x: x[1][1])
        done.append(best)
        T.pop(i)
    return done

print(select_optimal_tasks([(0,1),(1,2),(2,3),(2,2),(4,3),(4,3)]))