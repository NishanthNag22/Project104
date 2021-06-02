import csv
from types import prepare_class
from typing import Counter

with open('Project104/data.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
new_data=[]

for i in range(len(fileData)):
    num=fileData[i][2]
    new_data.append(float(num))

data=Counter(new_data)
mode_data_for_range={
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140-150":0,
    "150-160":0
}

for weight,occurrence in data.items():
    if 100< float(weight)<110:
        mode_data_for_range["100-110"]+=occurrence
    elif 110<float(weight)<120:
        mode_data_for_range["110-120"]+=occurrence
    elif 120<float(weight)<130:
        mode_data_for_range["120-130"]+=occurrence
    elif 130<float(weight)<140:
        mode_data_for_range["130-140"]+=occurrence
    elif 140<float(weight)<150:
        mode_data_for_range["140-150"]+=occurrence
    elif 150<float(weight)<160:
        mode_data_for_range["150-160"]+=occurrence

mode_range,mode_occurrence=0,0

for range,occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurrence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is {mode:2f}")