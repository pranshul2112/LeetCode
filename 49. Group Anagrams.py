#  https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {'a': 2,
                 'b': 3,
                 'c': 5,
                 'd': 7,
                 'e': 11,
                 'f': 13,
                 'g': 17,
                 'h': 19,
                 'i': 23,
                 'j': 29,
                 'k': 31,
                 'l': 37,
                 'm': 41,
                 'n': 43,
                 'o': 47,
                 'p': 53,
                 'q': 59,
                 'r': 61,
                 's': 67,
                 't': 71,
                 'u': 73,
                 'v': 79,
                 'w': 83,
                 'x': 89,
                 'y': 97,
                 'z': 101
                 }

        one = {}

        for i in strs:
            p = 1

            for c in i:
                p = check[c] * p

            if p in one.keys():
                lst = one[p]
                lst.append(i)
                one[p] = lst
            else:
                one[p] = [i]

        res = []

        for val in one.keys():
            res.append(one[val])

        return res
