# Handel index out of range exception

def fun_access():
    indx = int(input("\nEnter Position of element u want to access : "))
    try:
        print(f"Element at {indx} position : {lis[indx-1]}")
    except Exception as e:
        print("Error : ", e)
    finally:
        if input("\nDo you want to access another element ? (y/n) : ") == "y":
            fun_access()


lis = list(input("Enter A list : ").split(", "))
print("List : ", lis)

fun_access()