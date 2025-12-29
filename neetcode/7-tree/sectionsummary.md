# Section Summary — Trees (Neetcode)

- Focus: traversal templates (DFS recursion and BFS queue), BST invariants.

Review prompts:
- When choose BFS vs DFS for a tree problem?
- Practice: validate BST, serialize/deserialize, tree diameter.

## Deep-dive prompts
- Write the 3 DFS orders and what each is good for.
- Explain BFS level-order and how you track levels.
- For BST: define the invariant and how validation differs from local-child checks.
- For path problems: compare “root-to-leaf” vs “any path” and how state changes.

## Mini quiz (no notes)
1) True/False: Inorder traversal of a BST yields a sorted sequence.
2) What data structure do you use for BFS and why?
3) In recursion, what is the base case for an empty tree?
4) For LCA in a BST, how do you decide to go left vs right?

## Operations & gotchas drill
- Traversals: write the iterative templates for DFS (stack) and BFS (queue) in words.
- BST gotcha: why checking only `node.left < node < node.right` is insufficient.
- Recursion state: what do you pass down (min/max bounds, path sum, depth) and why?
- Path problems: distinguish root-to-leaf vs any-path and how it changes the algorithm.
- Serialization: what’s the minimal info needed to reconstruct a tree?
- Complexity drill: what is the worst-case height of a BST and why does it matter?
- Trick: how do you do level-order with per-level separation (two loops vs sentinel)?

### Quick quiz
1) True/False: Inorder traversal of a BST is sorted.
2) What makes BFS the natural choice for “shortest path in edges” on a tree?
3) What’s the base case for recursion on a null node?
4) In validating BST, what bounds do you carry?
5) Name a tree problem where postorder is the cleanest approach.
6) What’s the difference between diameter and max path sum?
