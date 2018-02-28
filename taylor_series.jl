function my_nfact(n)

  nfact=1.0
  for i in 1:n
   nfact=nfact*i
  end
  return nfact

end

function my_power(x,N)

  pow=1.0
  for i in 1:N
   pow=pow*x
  end

  return pow

end

function PN(N,x)

 y=1.0
 for i in 1:N
  nfact=my_nfact(i) 
  term=my_power(x,i)/nfact
  y=y+term
 end
    
 return y
 
end 

N=3
x=0.1
y=PN(N,x)
exact=exp(x)
println("x=",x," and N= ",N,"\n")
println("Taylor series approximation is: ",y,"\n")
println("exp(x) is: ",exact,"\n")
println("error is: ",abs(exact-y),"\n")
#Pkg.add("PyPlot")
using PyPlot
Nplot=100
x_array=Array{Float64,1}(Nplot+1)
y_array=Array{Float64,1}(Nplot+1)
z_array=Array{Float64,1}(Nplot+1)
a=0.0 
b=1.0
h=(b-a)/Nplot
for iplot in 0:Nplot
 x_array[iplot+1]=a+h*iplot  
 y_array[iplot+1]=PN(N,x_array[iplot+1])
 z_array[iplot+1]=exp(x_array[iplot+1])
end
plot(x_array,y_array,color="red",linewidth=2.0,linestyle="--")
plot(x_array,z_array,color="blue",linewidth=2.0,linestyle="--")
