import csv
import random

########## <-Fuctions-> #########
def Read_data():
    with open('Sample_Data.csv',mode='r') as DFile:
        CSV_File = csv.reader(DFile,delimiter=',')

        for row in CSV_File:
            Data.append(row)
    
    DFile.close()

def Data_converter(Data):
    for i in range(len(Data[0])):
        for j in range(len(Data[0])) :
            Data[i][j] = int(Data[i][j])
    return Data

def Fitness(Sample):
    # Avoid repeating one city twice in the solution
    if (Check_Duplicate_item(Sample)==True):
        # Sampple has duplicated citis, Its fitness is Zero
        return 0
    # Avoid setting two citys next to each other
        for i in range(len(Sample)-2):
            if (Data[sample[i]-1][Sample[i+1]-1] == -1): 
                # There isn't any direct route between city(i) and city(i+1)
                return 0
        if (Data[Sample[-1]-1][Sample[0]-1] == -1):
            return 0
    
    # Sample is feasible and we can calculate its fitness:
    Route_Cost = 0
    for i in range(len(Sample)-2):
        Route_Cost += Data[Sample[i]-1][Sample[i+1]-1]
    
    Route_Cost += Data[Sample[-1]-1][Sample[0]-1]

    Fit_Value = 1000.0 / Route_Cost
    return Fit_Value


def Check_Duplicate_item(Sample):
    if len(Sample) == len(set(Sample)):
        return False
    return True


def Initialization(Data,Populution_size):

    # sample sizes
    Each_Sample_size = len(Data[0])

    population = []

    # main loop for generating samples
    for i in range(Populution_size):
        # empty sample
        Sample = []
        # generate sample 
        for j in range(Each_Sample_size):
            Sample.append(j+1)
        
        # number of modifications:
        Modifications = random.randint(1,30)

        # do modifications
        for j in range(Modifications):
            Tmp_Position1 = random.randint(0,Each_Sample_size-1)
            Tmp_Position2 = random.randint(0,Each_Sample_size-1)

            #swap indexes:
            Sample[Tmp_Position1],Sample[Tmp_Position2] = Sample[Tmp_Position2],Sample[Tmp_Position1]
        
        # add sample to populaion 
        population.append(Sample)

    return population

# main

# Parameters: 

Max_iteration = 1000
Populution_size = 5

# data
Data = []
Read_data()
Data = Data_converter(Data)

# Algorithm
population = Initialization(Data,Populution_size)





