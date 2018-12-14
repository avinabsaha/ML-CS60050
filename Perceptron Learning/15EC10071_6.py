# Name: Avinab Saha
# Roll: 15EC10071
# Assignment 6 -ML-CS60050
# No Special Compilation Flags


import numpy as np

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_derivative(x):
    return (x)*(1.0-(x))

# Reading number of Training Examples
with open('data6.csv') as file:
    line_count=0
    for line in file:    
        line_count = line_count+1

# Defining Data Matrix
w1 = 8
w2 = 1
h = line_count
Training_Data = np.zeros(shape=(h,w1))
Training_Label = np.zeros(h)

# Reading the Training Data Provided
with open('data6.csv') as file:
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

# Reading number of Training ETraining_Dataamples
with open('test6.csv') as file:
    line_count=0
    for line in file:    
        line_count = line_count+1

# Defining Data Matrix
w1 = 8
h = line_count
Test_Data = np.zeros(shape=(h,w1))

# Reading the Test Data Provided
with open('test6.csv') as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(8):
                Test_Data[line_count][i] = line[i]
        line_count = line_count+1

#weight_vector = [0.40600947,0.94565282,0.12740792,0.48801408,0.11202948,0.75026382,0.37335255,0.21869728,0.37544188]
weight_vector = np.zeros(w1+1)
for loop in range(w1+1):
    weight_vector[loop]= np.random.random_sample()

for epoch in range(1000):
    #print(weight_vector)
    count=0
    error=0
    deltas = np.zeros(w1+1)
    for val in range(Training_Data.shape[0]):
        row_val = Training_Data[val,:]
        #print(row_val)
        output = weight_vector[0]+ np.dot(weight_vector[1:],row_val)
        output = sigmoid(output)
        #error = error + 0.5*(Training_Label[val]-output)*(Training_Label[val]-output)
        deltas[0]= deltas[0]+ 0.1* (Training_Label[val]-output)*1* sigmoid_derivative(output)
        for loop2 in range(1,9):
            deltas[loop2]= deltas[loop2]+ 0.1* (Training_Label[val]-output)* row_val[loop2-1]*sigmoid_derivative(output)
    # Update after each epoch
    weight_vector[0]= weight_vector[0]+ deltas[0]
    for loop2 in range(1,9):
        weight_vector[loop2]= weight_vector[loop2]+ deltas[loop2]
    #print(error)
    #print(weight_vector)
#print(weight_vector)
"""
for val in range(Training_Data.shape[0]):
    row_val = Training_Data[val,:]
    output = weight_vector[0]+ np.dot(weight_vector[1:],row_val)
    output = sigmoid(output)
    if (output>=0.5):
        output = 1
    if (output<0.5):
        output = 0
    #print(output,int(Training_Label[val]))
"""

test_results= np.zeros(Test_Data.shape[0])
for val in range(Test_Data.shape[0]):
    row_val = Test_Data[val,:]
    output = weight_vector[0]+ np.dot(weight_vector[1:],row_val)
    output = sigmoid(output)
    if (output>=0.5):
        output=1
    if (output<0.5):
        output = 0
    test_results[val]=output

#print(test_results)
with open('15EC10071_6.out','w') as file:
	for x in test_results:
		file.write(str(int(x)))
		file.write(" ")
file.close()
