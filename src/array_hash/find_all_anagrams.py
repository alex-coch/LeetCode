from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # time O(n), space O(1)
        out=list()
        s_counter, p_counter=Counter(s[:len(p)-1]), Counter(p)
        for i in range(len(p)-1,len(s)):
            s_counter[s[i]]+=1
            if s_counter==p_counter: out.append(i-len(p)+1)
            s_counter[s[i-len(p)+1]]-=1
            if s_counter[s[i-len(p)+1]]==0: del s_counter[s[i-len(p)+1]]
        return out

