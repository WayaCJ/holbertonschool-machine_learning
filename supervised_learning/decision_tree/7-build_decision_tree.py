import numpy as np

class Decision_Tree:
    def __init__(self, max_depth=10, min_pop=1, seed=0, split_criterion="random", root=None):
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def fit(self, explanatory, target, verbose=0):
        if self.split_criterion == "random":
            self.split_criterion = self.random_split_criterion
        else:
            self.split_criterion = self.Gini_split_criterion  # to be defined later

        self.explanatory = explanatory
        self.target = target
        self.root.sub_population = np.ones_like(self.target, dtype='bool')

        self.fit_node(self.root)

        self.update_predict()

        if verbose == 1:
            print(f"""Training finished.
- Depth                     : {self.depth()}
- Number of nodes           : {self.count_nodes()}
- Number of leaves          : {self.count_nodes(only_leaves=True)}
- Accuracy on training data : {self.accuracy(self.explanatory, self.target)}""")

    def np_extrema(self, arr):
        return np.min(arr), np.max(arr)

    def random_split_criterion(self, node):
        """
        Select a random feature and threshold to split the data.
        """
        diff = 0
        while diff == 0:
            feature = self.rng.integers(0, self.explanatory.shape[1])
            feature_min, feature_max = self.np_extrema(self.explanatory[:, feature][node.sub_population])
            diff = feature_max - feature_min

        x = self.rng.uniform()
        threshold = (1 - x) * feature_min + x * feature_max
        return feature, threshold

    def fit_node(self, node):
        """
        Recursively fit the tree by splitting nodes until stopping criteria are met.
        """
        node.feature, node.threshold = self.split_criterion(node)

        left_population = node.sub_population & (self.explanatory[:, node.feature] > node.threshold)
        right_population = node.sub_population & (self.explanatory[:, node.feature] <= node.threshold)

        # Check if the left child should be a leaf
        is_left_leaf = (np.sum(left_population) < self.min_pop) or (node.depth >= self.max_depth) or np.all(self.target[left_population] == self.target[left_population][0])

        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)

        # Check if the right child should be a leaf
        is_right_leaf = (np.sum(right_population) < self.min_pop) or (node.depth >= self.max_depth) or np.all(self.target[right_population] == self.target[right_population][0])

        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def get_leaf_child(self, node, sub_population):
        """
        Create a leaf node and assign the most common class as the value.
        """
        value = np.bincount(self.target[sub_population]).argmax()
        leaf_child = Leaf(value)
        leaf_child.depth = node.depth + 1
        leaf_child.sub_population = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """
        Create a child node and assign the sub-population.
        """
        n = Node()
        n.depth = node.depth + 1
        n.sub_population = sub_population
        return n

    def accuracy(self, test_explanatory, test_target):
        """
        Compute accuracy of the model on test data.
        """
        return np.sum(np.equal(self.predict(test_explanatory), test_target)) / test_target.size

# Additional necessary classes and methods (Node, Leaf, etc.) should be defined, as done in previous steps.
