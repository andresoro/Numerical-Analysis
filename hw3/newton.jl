function f(x)

 return x^3-3.0

end

function df(f,x)
 
 h=10.0^(-8)
 ih=complex(0.0,h)
 compx=complex(x,0.0)
 return imag(f(compx+ih))/h

end

x=1.0
tol=10.0^(-10)
while (abs(f(x))>tol)

 x=x-f(x)/df(f,x)

end

println("x= ",x)
