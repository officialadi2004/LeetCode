
from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        size = m * n
        start = 0
        litter_bit = [0] * size
        reset = [False] * size
        total = 0

        for r in range(m):
            for c in range(n):
                p = r * n + c
                ch = classroom[r][c]

                if ch == 'S':
                    start = p
                elif ch == 'L':
                    litter_bit[p] = 1 << total
                    total += 1
                elif ch == 'R':
                    reset[p] = True

        if total == 0:
            return 0

        target = (1 << total) - 1

        # Precompute valid neighbors for each cell.
        neighbors = [[] for _ in range(size)]

        for r in range(m):
            for c in range(n):
                p = r * n + c
                if classroom[r][c] == 'X':
                    continue

                if r > 0 and classroom[r - 1][c] != 'X':
                    neighbors[p].append(p - n)
                if r + 1 < m and classroom[r + 1][c] != 'X':
                    neighbors[p].append(p + n)
                if c > 0 and classroom[r][c - 1] != 'X':
                    neighbors[p].append(p - 1)
                if c + 1 < n and classroom[r][c + 1] != 'X':
                    neighbors[p].append(p + 1)

        # best[pos][mask] = greatest energy reached with
        # this position and mask in an earlier or equal BFS layer.
        states = 1 << total
        best = [[-1] * states for _ in range(size)]
        best[start][0] = energy

        q = deque([(start, energy, 0)])
        moves = 0

        while q:
            for _ in range(len(q)):
                pos, rem, mask = q.popleft()

                if rem == 0:
                    continue

                new_rem = rem - 1

                for nxt in neighbors[pos]:
                    new_mask = mask | litter_bit[nxt]

                    if new_mask == target:
                        return moves + 1

                    if reset[nxt]:
                        nr = energy
                    else:
                        nr = new_rem

                    if best[nxt][new_mask] >= nr:
                        continue

                    best[nxt][new_mask] = nr
                    q.append((nxt, nr, new_mask))

            moves += 1

        return -1
