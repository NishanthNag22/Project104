import csv

with open('Project104/data.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
new_data=[]

for i in range(len(fileData)):
    num=fileData[i][2]
    new_data.append(float(num))

n=len(new_data)
new_data.sort()

if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]
print(n)
print("median is "+str(median))