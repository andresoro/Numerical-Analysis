A=Array{Float64}(3,3)
B=Array{Float64}(3)
X=Array{Float64}(3)

# interval is 0 to 1
# int_0^1 x^{i+j-2}=1/(i+j-1)
for i in 1:3
 for j in 1:3
  A[i,j]=1.0/(i+j-1.0)
 end
end

# y=x^3
# int_0^1 x^{3+j-1}=1/(3+j)
for j in 1:3
 B[j]=1.0/(3.0+j)
end

X=inv(A)*B

Nplot=100
xplot=Array{Float64,1}(Nplot+1)
yplot=Array{Float64,1}(Nplot+1)
zplot=Array{Float64,1}(Nplot+1)
a=0.0 
b=1.0
h=(b-a)/Nplot
for iplot in 0:Nplot
 XX=a+h*iplot
 xplot[iplot+1]=XX
 yplot[iplot+1]=X[1]+X[2]*XX+X[3]*(XX^2)
 zplot[iplot+1]=XX^3
end
println("a0= ",X[1],"\n")
println("a1= ",X[2],"\n")
println("a2= ",X[3],"\n")
disc=sqrt(X[2]^2-4.0*X[1]*X[3])
root1=(-X[2]-disc)/(2.0*X[3])
root2=(-X[2]+disc)/(2.0*X[3])
println("root1= ",root1,"\n")
println("root2= ",root2,"\n")

#Pkg.add("PyPlot")
using PyPlot
plot(xplot,yplot,color="red",linewidth=2.0,linestyle="--")
plot(xplot,zplot,color="blue",linewidth=2.0,linestyle="--")
