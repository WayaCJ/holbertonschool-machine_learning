import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left_child=None, right_child=None, is_root=False, depth=0):
        """
        Initialize a node in the decision tree.

        Args:
            feature: The feature to split on (optional).
            threshold: The threshold value for splitting (optional).
            left_child: Left child node (optional).
            right_child: Right child node (optional).
            is_root: Boolean indicating if this is the root node (optional).
            depth: The depth of the node in the tree (optional).
        """
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

    def update_indicator(self):
        """
        Update the indicator function based on the current node's lower and upper bounds.
        The indicator function will check if each individual's features are within the node's bounds.
        """
        def is_large_enough(x):
            """
            Check if each individual's feature values are greater than the corresponding lower bounds.
            """
            return np.all(np.array([np.greater(x[:, key], self.lower[key]) for key in self.lower.keys()]), axis=0)

        def is_small_enough(x):
            """
            Check if each individual's feature values are less than or equal to the corresponding upper bounds.
            """
            return np.all(np.array([np.less_equal(x[:, key], self.upper[key]) for key in self.upper.keys()]), axis=0)

        # Define the indicator function using the conditions from is_large_enough and is_small_enough
        self.indicator = lambda x: np.all(np.array([is_large_enough(x), is_small_enough(x)]), axis=0)

