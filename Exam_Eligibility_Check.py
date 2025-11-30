medical_cause=input("Do you have a medical cause Y/N")

atten=int(input('enter the attendance of the student:'))

if medical_cause=='Y':
    print("You are allowed")
else:
    if atten>=75: #checking the conditioon 2
        print("Allowed")
    else:
        print("Not Allowed")

units=int(input("Please enter Number of Units you Command:"))

if(units<50):
    amount=units*2.60
    surcharge=35

elif(units<=100):
    amount=130+((units-50)*3.25)
    surcharge=35

elif(units<=200):
    amount=130+162.50+((units-100))
    surcharge=45


else:
    amount=130+162.50+((units-200)*8.45)
    surcharge=75

total=amount+surcharge
print("\nElectricity Bill=%.2f"%total)
