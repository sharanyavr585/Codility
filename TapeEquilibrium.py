# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    sum=0
    for p in A:
        sum=sum + p
    sum_left=0
    N=len(A)
    for p in range(0,N-1):
        sum_left=sum_left+A[p]
        diff=abs((sum-sum_left)-sum_left)
        if (p==0):
            min=diff
            
        elif(diff<min):
            min=diff
           
    return min
