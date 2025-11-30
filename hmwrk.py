n=int(input("Enter Number"))

c=0
while n>0:
 n=n//10
 c=c+1

print("Number of digits are",c)
# Function to convert decimal to binary
def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return "-" + bin(decimal_number)[3:]  # Handle negative numbers
    return bin(decimal_number)[2:]  # Remove '0b' prefix

# Ask user for input
try:
    number = int(input("Enter a decimal number: "))
    binary = decimal_to_binary(number)
    print(f"Binary representation: {binary}")
except ValueError:
    print("Please enter a valid integer.")
