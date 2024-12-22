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

    def count_nodes_below(self, only_leaves=False):
        """
        Count the number of nodes in the subtree rooted at this node.

        Args:
            only_leaves: If True, count only leaf nodes. Otherwise, count all nodes.

        Returns:
            int: The number of nodes in the subtree.
        """
        if self.is_leaf:
            return 1 if only_leaves else 1
        count = 1
        if self.left_child:
            count += self.left_child.count_nodes_below(only_leaves)
        if self.right_child:
            count += self.rig
