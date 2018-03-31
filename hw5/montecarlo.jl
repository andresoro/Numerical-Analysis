# 1. search "Julia Box" and go to the web site.
#  https://www.juliabox.com
# 2. login with google
# 3. Files: "Upload" 
# 4. highlight your file and do "copy"
# 5. "New" -> Julia 0.6.0
# 6. paste your program into the box.
# 7. click on "Run"
# 8. File -> Print Preview

function f(x)
 return x^2+2.0
end

#Pkg.add("Plots")
#using Plots

srand(1234)
N=100
sum=0.0
for i=0:N-1
 x=rand()
 x=2.0*(x-0.5)
 sum=sum+f(x)
end
sum=2.0*sum/N
# x^3/3+2x -> 2/3+4=14/3
exact=14.0/3.0
error=abs(sum-exact)
println("approx= ",sum)
println("exact= ",exact)
println("error= ",error)
