# Here's how I solved it..

# If q = 4, the tree looks like this...

# LEVEL 4    #           15
             #         /     \
             #        /       \
             #       /         \
# LEVEL 3    #      7          14 
             #    /   \       /   \
# LEVEL 2    #   3     6     10   13
             #  / \   / \   / \   / \ 
# LEVEL 1    # 1   2 4   5 8   9 11 12

# Stare long enough and you'll notice some patterns:
# 1. Children are less than their parents
# 2. Left-children are less than their sibling (right-children)
# 3. Every RIGHT child = parent-1
# 4. Every LEFT child = parent-2**child_level

# When searching for child C...
# Start with root
# Calculate the left-child and right-child
#
# If C <= left-child, C is a sub-child of left-child...
# move a level down and calculate left-child's children, repeat
#
# If C > left-child, C is NOT sub-child of left-child, thus a sub-child of right-child...
# move a level down and calculate right-child's children, repeat

def answer(h,q):

    # Search for child, starting at parent...
    def search(parent,child,level):
        right = parent-1 # Calculate RIGHT child
        left = parent-2**level # Calculate LEFT child
        level -= 1 # Increment level
    
        # If child found, return parent
        if right == child or left == child:
            return parent
        # Otherwise search a level deeper
        else:
            if child <= left:
                return search(left,child,level)
            else:
                return search(right,child,level)

    root = (2**h)-1
    parents = []
    for converter in q:
        # If converter is root, parent is -1
        if converter == root: 
            parent = -1
        # Otherwise search for converter parent
        else: 
            parent = search(root,converter,h-1)
        parents.append(parent)

    return parents


print answer(3,[1,4,7]) 
print(answer(5, [19,14,28]))
