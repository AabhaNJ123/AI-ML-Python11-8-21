from array import *

arr = array('i', [10, 20, 30, 40, 50])
print("\nArray : ", arr)

print("\nAccessing elements from the Array, arr[3] : ", arr[3])
print("Slicing of a Array, arr[3:6] : ", arr[3:6])
print("Slicing of a Array, arr[2:] : ", arr[2:])
print("Slicing of a Array, arr[:] : ", arr[:])
arr[4]=0
print("Updating Elements in a Array, arr[4]=0 : ", arr)


arr = array('i', [10, 20, 30, 40, 50])
print("\nArray : ", arr)

print("\nApplied Function : Result")

arr.append(50)
print(".append(50) : ", arr)

print(".count(50) : ", arr.count(50))

arr.extend([70, 80, 90])
print(".extend([70, 80, 90]) : ", arr)

arr.insert(5, 60)
print(".insert(5, 60) : ", arr)

print(".index(50) : ", arr.index(50))

arr.pop()
print(".pop() : ", arr)
arr.pop(6)
print(".pop(6) : ", arr)

arr.remove(80)
print(".remove(80) : ", arr)

arr.reverse()
print(".reverse() : ", arr)