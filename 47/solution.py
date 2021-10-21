class Solution(object):

    def permuteUnique(self, num):
        res = []
        if len(num) == 0:
            return res
        self.permute(res, num, 0)
        return res

    def permute(self, res, num, index):
        if index == len(num):
            res.append(list(num))
            return
        appeared = set()
        for i in range(index, len(num)):
            if num[i] in appeared:
                continue
            appeared.add(num[i])
            num[i], num[index] = num[index], num[i]
            self.permute(res, num, index + 1)
            num[i], num[index] = num[index], num[i]

    def permuteUnique(self, num):
        # iterative solution
        res = [[]]
        for i in range(len(nums)):
            cache = set()
            while len(res[0]) == i:
                curr = res.pop(0)
                for j in range(len(curr) + 1):
                    # generate new n permutations from n -1 permutations
                    new_perm = curr[:j] + [nums[i]] + curr[j:]
                    stemp = ''.join(map(str, new_perm))
                    if stemp not in cache:
                        cache.add(stemp)
                        res.append(new_perm)
        return res
