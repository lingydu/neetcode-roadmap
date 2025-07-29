class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for e in strs:
            l=len(e)
            result=result+str(l)+"$"+e
        return result

    def decode(self, s: str) -> List[str]:
        r_list=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="$":
                j=j+1
            leng=int(s[i:j])
            r_list.append(s[j+1:j+leng+1])
            i=j+1+leng
        return r_list
                
   