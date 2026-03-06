"""Binary Tree + Binary Search Tree (BST) basics.

Run:
    python baseimplementations/binary_tree_bst.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generator, Optional


@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


def inorder(root: Optional[TreeNode]) -> Generator[int, None, None]:
    if root is None:
        return
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)


def preorder(root: Optional[TreeNode]) -> Generator[int, None, None]:
    if root is None:
        return
    yield root.val
    yield from preorder(root.left)
    yield from preorder(root.right)


def postorder(root: Optional[TreeNode]) -> Generator[int, None, None]:
    if root is None:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root.val


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(val)
            return

        curr = self.root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    return
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    return
                curr = curr.right
            else:
                return  # ignore duplicates

    def contains(self, val: int) -> bool:
        curr = self.root
        while curr is not None:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return True
        return False


def _test_binary_tree_bst() -> None:
    bst = BinarySearchTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)

    assert bst.contains(6)
    assert not bst.contains(10)

    assert list(inorder(bst.root)) == [2, 3, 4, 5, 6, 7, 8]
    assert list(preorder(bst.root))[:3] == [5, 3, 2]
    assert list(postorder(bst.root))[-3:] == [6, 8, 7]


if __name__ == "__main__":
    _test_binary_tree_bst()
    print("binary_tree_bst.py: OK")
