
c=lambda n,a=1,b=0 : c(n-1,a+b,a) if n>1 else str(a+b)+" no. of ways\n"
##^^^^^^^^method--1^^^^^^^^##


d=lambda n: str(round((1/(5)**0.5)*((0.5*(1+(5)**0.5))**(1+n))))+" no. of ways\n\n"
##^^^^^^^^method--2^^^^^^^^##


print(c(59), d(59))
print(c(8), d(8))
print(c(int(input())))
print (d(1000))


### functional one liners-)))
## author-->> Sayan Chandra..

'''
The d function is a FIBONACCI GENERATOR ITSELF
////
NO NEED FOR RECURSION AND LOOPING
$$$ IT WAS IN MY SECOND VERSION OF CODE...I INCLUDED IN THIS ONE NOW..$$$

Thats why d is more efficient than c function
///
'''

'''challenge thread is in the comments'''
