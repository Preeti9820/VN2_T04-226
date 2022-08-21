
from typing import List

class Time:
    # A = list(input("enter list"))
    def largest(self,A)->str:
        result=""
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i==j or j==k or k==i:
                        continue
                    hh=str(A[i])+str(A[j])
                    mm=str(A[k])+str(A[6-i-j-k])
                    time=hh+":"+mm
                    if hh<"24" and mm<"60" and time>result:
                        result=time
        return result
x=Time.largest([1,2,3,4])
print(x)