class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}

        if len(strs) == 1:
            return [[strs[0]]]
        if not strs:
            return [[""]]

        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in mydict:
                mydict[sorted_str].append(strs[i])
            else:
                mydict[sorted_str] = []
                mydict[sorted_str].append(strs[i])

        ans = []
        for val in mydict.values():
            ans.append(val)

        return ans


    

        