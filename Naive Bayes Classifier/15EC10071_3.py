# Roll: 15EC10071
# Name: Avinab Saha
# Assignment number: 3
# Specific compilation/execution flags: None

import numpy as np

def counter(Var1,Training_Label,length_of_training_set):
    count00=0
    count01=0
    count10=0
    count11=0
    for loop in range(length_of_training_set):
    
        if int(Var1[loop]) == 0 and int(Training_Label[loop]) == 0 :
            count00 = count00 +1
        if int(Var1[loop]) == 0 and int(Training_Label[loop]) == 1 :
            count01 = count01+1
        if int(Var1[loop]) == 1 and int(Training_Label[loop]) == 0 :
            count10 = count10+1
        if int(Var1[loop]) == 1 and int(Training_Label[loop]) == 1 :
            count11 = count11+1

    return count00,count01,count10,count11

# Reading number of Training Examples
with open('data3.csv') as file:
    line_count=0
    for line in file:    
        line_count = line_count+1

# Defining Data Matrix
w1 = 8
w2 = 1
h = line_count
Training_Data = np.zeros(shape=(h,w1))
Training_Label = np.zeros(h)
length_of_training_set = h
# Reading the Training Data Provided
with open('data3.csv') as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(9):
            if i<8:
                Training_Data[line_count][i] = line[i]
            else:
                Training_Label[line_count] = line[i]
    
        line_count = line_count+1

# Reading number of Test Examples
with open('test3.csv') as file:
    line_count=0
    for line in file:    
        line_count = line_count+1

# Defining Data Matrix
w1 = 8
h = line_count
Test_Data = np.zeros(shape=(h,w1))
length_of_test_Data = h

# Reading the Test Data Provided
with open('test3.csv') as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(8):
                Test_Data[line_count][i] = line[i]
    
        line_count = line_count+1


# Training Code

# Calculating Prior Probabilities P(Y=1) & P(Y=0)
number_of_ones = np.count_nonzero(Training_Label == 1)
number_of_zeros = length_of_training_set - number_of_ones

"""
print(number_of_ones)
print(number_of_zeros)
"""

prior_probability_1 = float(number_of_ones+1)/(length_of_training_set+ 2)
prior_probability_0 = float(number_of_zeros+1)/(length_of_training_set+ 2)

"""
print(prior_probability_0)
print(prior_probability_1)
print(prior_probability_0+prior_probability_1)
"""

Var1 = Training_Data[:,0]
Matrix_Var1 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var1,Training_Label,length_of_training_set)
    
Matrix_Var1[0][0] = a
Matrix_Var1[0][1] = b
Matrix_Var1[1][0] = c
Matrix_Var1[1][1] = d
#print(Matrix_Var1)


Var2 = Training_Data[:,1]
Matrix_Var2 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var2,Training_Label,length_of_training_set)
    
Matrix_Var2[0][0] = a
Matrix_Var2[0][1] = b
Matrix_Var2[1][0] = c
Matrix_Var2[1][1] = d
#print(Matrix_Var2)

Var3 = Training_Data[:,2]
Matrix_Var3 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var3,Training_Label,length_of_training_set)
    
Matrix_Var3[0][0] = a
Matrix_Var3[0][1] = b
Matrix_Var3[1][0] = c
Matrix_Var3[1][1] = d
#print(Matrix_Var3)

Var4 = Training_Data[:,3]
Matrix_Var4 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var4,Training_Label,length_of_training_set)
    
Matrix_Var4[0][0] = a
Matrix_Var4[0][1] = b
Matrix_Var4[1][0] = c
Matrix_Var4[1][1] = d
#print(Matrix_Var4)

Var5 = Training_Data[:,4]
Matrix_Var5 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var5,Training_Label,length_of_training_set)
    
Matrix_Var5[0][0] = a
Matrix_Var5[0][1] = b
Matrix_Var5[1][0] = c
Matrix_Var5[1][1] = d
#print(Matrix_Var5)


Var6 = Training_Data[:,5]
Matrix_Var6 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var6,Training_Label,length_of_training_set)
    
Matrix_Var6[0][0] = a
Matrix_Var6[0][1] = b
Matrix_Var6[1][0] = c
Matrix_Var6[1][1] = d
#print(Matrix_Var6)


Var7 = Training_Data[:,6]
Matrix_Var7 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var7,Training_Label,length_of_training_set)
    
Matrix_Var7[0][0] = a
Matrix_Var7[0][1] = b
Matrix_Var7[1][0] = c
Matrix_Var7[1][1] = d
#print(Matrix_Var7)


Var8 = Training_Data[:,7]
Matrix_Var8 = np.zeros([2,2],dtype=int)
a,b,c,d = counter(Var8,Training_Label,length_of_training_set)
    
Matrix_Var8[0][0] = a
Matrix_Var8[0][1] = b
Matrix_Var8[1][0] = c
Matrix_Var8[1][1] = d
#print(Matrix_Var8)


test_results = np.zeros(length_of_test_Data,dtype=int)
#print(test_results)
# Testing Code
for i in range(length_of_test_Data): 
    test1 = Test_Data[i,:]


    # Calculate For Class 0
    prob0 = prior_probability_0
    if (int(test1[0]))== 0:
        prob0 = prob0 * (float(Matrix_Var1[0][0]+1) / (Matrix_Var1[0][0]+Matrix_Var1[1][0]+2))
    if (int(test1[0]))== 1:
        prob0 = prob0 * (float(Matrix_Var1[1][0]+1) / (Matrix_Var1[0][0]+Matrix_Var1[1][0]+2))

    if (int(test1[1]))==0:
        prob0 = prob0 * (float(Matrix_Var2[0][0]+1) / (Matrix_Var2[0][0]+Matrix_Var2[1][0]+2))
    if (int(test1[1]))==1:
        prob0 = prob0 * (float(Matrix_Var2[1][0]+1) / (Matrix_Var2[0][0]+Matrix_Var2[1][0]+2))

    if (int(test1[2]))==0:
        prob0 = prob0 * (float(Matrix_Var3[0][0]+1) / (Matrix_Var3[0][0]+Matrix_Var3[1][0]+2))
    if (int(test1[2]))==1:
        prob0 = prob0 * (float(Matrix_Var3[1][0]+1) / (Matrix_Var3[0][0]+Matrix_Var3[1][0]+2))

    if (int(test1[3]))==0:
        prob0 = prob0 * (float(Matrix_Var4[0][0]+1) / (Matrix_Var4[0][0]+Matrix_Var4[1][0]+2))
    if (int(test1[3]))==1:
        prob0 = prob0 * (float(Matrix_Var4[1][0]+1) / (Matrix_Var4[0][0]+Matrix_Var4[1][0]+2))

    if (int(test1[4]))==0:
        prob0 = prob0 * (float(Matrix_Var5[0][0]+1) / (Matrix_Var5[0][0]+Matrix_Var5[1][0]+2))
    if (int(test1[4]))==1:
        prob0 = prob0 * (float(Matrix_Var5[1][0]+1) / (Matrix_Var5[0][0]+Matrix_Var5[1][0]+2))

    if (int(test1[5]))==0:
        prob0 = prob0 * (float(Matrix_Var6[0][0]+1) / (Matrix_Var6[0][0]+Matrix_Var6[1][0]+2))
    if (int(test1[5]))==1:
        prob0 = prob0 * (float(Matrix_Var6[1][0]+1) / (Matrix_Var6[0][0]+Matrix_Var6[1][0]+2))

    if (int(test1[6]))==0:
        prob0 = prob0 * (float(Matrix_Var7[0][0]+1) / (Matrix_Var7[0][0]+Matrix_Var7[1][0]+2))
    if (int(test1[6]))==1:
        prob0 = prob0 * (float(Matrix_Var7[1][0]+1) / (Matrix_Var7[0][0]+Matrix_Var7[1][0]+2))

    if (int(test1[7]))==0:
        prob0 = prob0 * (float(Matrix_Var8[0][0]+1) / (Matrix_Var8[0][0]+Matrix_Var8[1][0]+2))
    if (int(test1[7]))==1:
        prob0 = prob0 * (float(Matrix_Var8[1][0]+1) / (Matrix_Var8[0][0]+Matrix_Var8[1][0]+2))


    # Calculate For Class 1
    prob1 = prior_probability_1

    if (int(test1[0]))==0:
        prob1 = prob1 * (float(Matrix_Var1[0][1]+1) / (Matrix_Var1[0][1]+Matrix_Var1[1][1]+2))
    if (int(test1[0]))==1:
        prob1 = prob1 * (float(Matrix_Var1[1][1]+1) / (Matrix_Var1[0][1]+Matrix_Var1[1][1]+2))

    if (int(test1[1]))==0:
        prob1 = prob1 * (float(Matrix_Var2[0][1]+1) / (Matrix_Var2[0][1]+Matrix_Var2[1][1]+2))
    if (int(test1[1]))==1:
        prob1 = prob1 * (float(Matrix_Var2[1][1]+1) / (Matrix_Var2[0][1]+Matrix_Var2[1][1]+2))

    if (int(test1[2]))==0:
        prob1 = prob1 * (float(Matrix_Var3[0][1]+1) / (Matrix_Var3[0][1]+Matrix_Var3[1][1]+2))
    if (int(test1[2]))==1:
        prob1 = prob1 * (float(Matrix_Var3[1][1]+1) / (Matrix_Var3[0][1]+Matrix_Var3[1][1]+2))

    if (int(test1[3]))==0:
        prob1 = prob1 * (float(Matrix_Var4[0][1]+1) / (Matrix_Var4[0][1]+Matrix_Var4[1][1]+2))
    if (int(test1[3]))==1:
        prob1 = prob1 * (float(Matrix_Var4[1][1]+1) / (Matrix_Var4[0][1]+Matrix_Var4[1][1]+2))

    if (int(test1[4]))==0:
        prob1 = prob1 * (float(Matrix_Var5[0][1]+1) / (Matrix_Var5[0][1]+Matrix_Var5[1][1]+2))
    if (int(test1[4]))==1:
        prob1 = prob1 * (float(Matrix_Var5[1][1]+1) / (Matrix_Var5[0][1]+Matrix_Var5[1][1]+2))

    if (int(test1[5]))==0:
        prob1 = prob1 * (float(Matrix_Var6[0][1]+1) / (Matrix_Var6[0][1]+Matrix_Var6[1][1]+2))
    if (int(test1[5]))==1:
        prob1 = prob1 * (float(Matrix_Var6[1][1]+1) / (Matrix_Var6[0][1]+Matrix_Var6[1][1]+2))

    if (int(test1[6]))==0:
        prob1 = prob1 * (float(Matrix_Var7[0][1]+1) / (Matrix_Var7[0][1]+Matrix_Var7[1][1]+2))
    if (int(test1[6]))==1:
        prob1 = prob1 * (float(Matrix_Var7[1][1]+1) / (Matrix_Var7[0][1]+Matrix_Var7[1][1]+2))

    if (int(test1[7]))==0:
        prob1 = prob1 * (float(Matrix_Var8[0][1]+1) / (Matrix_Var8[0][1]+Matrix_Var8[1][1]+2))
    if (int(test1[7]))==1:
        prob1 = prob1 * (float(Matrix_Var8[1][1]+1) / (Matrix_Var8[0][1]+Matrix_Var8[1][1]+2))


    if (prob0<prob1):
        test_results[i] = 1
    if (prob0>=prob1):
        test_results[i] = 0

#print(test_results)


with open('15EC10071_3.out','w') as file:
	for x in test_results:
		file.write(str(int(x)))
		file.write(" ")
file.close()