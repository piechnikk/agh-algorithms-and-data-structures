# There is a set of points X = {x1,...,xn} on a straight line. 
# Please give an algorithm that finds the minimum number of closed unit compartments needed to cover all points from X. 
# (Example: If X = {0.25, 0.5, 1.6} then two compartments are needed, e.g. [0.2,1.2] and [1.4,2.4]).

def coverage_with_unit_compartments(X):
    X.sort()
    compartments = []
    compartments.append([X[0], X[0] + 1])
    for point in X:
        if point > compartments[len(compartments)-1][1]:
            compartments.append([point, point+1])
    return compartments

print(coverage_with_unit_compartments([0.25, 0.5, 1.6]))