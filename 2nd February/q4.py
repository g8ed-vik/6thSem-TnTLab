#WAP to find out the value of nth term of the Fibonacci sequence by writing a suitable user defined function

def fib(n):
     if n == 1:
         return 0
     elif n == 2:
         return 1
     else:
         return fib(n-1) + fib(n-2)
     
x = fib(5)
print("The value of nth term of the Fibonacci sequence is", x, "for n = 5") 