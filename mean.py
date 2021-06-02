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
total=0

for x in new_data:
    total=total+x

mean=total/n
print("Mean is "+str(mean))