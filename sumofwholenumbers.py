n=int(input("Enter the number whose sum you would like to find:"))

sum=0

for i in range(1, n+1):
 sum = sum+i
 print("\nSum=", sum)

string=input("Please enter your own string:")
string2=("")
for i in string:
 string2=i+string2
 print("/nThe Original String=", string)
 print("/nThe Reversed String=", string2)

 n=int(input("Enter value of n: "))

 print("numberss from{0} to {1} are: ".format(n,1))

 for i in range(n,0,-1):
  print(i)
  
print("hello")

n=int(input("Enter the number whose sum you would like to find:"))
sum=n
for i in range(1, n-1):
 sum=sum+i
 print("\nSum=", sum)