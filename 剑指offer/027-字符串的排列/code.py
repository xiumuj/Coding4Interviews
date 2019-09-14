
def helper(s):
    if len(s) == 1:
        return s[0]
    res = []
    for i in range(len(s)):
        l = helper(s[:i] + s[i+1:])
        for j in l:
            res.append(s[i] + j)

    return res

def Permutation(ss):
    # write code here
    if not ss: return []
    words = list(ss)
    return list(sorted(set(helper(words))))

print(Permutation('aa'))




class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in (self.Permutation(ss[: i] + ss[i+1 :])):
                res.add(ss[i] + j)
        return sorted(res)
