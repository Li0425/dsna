class Node(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def _collect(node, data, depth=0):
    if node is None:
        return None
    
    if depth not in data:
        data[depth] = (1, node.val)
    else:
        num_count, curr_sum = data[depth]
        data[depth] = (num_count + 1, curr_sum + node.val)

    _collect(node, data.left, depth+1)
    _collect(node, data.right, depth+1)

def get_avg_by_depth(node):
    result = []

    data = {}
    _collect(node, data)

    i = 0
    while i in data:
        num_count, curr_sum = data[i]
        avg = curr_sum / num_count
        result.append(avg)
        i += 1

    return result