f=open('xyz.txt','r')
print("Name        : ",f.name)
print("Mode        : ",f.mode)
print("Is Closed   : ",f.closed)
print("Is Readable : ",f.readable())
print("Is Writable : ",f.writable())
f.close()
print("closed      : ",f.closed)

#append content to file
f = open("xyz.txt", "a")
f.write(" Jahagirdar")
f.close()
f = open("xyz.txt", "r")
print(f.read())

#overwrite content in file
f = open("xyz.txt", "a")
f.write("\nNow the file has more content!")
f.close()
f = open("xyz.txt", "r")
print(f.read())