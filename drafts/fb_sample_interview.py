class Node(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

# # depth-first
# def _collect(node, data, depth=0):
#     if not node:  # base case
#         return None
    
#     if depth not in data:
#         data[depth] = []
    
#     data[depth].append(node.val)

#     _collect(node.left, data, depth+1)
#     _collect(node.right, data, depth+1)

# def avg_by_depth(node):
#     data = {}
#     _collect(node, data)

#     result = []
#     i = 0
#     while i in data:
#         nums = data[i]
#         avg = sum(nums) / len(nums)
#         result.append(avg)
#         i += 1

# store tuple instead of the whole list so the space complexity is O(nlogn)
def _collect(node, data, depth=0):
    if not node:  # base case
        return None
    
    if depth not in data:
        data[depth] = (node.val, 1)
    else:
        curr_sum, count = data[depth]
        curr_sum += node.val
        count += 1
        data[depth] = (curr_sum, count)

    _collect(node.left, data, depth+1)
    _collect(node.right, data, depth+1)

def avg_by_depth(node):
    data = {}
    _collect(node, data)

    result = []
    i = 0
    while i in data:
        curr_sum, count = data[i]
        result.append(curr_sum / count)
        i += 1
