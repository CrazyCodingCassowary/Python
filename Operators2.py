a=10
b=12
c=0

if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("At least one number has boolean value as False")

a=10
b=-10
c=0

if a>0 or b>0:
    print("Either one of the numbers is greater than 0")
else:
    print("No number is greater than 0")

if b>0 or c>0:
    print("Either one of the numbers is greater than 0")
else:
    print("No number is greater than 0")

a=10
b=12
c=12

print(a!=b)
print(b!=c)

a="python"
b="coding"
if a!=b:
    print(a,'and', b, 'are different.')

a=4
b=5

if(a==1)!=(b==5):
    print('Hello')

a=int(input("enter a number"))
if a%2!=0:
    print(a," is not an even number.")
else:
    print(a,"is an even number")

height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg"))
BMI=weight/(height/100)**2

print("Your BMI is", BMI)

if BMI <=18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are weight")
elif BMI <= 29.9:
    print("You are weight")
elif BMI <= 34.9:
    print("You are weight")
elif BMI <= 39.9:
    print("You are weight")
else:
    print("You are severely obese.")



