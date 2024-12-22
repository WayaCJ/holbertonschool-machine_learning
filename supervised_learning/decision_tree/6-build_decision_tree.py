import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left_child=None, right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth
        self.lower = None  # To store lower bounds of the node
        self.upper = None  # To store upper bounds of the node
        self.indicator = None  # To store the indicator function

    def pred(self, x):
        """
        Predict the value for a single instance x.
        """
        if x[self.feature] > self.threshold:
            return self.left_child.pred(x)
        else:
            return self.right_child.pred(x)

    def update_indicator(self):
        """
        Update the indicator function based on the current node's lower and upper bounds.
        """
        def is_large_enough(x):
            return np.all(np.array([np.greater(x[:, key], self.lower[key]) for key in self.lower.keys()]), axis=0)

        def is_small_enough(x):
            return np.all(np.array([np.less_equal(x[:, key], self.upper[key]) for key in self.upper.keys()]), axis=0)

        self.indicator = lambda x: np.all(np.array([is_large_enough(x), is_small_enough(x)]), axis=0)


class Leaf(Node):
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def pred(self, x):
        """
        Predict the value for a single instance x at a leaf.
        """
        return self.value


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

    def update_bounds(self):
        """
        Update the bounds of the entire decision tree.
        """
        self.root.update_bounds_below()

    def update_predict(self):
        """
        Update the prediction function of the decision tree.
        """
        self.update_bounds()  # First, update the bounds
        leaves = self.get_leaves()  # Get all leaves of the tree
        for leaf in leaves:
            leaf.update_indicator()  # Update the indicator for each leaf

        # Define the prediction function using the indicator of each leaf
        self.predict = lambda A: np.array([leaf.pred(x) for x in A if leaf.indicator(x)] for leaf in leaves)

    def get_leaves(self):
        """
        Get all the leaves of the tree.
        """
        return self.root.get_leaves_below()

    def pred(self, x):
        """
        Predict the value for a single instance x.
        """
        return self.root.pred(x)
