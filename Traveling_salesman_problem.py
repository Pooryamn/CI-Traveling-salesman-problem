import csv

########## <-Fuctions-> #########
def Read_data():
    with open('Sample_Data.csv',mode='r') as DFile:
        CSV_File = csv.reader(DFile,delimiter=',')

        for row in CSV_File:
            Data.append(row)
    
    DFile.close()

def Fitness(Sample):
    # Avoid repeating one city twice in the solution
    if (Check_Duplicate_item(Sample)==True):
        # Sampple has duplicated citis, Its fitness is Zero
        return 0
    # Avoid setting two citys next to each other
        for i in range(len(Sample)-2):
            if (Data[sample[i]][Sample[i+1]] == -1): 
                # There isn't any direct route between city(i) and city(i+1)
                return 0
        if (Data[Sample[-1]][Sample[0]] == -1):
            return 0
    
    # Sample is feasible and we can calculate its fitness:
    Route_Cost = 0
    for i in range(len(Sample)-2):
        Route_Cost += Data[Sample[i]][Sample[i+1]]
    
    Route_Cost += Data[Sample[-1]][Sample[0]]

    Fit_Value = 1.0 / Route_Cost
    return Fit_Value


def Check_Duplicate_item(Sample):
    if len(Sample) == len(set(Sample)):
        return False
    return True


# main

# Parameters: 
Max_iteration = 1000
Populution_size = 100

# data
Data = []

Read_data()





