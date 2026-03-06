/*
  DSA JavaScript Loops + Iterators (Syntax Cheat-Sheet)

  Goal: quick copy/paste patterns you’ll use in DSA practice.
  Notes:
  - Prefer `for...of` for values, `for...in` for object keys (and array indices, but be careful).
  - When you need early-exit, use a plain loop (`for`, `for...of`, `while`) not `forEach`.
*/

// -------------------------
// Core loops
// -------------------------

// 1) Classic for-loop (index-based) — best when you need i, j pointers
for (let i = 0; i < 10; i++) {
  // ...
}

// Reverse
for (let i = 9; i >= 0; i--) {
  // ...
}

// Two pointers template
function twoPointers(arr) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    // decide which pointer to move
    // left++ or right--
  }
}

// 2) while-loop — good for pointer movement / unknown iterations
let x = 0;
while (x < 10) {
  x++;
}

// 3) do...while — runs at least once
let y = 0;
do {
  y++;
} while (y < 10);

// -------------------------
// Iterating arrays
// -------------------------

const nums = [1, 2, 3];

// 4) for...of — iterates values (works for arrays, strings, sets, maps)
for (const n of nums) {
  // n is value
}

// 5) for...in — iterates enumerable keys (for arrays: indices as strings)
for (const i in nums) {
  const idx = Number(i);
  const val = nums[idx];
  // careful: i is a string
}

// 6) forEach — callback per element (no break/continue/return to exit outer)
nums.forEach((n, i) => {
  // ...
});

// 7) entries()/keys()/values() — explicit iterators
for (const [i, n] of nums.entries()) {
  // i is index, n is value
}
for (const i of nums.keys()) {
  // i is index
}
for (const n of nums.values()) {
  // n is value
}

// -------------------------
// Iterating strings
// -------------------------

const s = "hello";

// Characters via for...of
for (const ch of s) {
  // ch is character
}

// Indices via classic for
for (let i = 0; i < s.length; i++) {
  const ch = s[i];
}

// -------------------------
// Iterating objects (plain {})
// -------------------------

const obj = { a: 1, b: 2 };

// for...in over keys
for (const key in obj) {
  const val = obj[key];
}

// Object.keys / values / entries
for (const key of Object.keys(obj)) {
  const val = obj[key];
}

for (const val of Object.values(obj)) {
  // val
}

for (const [key, val] of Object.entries(obj)) {
  // key, val
}

// -------------------------
// Map and Set iteration
// -------------------------

const set = new Set([1, 2, 3]);
for (const v of set) {
  // v
}

const map = new Map([
  ["a", 1],
  ["b", 2],
]);

for (const [k, v] of map) {
  // k, v
}

for (const k of map.keys()) {
  // k
}

for (const v of map.values()) {
  // v
}

for (const [k, v] of map.entries()) {
  // k, v
}

// -------------------------
// Common DSA helpers (minimal)
// -------------------------

// Frequency map for array or string
function freqMap(iterable) {
  const freq = new Map();
  for (const item of iterable) {
    freq.set(item, (freq.get(item) ?? 0) + 1);
  }
  return freq;
}

// Count chars (string) using plain object
function charCounts(str) {
  const counts = Object.create(null);
  for (const ch of str) {
    counts[ch] = (counts[ch] ?? 0) + 1;
  }
  return counts;
}

// Sliding window template
function slidingWindow(arr, k) {
  let left = 0;
  let windowValue = 0;

  for (let right = 0; right < arr.length; right++) {
    windowValue += arr[right];

    while (right - left + 1 > k) {
      windowValue -= arr[left];
      left++;
    }

    if (right - left + 1 === k) {
      // use windowValue
    }
  }
}

// Binary search template (sorted array)
function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }

  return -1;
}

// BFS template (adjacency list: { node: [neighbors...] })
function bfs(graph, start) {
  const queue = [start];
  const visited = new Set([start]);

  while (queue.length) {
    const node = queue.shift();

    for (const nei of graph[node] ?? []) {
      if (visited.has(nei)) continue;
      visited.add(nei);
      queue.push(nei);
    }
  }
}

// DFS template (iterative)
function dfs(graph, start) {
  const stack = [start];
  const visited = new Set([start]);

  while (stack.length) {
    const node = stack.pop();

    for (const nei of graph[node] ?? []) {
      if (visited.has(nei)) continue;
      visited.add(nei);
      stack.push(nei);
    }
  }
}
