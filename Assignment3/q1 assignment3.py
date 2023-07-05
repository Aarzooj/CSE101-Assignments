n=int(input())
i=0
def pattern1(n,i):
    if n==0:
        return 
    else:
        print('* '*n,end="")
        print('  '*(2*i),end="")
        print('* '*n)       
        pattern1(n-1,i+1) 
j=0                 
def pattern2(n,j):
    if n<=1:
        return
    else:
        pattern2(n-1,j+1)
        print('* '*n,end="")  
        print('  '*(2*j),end="")
        print('* '*n)
pattern1(n,i)
pattern2(n,j)          