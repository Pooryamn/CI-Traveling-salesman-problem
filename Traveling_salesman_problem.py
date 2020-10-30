import csv


Data = []

with open('Sample_Data.csv',mode='r') as DFile:
    CSV_File = csv.reader(DFile,delimiter=',')

    for row in CSV_File:
        Data.append(row)

print(Data[3][4])