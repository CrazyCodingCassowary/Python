num=-1
if num>0:
    print(num, "is a positive number")
else:
    print(num, "is a negative number")

num=3
if num>0:
    print(num, "is a posiTtive number")

actual_cost=float(input("Please enter the Actual Product Price"))
sale_amount=float(input("Please enter the Sales Amount:"))

if(sale_amount>actual_cost):
    amount=sale_amount-actual_cost
    print("Total Profit={0}".format(amount))
else:
    print("No Profit")

i=int(input("enter a number: "))

if (i<15):
    print("i is smaller than 15")
    print("this is the [if] block")

else:
     print("i is greater than 15")
     print("this is the [else] block")
print("This is not it [if], nor is it in [else]")

number=int(input("Enter a number to check whether it is even or odd."))
print("\n Your number of choice is",number)

if number%2==0:
    print("This is an even number")
else:
    print("This is an odd number")




char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter only one character.")
else:
    if char.isalpha():
        print(f"'{char}' is an alphabet letter.")
    else:
        print(f"'{char}' is not an alphabet letter.")
