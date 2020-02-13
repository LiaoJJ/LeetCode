'''

When I first see this problem in LeetCode Weekly Contest, I have no idea how to solve this weird problem.

After seevral month, when I redo this problem, it's really not that hard, just a simple BFS problem

- 4 possible: right, down, clockwise, anti-clockwise
- 4 index to identify a position: (X_tail, Y_tail, X_head, Y_head)
- using BFS from (0,0,0,1) to (n-1, n-2, n-1, n-1)

'''