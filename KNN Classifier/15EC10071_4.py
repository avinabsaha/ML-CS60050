# Roll: 15EC10071
# Name: Avinab Saha
# Assignment number: 4
# Specific compilation/execution flags: None
import numpy as np

def get_euclidean_distance(Test,Training):
    sum = 0
    for i in range(8):
        sum = sum+ (float(Test[i])-float(Training[i]))*(float(Test[i])-float(Training[i]))
    return sum
    
# Reading number of Training Examples
with open('data4.csv') as file:
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
with open('data4.csv') as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(5):
            if i<4:
                Training_Data[line_count][i] = line[i]
            else:
                Training_Label[line_count] = line[i]
    
        line_count = line_count+1

# Reading number of Test Examples
with open('test4.csv') as file:
    line_count=0
    for line in file:    
        line_count = line_count+1

# Defining Data Matrix
w1 = 8
h = line_count
Test_Data = np.zeros(shape=(h,w1))
length_of_test_Data = h

# Reading the Test Data Provided
with open('test4.csv') as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(4):
                Test_Data[line_count][i] = line[i]
    
        line_count = line_count+1


# Training phase
# Saved Data acts as trained model
#print(Training_Label)

results = np.zeros(length_of_test_Data,dtype=int)
# Test phase
for i in range(length_of_test_Data):
    euclidean_array = np.zeros(length_of_training_set,dtype=float)
    for j in range(length_of_training_set):
        euclidean_array[j] = get_euclidean_distance(Test_Data[i,:],Training_Data[j,:])
    #print(euclidean_array)
    top_5 = np.argpartition(euclidean_array,5)[:5]
    #print(top_5)
    top_5_labels = [float(Training_Label[k]) for k in top_5]
    #print(top_5_labels)
    results[i] = np.bincount(top_5_labels).argmax()

with open('15EC10071_4.out','w') as file:
	for x in results:
		file.write(str(int(x)))
		file.write(" ")
file.close()