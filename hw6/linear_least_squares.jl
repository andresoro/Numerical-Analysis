A=Array{Float64}(2,2)
B=Array{Float64}(2)
X=Array{Float64}(2)
xdat=Array{Float64}(3)
ydat=Array{Float64}(3)

xdat[1]=0.0
xdat[2]=1.0
xdat[3]=2.0
ydat[1]=0.0
ydat[2]=1.0
ydat[3]=8.0
n=3

for i in 1:2
 for j in 1:2
  A[i,j]=0.0
  for k in 1:n
   if (i==1)
    phi_i=1.0
   elseif (i==2)
    phi_i=xdat[k]
   end
   if (j==1)
    phi_j=1.0
   elseif (j==2)
    phi_j=xdat[k]
   end
   A[i,j]=A[i,j]+phi_i*phi_j
  end
 end
end

for j in 1:2
 B[j]=0.0
 for k in 1:n
  if (j==1)
   phi_j=1.0
  elseif (j==2)
   phi_j=xdat[k]
  end
  B[j]=B[j]+phi_j*ydat[k]
 end
end

X=inv(A)*B

#Pkg.add("PyPlot")
using PyPlot
Nplot=100
xplot=Array{Float64,1}(Nplot+1)
yplot=Array{Float64,1}(Nplot+1)
a=0.0 
b=2.0
h=(b-a)/Nplot
for iplot in 0:Nplot
 XX=a+h*iplot
 xplot[iplot+1]=XX
 yplot[iplot+1]=X[1]+X[2]*XX
end
println("a0= ",X[1],"\n")
println("a1= ",X[2],"\n")
plot(xplot,yplot,color="red",linewidth=2.0,linestyle="--")
plot(xdat,ydat,color="blue",linewidth=2.0,linestyle="--")
