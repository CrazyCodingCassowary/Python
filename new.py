string=input("Please enter your own word: ")

char=input("Please enter your own charaacter: ")

i=0
count=0
while (i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
print("The total number of times", char,"has appeared=",count)

lower=int(input("Enter a lower range: "))
upper=int(input("Enter an upper range: "))


print("Prime numbers between", lower,"and",upper,"are: ")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2, num):
            if(num%i)==0:
                break
        else:
            print(num)
# Input a number
num = int(input("Enter the number : "))
t = num
numLen = 0

# iterate the loop to find the number of digits
while t > 0:
    numLen = numLen + 1
    t = int(t / 10)

if numLen >= 4:  # condition 1
    halfLen = int(numLen / 2)
    chk = 0

    while num > 0:  # iterate through digits
        rem = num % 10

        if chk == halfLen:  # nested condition 1
            midOne = rem
        elif chk == (halfLen - 1):
            midTwo = rem

        num = int(num / 10)
        chk = chk + 1

    prod = midOne * midTwo  # product of middle digits

    # display the result
    print("\nProduct of Mid digits (" + str(midOne) + " * " + str(midTwo) + ") = ", prod)

else:
    print("\nIt's not a 4 or more than 4-digit number!")
