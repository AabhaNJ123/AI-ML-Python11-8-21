m=int(input("Enter Marks : "))
if m<25:
    print("F")
elif m>=25 and m<45:
    print("E")
elif m>=45 and m<50:
    print("D")
elif m>=50 and m<60:
    print("C")
elif m>=60 and m<80:
    print("B")
elif m>=80 and m<=100:
    print("A")
else:
    print("Wrong input")