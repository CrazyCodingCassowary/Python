n=int(input("Enter the value of terms:"))

sum=0#initialise
i=1 #initialise

while i <+n:
    sum= sum+i
    i= i+1
    print("\nSum=",sum)

i=0
while i<=0:
 print("I will run forever")
 i=i+1

num=int(input("Enter a number:"))

sum=0

temp=num
while temp> 0:
   digit=temp%10
   sum+=digit**3
   temp//=10

if num==sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstong number")
   