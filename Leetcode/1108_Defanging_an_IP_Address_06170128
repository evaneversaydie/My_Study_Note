class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans =address.split('.')
        a =''
        for i in range(len(ans)):
            a+=ans[i]+'[.]'
        return a[:-3]