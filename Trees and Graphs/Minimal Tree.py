def minimal_tree(sorted_list):
	length = len(sorted_list)
	if length == 0:
        return None

	root = Node(sorted_list[length//2])

	root.left = minimal_tree(sorted_list[0: length//2])
	root.right = minimal_tree(sorted_list[length//2:length-1])

	return root
