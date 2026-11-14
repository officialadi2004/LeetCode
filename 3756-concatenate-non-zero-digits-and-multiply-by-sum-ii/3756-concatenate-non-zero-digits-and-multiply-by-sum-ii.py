class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 1000000007
        m = len(s)
        
        cnt = [0] * (m + 1)
        dig_sum = [0] * (m + 1)
        val = [0] * (m + 1)
        pow10 = [1] * (m + 1)
        
        c = 0
        ds = 0
        v = 0
        p = 1
        
        for i, ch in enumerate(s):
            d = ord(ch) - 48
            if d:
                c += 1
                ds += d
                v = (v * 10 + d) % MOD
            p = (p * 10) % MOD
            cnt[i + 1] = c
            dig_sum[i + 1] = ds
            val[i + 1] = v
            pow10[i + 1] = p
            
        ans = []
        append = ans.append
        for l, r in queries:
            r1 = r + 1
            k = cnt[r1] - cnt[l]
            if k == 0:
                append(0)
            else:
                x = (val[r1] - val[l] * pow10[k]) % MOD
                append((x * (dig_sum[r1] - dig_sum[l])) % MOD)
                
        return ans