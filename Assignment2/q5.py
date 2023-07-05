N=int(input('Enter the order of matrix desired'))
l=[]
for i in range(N):
    t=tuple(map(int,input('Enter coordinates').split()))
    l.append(t)
matrix=[]    
for m in range(N):
    z=[]
    for n in range(3):
        if n<2:
            z.append(l[m][n])
        else:
            z.append(1)    
    matrix.append(z)        
cx=int(input('Enter cx'))
cy=int(input('Enter cy'))
m_matrix=[]
r1=[cx,0,0]
r2=[0,cy,0]
r3=[0,0,1]
m_matrix.append(r1)
m_matrix.append(r2)
m_matrix.append(r3)
f_matrix=[]
for j in range(N):
    ff=[]
    sum=0   
    for l in range(3):
        for k in range(3):                
            sum+=int(matrix[j][k])*int(m_matrix[k][l])            
        ff.append(sum)
        sum=0
    f_matrix.append(ff)  
for i in f_matrix:
    del i[2]
print(f_matrix)    