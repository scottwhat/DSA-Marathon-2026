# Section Summary — System Design & Practical Problems (Atlassian)

- Focus: common system-design flavored problems and applied DS&A patterns.

Review prompts:
- For each system problem (rate-limiter, job-scheduler), identify core data structures and tradeoffs.
- Practice: design a tagging system and LRU cache at high-level; note persistence and scaling considerations.

## Deep-dive prompts
- For each design: identify API, core data structures, and performance bottlenecks.
- Rate limiter: compare token bucket vs leaky bucket vs fixed window.
- Scheduler: what data structure backs “next job” selection and how do you handle retries?
- Caching: what makes LRU work; what’s the eviction mechanism?

## Mini quiz (no notes)
1) True/False: Fixed-window rate limiting can cause boundary bursts.
2) In an LRU cache, what operation must be O(1) and why?
3) What is idempotency and why does it matter for retries?
4) Name two metrics you’d monitor for a rate limiter.

## Operations & gotchas drill
- Rate limiter: compare fixed window, sliding window, token bucket—what’s the main gotcha for each?
- Time gotcha: clock skew and distributed systems—how does it affect rate limiting?
- Idempotency: define it and explain why retries require it.
- Data structures: for LRU, what operations must be O(1) and how do you achieve that?
- Scheduler: what happens if a worker crashes mid-job? What state transitions are needed?
- Consistency drill: what do you store (in-memory vs persistent) and why?
- Load drill: what metrics indicate backpressure is needed?

### Quick quiz
1) True/False: Using Redis automatically solves distributed locking issues.
2) In a token bucket, what does “burst” mean?
3) What’s the difference between at-least-once and exactly-once processing?
4) Name two ways to implement delayed jobs.
5) What’s a common pitfall of fixed-window rate limiting?
6) In an LRU cache, what do you update on every `get`?
