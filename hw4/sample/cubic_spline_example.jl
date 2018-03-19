A=Array{Float64}(8,8)
B=Array{Float64}(8)
X=Array{Float64}(8)

for i in 1:8
 for j in 1:8
  A[i,j]=0.0
 end
end

pi_local=4.0*atan(1.0)
x0=0.0
x1=0.5*pi_local
x2=pi_local

# f(x)=sin(x)
# free boundary condition on the left.
# clamped boundary condition on the right (S_{1}'(x2)=-1)
# a0+b0(x-0)+c0(x-0)^2+d0(x-0)^3
# b0+2 c0(x-0)+3 d0(x-0)^2
# 2 c0+6 d0(x-0)
A[1,1]=1.0 # S0(0)=0
B[1]=0.0
A[2,3]=1.0 # S0''(0)=0
B[2]=0.0
A[3,1]=1.0
A[3,2]=x1
A[3,3]=x1^2
A[3,4]=x1^3
B[3]=1.0
A[4,5]=1.0
B[4]=1.0
A[5,5]=1.0
A[5,6]=(x2-x1)
A[5,7]=(x2-x1)^2
A[5,8]=(x2-x1)^3
B[5]=0.0
A[6,6]=1.0
A[6,7]=2.0*(x2-x1)
A[6,8]=3.0*(x2-x1)^2
B[6]=-1.0
A[7,2]=1.0
A[7,3]=2.0*x1
A[7,4]=3.0*x1^2
A[7,6]=-1.0
B[7]=0.0
A[8,3]=2.0
A[8,4]=6.0*x1
A[8,7]=-2.0
B[8]=0.0

X=inv(A)*B

#Pkg.add("PyPlot")
using PyPlot
Nplot=100
xplot=Array{Float64,1}(Nplot+1)
yplot=Array{Float64,1}(Nplot+1)
zplot=Array{Float64,1}(Nplot+1)
a=0.0 
b=pi_local
h=(b-a)/Nplot
for iplot in 0:Nplot
 XX=a+h*iplot
 xplot[iplot+1]=XX
 if (XX<=x1)
  yplot[iplot+1]=X[1]+X[2]*XX+X[3]*XX^2+X[4]*XX^3
 else
  yplot[iplot+1]=X[5]+X[6]*(XX-x1)+X[7]*(XX-x1)^2+X[8]*(XX-x1)^3
 end
 zplot[iplot+1]=sin(XX)
end
plot(xplot,yplot,color="red",linewidth=2.0,linestyle="--")
plot(xplot,zplot,color="blue",linewidth=2.0,linestyle="--")
