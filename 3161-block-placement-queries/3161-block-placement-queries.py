class Solution:
    def getResults(self, queries):
        coords = sorted({0} | {q[1] for q in queries})
        m = len(coords)
        idx = {x: i for i, x in enumerate(coords)}

        # Fenwick tree: tracks active obstacle positions.
        bit = [0] * (m + 1)

        def add(i, v):
            i += 1
            while i <= m:
                bit[i] += v
                i += i & -i

        def summ(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def kth(k):
            i = 0
            step = 1 << (m.bit_length() - 1)
            while step:
                j = i + step
                if j <= m and bit[j] < k:
                    i = j
                    k -= bit[j]
                step >>= 1
            return i

        # Segment tree: maximum gap ending at each obstacle.
        size = 1
        while size < m:
            size <<= 1
        seg = [0] * (2 * size)

        def update(p, v):
            p += size
            seg[p] = v
            p >>= 1
            while p:
                seg[p] = max(seg[p << 1], seg[p << 1 | 1])
                p >>= 1

        def query(r):
            l = size
            r += size
            res = 0
            while l < r:
                if l & 1:
                    res = max(res, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, seg[r])
                l >>= 1
                r >>= 1
            return res

        add(idx[0], 1)
        obstacles = [0]
        ans = []

        for q in queries:
            x = q[1]
            ix = idx[x]

            if q[0] == 1:
                count = summ(ix)
                p = kth(count)
                prev = coords[p]

                total = summ(m)
                if count < total:
                    nxt = coords[kth(count + 1)]
                    update(idx[nxt], nxt - x)

                update(ix, x - prev)
                add(ix, 1)

            else:
                sz = q[2]
                count = summ(ix + 1)
                p = kth(count)
                prev = coords[p]

                ans.append(
                    query(ix + 1) >= sz or x - prev >= sz
                )

        return ans