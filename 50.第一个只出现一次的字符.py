class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dicts = {}
        ltor = []
        for i in s:
            # print(i)
            if i not in dicts.keys():
                print(i)
                dicts[i] = 1
                ltor.append(i)
            else:
                num = dicts[i]
                dicts[i] = num + 1

        print(dicts)
        index = -1
        for x, y in dicts.items():
            if y == 1:
                flag = s.index(x)
                print(flag)
                if index < 0 or flag < index:
                    index = flag
        return index
        return s[index]