#Print the nodes at odd levels of a tree
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None
	
def printOddNodes(root) :
        # Base Case
	if (root == None):
		return

	# Create an empty queue for level order traversal
	q = []

	# Enqueue root and initialize level as odd
	q.append(root)
	isOdd = True

	while (1) :
	
		# nodeCount (queue size) indicates number of nodes at current level.
		nodeCount = len(q)
		if (nodeCount == 0) :
			break

		# Dequeue all nodes of current level and Enqueue all nodes of next level
		while (nodeCount > 0):
		
			node = q[0]
			if (isOdd):
				print(node.data, end = " ")
			q.pop(0)
			if (node.left != None) :
				q.append(node.left)
			if (node.right != None) :
				q.append(node.right)
			nodeCount -= 1
			
		isOdd = not isOdd

# Driver Code
if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	printOddNodes(root)


