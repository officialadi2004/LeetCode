from bisect import bisect_left
from fractions import gcd

class Solution(object):
    def findKthSmallest(self, coins, k):
        coins.sort()
        
        # 1. Remove coins that are multiples of smaller coins
        filtered = []
        for c in coins:
            for prev in filtered:
                if c % prev == 0:
                    break
            else:
                filtered.append(c)
                
        if filtered[0] == 1:
            return k
            
        # 2. Build positive (odd-sized) and negative (even-sized) subset LCMs
        pos_lcms = []
        neg_lcms = []
        period = 1
        
        for c in filtered:
            period = (period * c) // gcd(period, c)
            new_pos = [c]
            new_neg = []
            for p in pos_lcms:
                new_neg.append((p * c) // gcd(p, c))
            for n in neg_lcms:
                new_pos.append((n * c) // gcd(n, c))
            pos_lcms.extend(new_pos)
            neg_lcms.extend(new_neg)
            
        pos_lcms = tuple(pos_lcms)
        neg_lcms = tuple(neg_lcms)
        
        # 3. Reduce k by full LCM periods
        per_period = sum(period // d for d in pos_lcms) - sum(period // d for d in neg_lcms)
        q, rem = divmod(k - 1, per_period)
        target = rem + 1
        
        # 4. C-level bisect_left over [filtered[0], period]
        class CountSeq(object):
            def __getitem__(self, x):
                return sum(x // d for d in pos_lcms) - sum(x // d for d in neg_lcms)
                
        return q * period + bisect_left(CountSeq(), target, filtered[0], period)