# Section Summary — Advanced Graphs (Neetcode)

- Focus: multi-source BFS, MSTs, flow basics, shortest-path variants.

Review prompts:
- Differentiate Dijkstra, Bellman-Ford, and Floyd-Warshall use-cases.
- Practice: network delay, connect all points, reconstruct itinerary.

## Deep-dive prompts
- Dijkstra: what invariant does the priority queue guarantee when you pop?
- MST: compare Prim vs Kruskal and when union-find appears.
- Topological sort: what does it mean and what breaks it (cycles)?
- For shortest paths: compare Dijkstra vs Bellman-Ford.

## Mini quiz (no notes)
1) True/False: Dijkstra works with negative edge weights.
2) What is the key operation in union-find that makes it fast?
3) For topological sort, what does in-degree represent?
4) When would you prefer Bellman-Ford over Dijkstra?

## Operations & gotchas drill
- Dijkstra invariant: what is guaranteed when you pop from the heap?
- Negative weights: why Dijkstra fails and what you use instead.
- MST: compare Prim vs Kruskal and where union-find fits.
- Topological sort: what it produces and what a cycle implies.
- Priority queue gotcha: why you may need to ignore stale distances.
- Trick: multi-source BFS vs Dijkstra—when each applies.

### Quick quiz
1) True/False: Bellman-Ford can detect negative cycles.
2) What’s the difference between shortest path tree and MST?
3) In Kruskal, what’s the greedy choice?
4) What does in-degree represent in Kahn’s algorithm?
5) Why do we sometimes push multiple entries per node into the PQ?
6) When would you use Floyd-Warshall?
