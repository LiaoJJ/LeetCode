class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        c = collections.defaultdict(list)
        res = []
        for string in strings:
            key = []
            for i in range(1, len(string)):
                dif = ord(string[i]) - ord(string[i-1])
                dif = dif+26 if dif<0 else dif
                key.append(dif)
            c[tuple(key)].append(string)
        # print(c)
        return [val for val in c.values()]