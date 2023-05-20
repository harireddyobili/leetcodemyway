class Solution:
    def numDecodings(self, s: str) -> int:
        store={}
        @lru_cache(None)   
        def decode(i):
            if(i==len(s)):
                return 1
            ways=0
            if int(s[i]) > 0: 
                ways=ways+decode(i+1)
            if(i<len(s)-1 and s[i]!='0'):
                if(int(s[i]+s[i+1])<=26):
                    ways=ways+decode(i+2)            
            return ways        
        return decode(0)