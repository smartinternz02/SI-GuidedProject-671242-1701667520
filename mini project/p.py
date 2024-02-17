import csv
with open("emp.csv",'w',newline='') as f:
  w=csv.writer(f)
  w.writerow(["ENO","ENAME","ESAL","EADDR"])
  n=int(input("no of employees"))
  for i in range (n):
     eno=int(input("enter emlpoyee number:"))
     ename=input("enter employee name:")
     esal=float(input("enter employee salary:"))
     eaddr=input("enter employee address:")
     w.writerow([eno,ename,esal,eaddr])
print("total employees data written to csv file sucessfully")
