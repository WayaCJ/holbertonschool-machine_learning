import numpy as np
Node = __import__('8-build_decision_tree').Node
Leaf = __import__('8-build_decision_tree').Leaf

class Isolation_Random_Tree:
    def __init__(self, max_depth=10, seed=0, root=None):
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.max_depth = max_depth
        self.predict = None
        self.min_pop = 1

    def __str__(self):
        # String representation for the tree, useful for debugging
        return f"Isolation_Random_Tree with max_depth={self.max_depth}"

    def depth(self):
        # Depth of the tree (max depth from root to leaf)
        return self._depth(self.root)

    def _depth(self, node):
        if isinstance(node, Leaf):
            return node.depth
        else:
            return max(self._depth(node.left_child), self._depth(node.right_child)) + 1

    def count_nodes(self, only_leaves=False):
        # Count nodes (or leaves if only_leaves is True)
        return self._count_nodes(self.root, only_leaves)

    def _count_nodes(self, node, only_leaves=False):
        if isinstance(node, Leaf):
            return 1 if only_leaves else 1
        else:
            left_count = self._count_nodes(node.left_child, only_leaves)
            right_count = self._count_nodes(node.right_child, only_leaves)
            return left_count + right_count

    def update_bounds(self):
        # Update bounds of the tree (useful for decision boundaries)
        pass  # No specific implementation needed for outlier detection task

    def get_leaves(self):
        # Get all leaves in the tree
        leaves = []
        self._get_leaves(self.root, leaves)
        return leaves

    def _get_leaves(self, node, leaves):
        if isinstance(node, Leaf):
            leaves.append(node)
        else:
            self._get_leaves(node.left_child, leaves)
            self._get_leaves(node.right_child, leaves)

    def update_predict(self):
        # Create the prediction function that returns the depth of the leaf each individual falls into
        self.predict = lambda A: np.array([self._predict_one(a) for a in A])

    def _predict_one(self, x):
        # Predict the depth for a single individual
        return self._predict_depth(self.root, x)

    def _predict_depth(self, node, x):
        if isinstance(node, Leaf):
            return node.depth
        else:
            if x[node.feature] > node.threshold:
                return self._predict_depth(node.left_child, x)
            else:
                return self._predict_depth(node.right_child, x)

    def np_extrema(self, arr):
        # Helper function to find min and max of an array
        return np.min(arr), np.max(arr)

    def random_split_criterion(self, node):
        # Randomly select a feature and a threshold for splitting
        diff = 0
        while diff == 0:
            feature = self.rng.integers(0, self.explanatory.shape[1])
            feature_min, feature_max = self.np_extrema(self.explanatory[:, feature][node.sub_population])
            diff = feature_max - feature_min
        x = self.rng.uniform()
        threshold = (1 - x) * feature_min + x * feature_max
        return feature, threshold

    def get_leaf_child(self, node, sub_population):
        # Create a leaf node with depth information
        value = None  # No value as we are not using class labels for outlier detection
        leaf_child = Leaf(value)
        leaf_child.depth = node.depth + 1
        leaf_child.subpopulation = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        # Create a new internal node
        n = Node()
        n.depth = node.depth + 1
        n.sub_population = sub_population
        return n

    def fit_node(self, node):
        # Recursively fit the tree until max depth is reached
        if node.depth == self.max_depth:
            return

        node.feature, node.threshold = self.random_split_criterion(node)

        left_population = node.sub_population & (self.explanatory[:, node.feature] > node.threshold)
        right_population = node.sub_population & (self.explanatory[:, node.feature] <= node.threshold)

        # Is left node a leaf?
        is_left_leaf = np.sum(left_population) <= self.min_pop

        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)

        # Is right node a leaf?
        is_right_leaf = np.sum(right_population) <= self.min_pop

        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def fit(self, explanatory, verbose=0):
        # Train the Isolation Random Tree
        self.explanatory = explanatory
        self.root.sub_population = np.ones(explanatory.shape[0], dtype='bool')

        self.fit_node(self.root)
        self.update_predict()

        if verbose == 1:
            print(f"""Training finished.
- Depth                     : {self.depth()}
- Number of nodes           : {self.count_nodes()}
- Number of leaves          : {self.count_nodes(only_leaves=True)}""")
