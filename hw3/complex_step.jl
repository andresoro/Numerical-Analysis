function f(x)

 return x^3

end

function df(f,x)
 
 h=10.0^(-8)
 ih=complex(0.0,h)
 compx=complex(x,0.0)
 return imag(f(compx+ih))/h

end

x=2.0
deriv=df(f,x)
println("deriv= ",deriv)
