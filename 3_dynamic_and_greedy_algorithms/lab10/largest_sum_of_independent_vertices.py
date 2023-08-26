# the corporate event problem
# each employee is at some level in the hierarchy tree depending on whose supervisor he/she is
# each employee has a party index (the higher, the better the party with him/her is)
# an employee and his/her immediate superior must not be present in order for the party to be successful
# we need to find a list of employees with whom it is best to party

# the set of independent vertices in the graph with the largest sum
# we want to take vertices with maximal sum such that no two vertices are connected by an edge

employees = [
    {"subordinates": [1,2,3], "fun": 50},
    {"subordinates": [4,5,6], "fun": 10},
    {"subordinates": [7,8], "fun": 20},
    {"subordinates": [9,10], "fun": 1},
    {"subordinates": [11,12,13], "fun": 18},
    {"subordinates": [], "fun": 5},
    {"subordinates": [], "fun": 23},
    {"subordinates": [14,15,16], "fun": 21},
    {"subordinates": [], "fun": 17},
    {"subordinates": [17,18], "fun": 1},
    {"subordinates": [19], "fun": 2},
    {"subordinates": [], "fun": 25},
    {"subordinates": [], "fun": 36},
    {"subordinates": [20,21,22], "fun": 7},
    {"subordinates": [], "fun": 18},
    {"subordinates": [], "fun": 1},
    {"subordinates": [], "fun": 5},
    {"subordinates": [], "fun": 1},
    {"subordinates": [], "fun": 1},
    {"subordinates": [], "fun": 1},
    {"subordinates": [], "fun": 100},
    {"subordinates": [], "fun": 100},
    {"subordinates": [], "fun": 100},
]

def max_fun(employees):
    n = len(employees)
    F = [None] * n
    G = [None] * n
    def f(i):
        if F[i]:
            return F[i]
        
        f_sum = 0
        for j in range(len(employees[i]["subordinates"])):
            f_sum += g(employees[i]["subordinates"][j])
        F[i] = max(g(i), f_sum + employees[i]["fun"])
        return F[i]

    def g(i):
        if G[i]:
            return G[i]
        
        g_sum = 0
        for j in range(len(employees[i]["subordinates"])):
            g_sum += f(employees[i]["subordinates"][j])
        G[i] = g_sum
        return G[i]
    return f(0)

print(max_fun(employees))