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

def TSP(populaion,fitness_arr,Max_iteration):


    each_population_size = len(populaion[0])

    for i in range(Max_iteration):
        
        # Cross over
        children = []
        next_generation = []

        for j in range(500):
            par1 = random.choice(populaion)
            par2 = random.choice(populaion)
            tmp = par1[0:int(each_population_size/2)] + par2[int(each_population_size/2):]
            children.append(tmp)
        
        # mutation

        mutation_thershold = int(0.05 * len(populaion[0]))

        for chid in children:

            for j in range(mutation_thershold):
                
                index1 = random.randint(0,each_population_size-1)
                index2 = random.randint(0,each_population_size-1)

                #swap indexes:
                chid[index1],chid[index2] = chid[index2],chid[index1]

        # calculate fitness and remove 0 fitnesses
        for k in children:
            a = Fitness(k)
            if (a > 0):
                next_generation.append(k)

        populaion = []
        populaion = next_generation

    fitness_arr = []

    for i in populaion:
        fitness_arr.append(Fitness(i))
    
    p=fitness_arr.index(max(fitness_arr))
    cost = int(1000 / fitness_arr[p])
    path = population[p]

    print('Path : {}'.format(path))
    print('Cost : {}'.format(cost))
    print('Fitness : {}'.format(fitness_arr[p]))

# main

# Parameters: 

Max_iteration = 1000
Populution_size = 100

# data
Data = []
Read_data()
Data = Data_converter(Data)

# Algorithm
population = Initialization(Data,Populution_size)

# evaluate fitness for inial population:

fitness_arr = []

for sample in population:
    fitness_arr.append(Fitness(sample))

TSP(population,fitness_arr,Max_iteration)