a=int(input("enter first number"))
b=int(input("enter second number"))
c=a/b
d=a%b
print(c,d)
'''a=int(input("enter 1st marks"))
b=int(input("enter 2nd marks"))
c=int(input("enter 3rd marks"))
d=int(input("enter 4th marks"))
e=int(input("enter 5th marks"))
sum=a+b+c+d+e
av=(a+b+c+d+e)/5
print(sum,av)'''
'''a=float(input("enter basic salary"))
b=float(input("enter house allowance"))
c=float(input("enter transport allowance"))
gs=a+b+c
print(gs)'''
'''r=float(input("enter radius"))
a=3.14*r*r
print(a)'''
'''l=int(input("enter length"))
b=int(input("enter breadth"))
a=l*b
print(a)'''
'''a=float(input("enter first side"))
b=float(input("enter second side"))
c=float(input("enter third side"))
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**0.5
print(s,a)'''
'''b=float(input("enter base"))
h=float(input("enter height"))
a=(b*h)/2
print(a)'''
'''base1=float(input("enter first base"))
base2=float(input("enter second base"))
h=float(input("enter height"))
a=(base1+base2)/2*h
print(a)'''
'''d1=float(input("enter first diagonal"))
d2=float(input("enter second diagonal"))
a=(d1*d2)/2
print("area of diagonal:",a)'''
'''b=float(input("enter base"))
h=float(input("enter height"))
a=b*h
print(a)'''
'''p=float(input("enter principal"))
r=float(input("enter rate"))
t=float(input("enter time"))
n=float(input("enter number of times interest is compound per year"))
ci=p*(1+r/n)**(n*t)
print("compound inertest is:",ci)'''
'''f=float(input("enter faherheit"))
c=(f-32)*5/9
print(c)'''
'''m1=float(input("enter mass1 object"))
m2=float(input("enter mass2 object"))
r=float(input("enter distance of two object"))
G=6.673*(10**-11)
f=G*(m1*m2)/r**2
print(f)'''
'''a=int(input("enter first number"))
b=int(input("enter second number"))
temp=a
a=b
b=temp
print(a,b)'''
'''a=int(input("enter first number"))
b=int(input("enter second number"))
a=a+b
b=a-b
a=a-b
print("a is:",a,"b is:",b)'''
'''x=int(input("enter first number"))
y=int(input("enter second number"))
x=y
y=x
print("x:",x,"y:",y)'''
'''a=8
b=3
c=a%b
print(c)'''
'''a=-8
b=3
c=a%b
print(c)'''
'''a=-8
b=-3
c=a%b
print(c)'''
'''a=8
b=3
print(a>b)
a=8
b=3
print(a<b)
a=8
b=3
print(a==b)
a=8
b=8
print(a>=b)
a=8
b=7
print(a!=b)'''
'''a=8
b=7
print(a>b and b<a)
a=True
b=not a
print(b)'''
'''a=-8
b=3
print(a%b)'''


'''a=15
b=17
print(a & b)
a=15
b=17
print(a | b)'''
'''a=int(input("enter number 1"))
b=int(input("enter number 2"))
if(a>b):
    print(a)
else:
    print(b)'''
'''a=int(input("enter first number"))
b=int(input("enter second number"))
if(a==b):
    print("numbers are equal")'''
'''a=int(input("enter first number"))
if(a>=0):
    print("numbers is positive")
else:
    print("numbers is negative")'''
'''a=int(input("enter first number"))
b=int(input("enter first number"))
c=int(input("enter first number"))
if(a>b):
    if(a>c):
        print("first number is greatest:",a)
    else:
        print("third number is greatest:",c)
else:
    if(b>c):
        print("second number is greatest:",b)
    else:
        print("third number is greatest :",c)'''

'''a=int(input("enter first number"))
b=int(input("enter first number"))
c=int(input("enter first number"))
if(a>b):
    if(a>c):
        print("first number is greatest:",a)
    else:
        print("third number is greatest",c)
elif(b>c):
    print("second number is greatest:",b)
else:
    print("third number is greatest:",c)'''
'''char=input("enter character")
if 'A' <= char <= 'Z':
    print("lower case:",chr(ord(char)+32))
else:
    print("upper case:",chr(ord(char)-32))'''
'''a=int(input("enter year"))
if(a%4==0 and a%100!=0 or a%400==0):
    print("leap year")
else:
    print("not  leap year")'''
'''alphabet=input("enter character")
if(alphabet== 'a' or alphabet== 'e' or alphabet== 'i' or
   alphabet== 'o' or alphabet== 'u'):
    print("vowels")
elif(alphabet== 'A' or alphabet== 'E' or alphabet== 'I' or  alphabet== 'O' or 
     alphabet== 'U'):
    print("vowels")
else:
    print("consonant")'''
'''x=int(input("enter x-axi coordinate"))
y=int(input("enter y-axis coordinate"))
if(x>0 and y>0):
    print("The point lies in first quadrant",(x,y))
elif(x<0 and y>0):
    print("the point lies in second quadrant",(x,y))
elif(x<0 and Y<0):
    print("the point lies in third quadrant",(x,y))
elif(x>0 and y<0):
    print("the point lies in fourth quadrant",(x,y))
else:
    print("the point lies in the axis",(x,y))'''
real1=int(input("enter first real number"))
imag1=int(input("enter first imaginary number"))
real2=int(input("enter second real number"))
imag2=int(input("enter second imaginary number"))
real_part=real1+real2
imag_part=imag1+imag2
print("the sum of two complex number:",real_part,"+",imag_part,"i")
'''x=int(input("enter the day number"))
if(x==1):
    print("monday")
    
elif(x==2):
    print("tuesday")
elif(x==3):
    print("wedensday")
elif(x==4):
    print("thursday")
elif(x==5):
    print("freday")
elif(x==6):
    print("saturday")
elif(x==7):
    print("sunday")
else:
    print("invalid number")'''
'''movies=[]
mov1=input("enter 1st movies")
mov2=input("enter 2nd movies")
mov3=input("enter 3rd movies")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)'''
'''tuple=("C","D","A","A","B","B","A")
print(tuple.count("A"))'''
'''a=int(input("enter a number"))
a=a%10
print(a)
if(a%3==0):
    print("number is divisble ")
else:
    print("not divisible")'''
'''string=input("enter a string")
integer=0
for char in string:
    integer=integer*10+ord(char)-ord('0')
print(integer)'''
'''integer=int(input("enter integer value"))
string=str(integer)
print(string)'''
'''n=int(input("enter number"))
i=1
while(i<=10):
    print(n,"x",i,"=",n*i)
    i+=1'''
#Quadratic expression
'''a=float(input("enter a coefficient"))
b=float(input("enter b coefficient"))
c=float(input("enter c coefficient"))
#calculate discriminant
discriminant=b**2-4*a*c
if(discriminant>0):
    root1=(-b+(discriminant**0.5))/(2*a)
    root2=(-b-(discriminant**0.5))/(2*a)
    print(root1,root2)
elif(discriminant==0):
    root=-b/(2*a)
    print(root)
else:
    real_part=-b/(2*a)
    imag_part=(abs(discriminant)**0.5)/(2*a)
    print(real_part,"+",imag_part,"i" and real_part,"-",imag_part,"i")'''
'''n=int(input("enter number of terms"))
a=0
b=1
while(n>0):
    print(a)
    c=a+b
    a=b
    b=c
    n-=1'''
'''salary = 8000

def printSalary():
  salary = 12000
  print("Salary:", salary)
  
printSalary()
print("Salary:", salary)'''
'''var1 = 1
var2 = 2
var3 = "3"

print(var1 + var2 + var3)'''
'''listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)
sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add(1, "Vicki")
print(sampleSet)'''
'''for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )'''
'''def func1():
    x = 50
    return x
func1()
print(x)'''
'''x = 50
def fun1():
    x = 25
    print(x)
    
fun1()
print(x)'''
'''def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)'''
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)w



            
    






    



    
























               
