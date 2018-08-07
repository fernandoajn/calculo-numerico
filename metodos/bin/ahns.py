#Solution to equations in one variable
#Bisection method

#Data to be given by the User.
import math
import numpy

print("")
print("Please use PYTHON Notations.\n")
Eq = input("Enter Equation: ")
print(" ")
a = float(input("Enter Lower Limit: "))             # Upper Limit
b =float(input("Enter Upper Limit: "))             # Lower Limit
print(" ")
t = float(input("Enter Tolerance: "))               # Tolerance

print(" ")
print("Given Equation: {0}=0".format(Eq))
print("Interval: [{0},{1}].".format(a,b))
print("Tolerance:",t)
print(" ")

A = 1               #To denote Approximations (used later on)

x=a               #Putting Value in Equation
  
fa = eval(Eq)
print("Value of f(x) at Lower Limit:",fa)
  
x=b               #Putting Value in Equation
  
fb = eval(Eq)
print("Value of f(x) at Upper Limit:",fb)
  
if((fa*fb)<0):
  print("Root lies in [{0},{1}].".format(a,b))
  q=0
  while(q==0):
    print(" ")
    print("Approximation",A)
    A+=1
    print(" ")
  
    p = float((a+b)/2) #Mid-point of Interval
    print("Mid-point of Interval:",p)
  
    x=p               #Putting Value in Equation
  
    fp = eval(Eq)
    print("Value of f(x) at Mid-point:",fp)
    print("New Intervals: [{0},{1}] , [{2},{3}].".format(a,p,p,b))
  
    if((fa*fp)<0):
      print("Root lies in [{0},{1}].".format(a,p))
      a=a
      b=p
  
    elif((fb*fp)<0):
      print("Root lies in [{0},{1}].".format(p,b))
      a=p
      b=b
  
    #Check
    if(abs(b-a)<t):
      print(" ")
      print("|{0} - {1}| = {2} is in Allowable Limit.".format(b,a,abs(b-a)))
      print(" ")
      print("Approximate Solution is:",b)
      print(" ")
      print("     **** Thanks for Using AHSAN's Calculator ****  ")
      break
  
    else:
      print(" ")
      print("|{0} - {1}| = {2} is not in Allowable Limit.".format(b,a,abs(b-a)))
      continue

else:
    print("Root do not lies in [{0},{1}].".format(a,b))