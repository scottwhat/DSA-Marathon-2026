# Section Summary — Intervals (Neetcode)

- Focus: sorting by start/end, merging intervals, greedy selection.

Review prompts:
- Explain interval scheduling and meeting rooms problems.
- Practice: merge intervals, insert interval, minimum intervals to remove.

## Deep-dive prompts
- Explain why sorting by start time is the first step for merging intervals.
- For meeting rooms: what does a min-heap track and why?
- For interval scheduling: how does greedy by end-time work?

## Mini quiz (no notes)
1) True/False: If intervals are sorted by start, merging is one pass.
2) What heap value is stored for meeting rooms II?
3) What is the greedy criterion for selecting max non-overlapping intervals?
4) Name a common edge case for interval merging.

## Operations & gotchas drill
- Sorting gotcha: when merging, why do we sort by start then compare ends?
- Endpoint gotcha: inclusive vs exclusive endpoints; how does it change overlap condition?
- Meeting rooms II: what does the min-heap store and why is it correct?
- Greedy scheduling: why sorting by end time is the classic optimal choice.
- Trick: how do you treat equal start times (tie-breaker by end)?

### Quick quiz
1) True/False: Intervals can always be merged without sorting.
2) What’s the overlap condition if intervals are closed [a,b] and [c,d]?
3) In meeting rooms, what indicates you can reuse a room?
4) Why does sorting by end time help maximize number of non-overlapping intervals?
5) Name a tricky case involving touching endpoints.
