#  https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, dig: str) -> List[str]:
        def combination(pre, dic, d):
            arr = []
            for i in pre:
                for j in dic[d]:
                    arr.append(i + j)
            print(arr)
            return arr
        
        if dig == "":
            return []
        
        dic = {'1':[''], '2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'0':[' ']}
        
        res = [""]
        for i in dig:
            res = combination(res, dic, i)
        return res
