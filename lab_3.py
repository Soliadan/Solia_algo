from collections import deque

class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = self.right = None

def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None
    tree.left, tree.right = invert_binary_tree(tree.right), invert_binary_tree(tree.left)
    return tree

def bfs(tree: BinaryTree):
    if tree is None:
        return []

    result = []
    queue = deque([tree])  
    while queue:
        level_size = len(queue)  
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_values)
    
    return result

def print_tree_pyramid(tree: BinaryTree):
    levels = bfs(tree)
    for level in levels:
        print(" ".join(map(str, level)).center(len(levels[-1])*3))  
if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    
    print("Tree before inversion:")
    print_tree_pyramid(root)  
    
    inverted_root = invert_binary_tree(root)
    
    print("\nTree after inversion:")
    print_tree_pyramid(inverted_root)  
