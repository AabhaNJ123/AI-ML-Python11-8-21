import csv
with open("xyz.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["SrNo.","Name","ID","RollNo"])
    n=int(input("\nEnter number of Students : "))
    for i in range(n):
        SrNo   = input("\nEnter Serial number of the student : ")
        Name   = input("Enter name of the student          : ")
        ID     = input("Enter ID of the student            : ")
        RollNo = input("Enter Roll Number of the student   : ",)
        w.writerow([SrNo,Name,ID,RollNo])
    print("\nData Updation Successful\n")

f=open("xyz.csv","r")
r=csv.reader(f)
data=list(r)
for line in data:
    for word in line:
        print(word,"\t",end="")
    print()