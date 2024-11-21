class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.data})"

############################################
### Please do not alter the above class. ###
############################################

def count_failures(pred, t):
    if t is None:
        return 0 
    else:
        return ((not pred(t.data)) + count_failures(pred, t.left), count_failures(pred, t.right))

def tree_map(f, t):
    if t is None:
        return None
    else:
        return TreeNode(f(t.data), tree_map(f, t.left), tree_map(f, t.right))

def tree_apply(f, t):
    if t is None:
        return
    else:
        t.data = f(t.data)
        tree_apply(f, t.left)
        tree_apply(f, t.right)