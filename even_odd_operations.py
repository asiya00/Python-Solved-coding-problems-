class node:
    def __init__(self, val, level):
        self.val = val
        self.level = level
        self.left = None
        self.right = None

def solve (X, Y):
    visit = set()
    q = []
    n = node(X, 0)
    q.append(n) 
    while q:
        t = q.pop(0)
        if t.val == Y:
            return t.level
        
        visit.add(t.val)

        if t.val % 2:
            if t.val * 2 == Y or 3 * t.val + 1 == Y:
                return t.level+1
        else:
            if t.val * 2 == Y or t.val // 2 == Y:
                return t.level+1

        if t.val % 2:
            if t.val * 2 not in visit:
                t.left = node(t.val*2, t.level+1)
                q.append(t.left)
            if 3 * t.val + 1 not in visit:
                t.right = node(3 * t.val + 1, t.level+1)
                q.append(t.right)
        if not t.val % 2:
            if t.val * 2 not in visit:
                t.left = node(t.val*2, t.level+1)
                q.append(t.left)
            if t.val//2 not in visit:
                t.right = node(t.val//2, t.level+1)
                q.append(t.right)

X, Y = map(int, input().split())
out_ = solve(X, Y)
print(out_)