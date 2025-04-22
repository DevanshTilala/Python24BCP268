class Matrix:
    def __init__(self,matrix1=0,matrix2=0):
        self.m1=matrix1
        self.m2=matrix2
    def matrix_add(self):
        m3=[]
        for i,j in zip(self.m1,self.m2):
            row=[]
            for k,l in zip(i,j):
                row.append(k+l)
            m3.append(row)
        print(m3)
    def matrix_multi(self):
        m3=[]
        for i in range(3):
            row=[]
            for j in range(3):
                x=0
                for k in range(3):
                    x+=self.m1[i][k]*self.m2[k][j]
                row.append(x)
            m3.append(row)
        print(m3)
    def matrix_transpose(self):
        m3=[]
        for i in range(3):
            row=[]
            for j in range(3):
                row.append(self.m1[j][i])
            m3.append(row)
        print(m3)
                

m11=[[1,0,0],[0,1,0],[0,0,1]]
m22=[[1,0,0],[0,1,0],[0,0,1]]
a=Matrix(m11,m22)
a.matrix_add()
a.matrix_multi()
a.matrix_transpose()