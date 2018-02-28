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

# evaluate P_{2N+1}
function PN_sin(N,x)

 y=0.0
 for i in 0:N
  M=2*i+1
  nfact=my_nfact(M)
  term=my_power(x,M)/nfact
  term2=my_power(-1.0,i)
  y=y+term*term2
 end

 return y

end

# 1. search "Julia Box" and go to the web site.
# 2. login with google
# 3. "New" -> Julia 0.6.0
# 4. copy and paste this program into the box.
# 5. click on "Run"
#Pkg.add("PyPlot")
using PyPlot

Nplot=100
x_array=Array{Float64,1}(Nplot+1)
y_array=Array{Float64,1}(Nplot+1)
z_array=Array{Float64,1}(Nplot+1)

my_pi=4.0*atan(1.0)

NHI=5

for N in 0:NHI

 M=2*N+1

 println("N=",N," M= ",M,"\n")

 a=-my_pi/4.0
 b=my_pi/4.0
 h=(b-a)/Nplot

 biggest_error=0.0

 for iplot in 0:Nplot
  x_array[iplot+1]=a+h*iplot  
  y_array[iplot+1]=PN_sin(N,x_array[iplot+1])
  z_array[iplot+1]=sin(x_array[iplot+1])
  err=abs(y_array[iplot+1]-z_array[iplot+1])
  if (err>biggest_error)
   biggest_error=err
  end
 end
 plot(x_array,y_array,color="red",linewidth=2.0,linestyle="--")
 println("biggest error ",biggest_error,"\n")
 error_bound=my_power(b,M+2)/my_nfact(M+2)
 println("error bound ",error_bound,"\n")
end 

plot(x_array,z_array,color="blue",linewidth=2.0,linestyle="--")
