# Name: Avinab Saha
# Roll: 15EC10071
# Assignment 7 ML CS60050
# Tested with Python 2.7.12 (default, Nov 20 2017, 18:23:56) [GCC 5.4.0 20160609] on linux2

import numpy as np

def euclidean(P1,P2,w):
    dist=0
    for i in range(w):
        dist =dist+ (P1[i]-P2[i])*(P1[i]-P2[i])
    return(np.sqrt(dist))

# Reading number of Training Examples
with open('data7.csv') as file:
    line_count=0
    for line in file:    
        line_count = line_count+1

line = line.strip()
line = line.split(',')
no_of_attributes = len(line)

# Defining Data Matrix
w = no_of_attributes
h = line_count
Training_Data = np.zeros(shape=(h,w))
Label = np.zeros(h,dtype=int)
# Reading the Training Data Provided
with open('data7.csv') as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(w):
                Training_Data[line_count][i] = line[i]
        line_count = line_count+1


#print(Training_Data)
# Set Seed to generate same results always
# np.random.seed(41)
# Randomly Assign Cluster Centres

one = np.random.random_integers(19)
two = np.random.random_integers(19)
while(one==two):
    two = np.random.random_integers(19)
#print(one,two)


C1 = Training_Data[one,:]
C2 = Training_Data[two,:]
#print(Label)

for loop in range(10):
    # Assign Labels
    for i in range(h):
        d1= euclidean(C1,Training_Data[i,:],w)
        d2= euclidean(C2,Training_Data[i,:],w)
        if (d1<=d2):
            Label [i]= 1
        if (d1>d2):
            Label[i] = 2
    # Update Centre of Cluster
    no_clusters_in_1 = np.count_nonzero(Label==1)
    no_clusters_in_2 = np.count_nonzero(Label==2)
    #print(no_clusters_in_1,no_clusters_in_2)
    temp_C1= np.zeros(w)
    temp_C2= np.zeros(w)
    for i in range(h):
        if(Label[i]==1):
            temp_C1 = temp_C1+ Training_Data[i,:]
        if(Label[i]==2):
            temp_C2 = temp_C2+ Training_Data[i,:]
    C1 = temp_C1/no_clusters_in_1
    C2 = temp_C2/no_clusters_in_2
    #print(Label)


with open('15EC10071_7.out','w') as file:
    #print(Label)
    for x in Label:
		file.write(str(int(x)))
		file.write(" ")
file.close()
