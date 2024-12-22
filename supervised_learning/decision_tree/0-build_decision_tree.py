#!/usr/bin/env python3

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

    def max_depth_below(self):
        """
        Calculate the maximum depth of the subtree rooted at this node.

        Returns:
            int: The maximum depth of the subtree.
        """
        if self.is_leaf:
            return self.depth
        left_depth = self.left_child.max_depth_below() if self.left_child else self.depth
        right_depth = self.right_child.max_depth_below() if self.right_child else self.depth
        return max(left_depth, right_depth)

class Leaf(Node):
    def __init__(self, value, depth=None):
        """
        Initialize a leaf node in the decision tree.

        Args:
            value: The value of the leaf node (the prediction for this leaf).
            depth: The depth of the leaf node.
        """
        super().__init__(depth=depth)
        self.value = value
        self.is_leaf = True

    def max_depth_below(self):
        """
        The depth of a leaf node is simply its own depth.

        Returns:
            int: The depth of the leaf.
        """
        return self.depth

class Decision_Tree():
    def __init__(self, max_depth=10, min_pop=1, seed=0, split_criterion="random", root=None):
        """
        Initialize a decision tree.

        Args:
            max_depth: The maximum depth of the tree.
            min_pop: The minimum population size for each node.
            seed: The random seed for reproducibility.
            split_criterion: The criterion for splitting nodes.
            root: The root node of the tree (optional).
        """
        self.rng = np.random.default_rng(seed)
        self.root = root if root else Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """
        Get the maximum depth of the decision tree.

        Returns:
            int: The maximum depth of the tree.
        """
        return self.root.max_depth_below()
