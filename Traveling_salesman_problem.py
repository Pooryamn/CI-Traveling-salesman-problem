import csv

########## <-Fuctions-> #########
def Fitness(Sample):
    # Avoid repeating one city twice in the solution

    # Avoid setting two citys next to each other

    pass



Data = []

with open('Sample_Data.csv',mode='r') as DFile:
    CSV_File = csv.reader(DFile,delimiter=',')

    for row in CSV_File:
        Data.append(row)

# Parameters: 
Max_iteration = 1000
Populution_size = 100

