# Section Summary — Graphs

- Core concepts: adjacency list vs matrix, BFS vs DFS, directed vs undirected graphs, visited state.
- Key algorithms: BFS shortest unweighted path, Dijkstra for weighted graphs, Bellman-Ford, Union-Find for connectivity, topological sort for DAGs.
- Complexity: nodes vs edges (O(V+E)). Sketch common traversals and edge relaxations.

Review prompts:
- When to use BFS vs DFS vs Dijkstra? Provide problem examples.
- Explain union-find with path compression and union by rank.
- Practice: detect cycles, connected components, shortest path variants, topological order.

## Deep-dive prompts
- Compare adjacency list vs matrix; when would you pick each?
- Explain BFS for shortest path in an unweighted graph.
- Explain DFS use-cases: components, cycle detection, topological foundations.
- For grid graphs, define how you encode state and visited.

## Mini quiz (no notes)
1) What is the time complexity of BFS/DFS in terms of V and E?
2) True/False: BFS always finds the shortest path (in number of edges).
3) For number of islands, what defines a node and an edge?
4) When do you need multi-source BFS?

## Operations & gotchas drill
- Representations: adjacency list vs matrix — memory and access tradeoffs.
- Visited gotcha: why do you mark visited when enqueuing in BFS (not when dequeuing)?
- BFS vs DFS: pick one for shortest paths and explain why.
- Directed graph gotcha: what changes in cycle detection vs undirected?
- Grid graphs: what constitutes a node, what are neighbors, and how do you encode coordinates?
- Multi-source BFS: when it’s needed and what the initial queue looks like.
- Union-find: what do path compression and union by rank do?

### Quick quiz
1) True/False: BFS is optimal for weighted graphs.
2) What is the complexity of BFS/DFS in terms of V and E?
3) In course schedule, what does an edge mean semantically?
4) Why do we need a recursion stack / coloring method for directed cycle detection?
5) When is union-find a better fit than BFS/DFS?
6) What’s a common bug when using BFS levels (distance counting)?
