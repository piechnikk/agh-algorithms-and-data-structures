# find a subset of items whose total weight does not exceed W and whose total price is the maximum
# f(i, w) - returns the maximum total price from the set {0,...,i} whose total weight of elements does not exceed w
# f(0, w) = 0 no
# f(i, 0) = 0

class Item:
    def __init__(self, weight, price):
        self.w = weight
        self.p = price

def knapsack(items, W):
    n = len(items)
    answers = [[None] * (W+1) for _ in range(n)]

    def f(i,w):
        print(items[i].w, items[i].p, i, w)
        if i==0:
            if w >= items[i].w:
                answers[i][w] = items[i].p
                return answers[i][w]
            return 0
        if w >= items[i].w:
            answers[i][w] = max(f(i-1, w-items[i].w) + items[i].p, f(i-1, w))
            return answers[i][w]
        
    return f(n-1, W)

items = [Item(3,3), Item(2,3), Item(2,2)]
print(knapsack(items, 5))