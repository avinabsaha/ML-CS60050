# Roll: 15EC10071
# Name: Avinab Saha
# Assignment number: 2
# Specific compilation/execution flags: None


import numpy as np

def entropy(labels):
    result = 0
    val, counts = np.unique(labels, return_counts=True)
    freqs = counts.astype('float')/len(labels)
    for p in freqs:
        if p != 0.0:
            result -= p * np.log2(p)
    return result

def info_gain(attribute_data,labels):
    result = entropy(labels)
    val, counts = np.unique(attribute_data, return_counts=True)
    freqs = counts.astype('float')/len(attribute_data)
    for p, v in zip(freqs, val):
        result -= p * entropy(labels[attribute_data == v])
    return result

def choose_best_attribute(data, labels, attributes):
		best_gain = -999999
		best_attribute = None
		for loop in range(0,len(attributes)):
			attribute_data = data[:, loop]
			gain = info_gain(attribute_data, labels)
			if gain > best_gain:
				best_gain = gain
				best_attribute = attributes[loop]
		return best_attribute

def choose_best_attribute_column(attributes,attribute):
	for loop in range(0,len(attributes)):
			if (attribute == attributes[loop]):
				return loop

def find_child_attribures(attributes,attribute):
	child_attributes = []
	for loop in range(0,len(attributes)):
			if attributes[loop] != attribute:
				child_attributes.append(attributes[loop])
	return child_attributes

def get_label(length,label):
	return np.ones(length) * label


class DecisionTree:

	def __init__(self, data, labels, attributes, max_level, old_level,value,parent,children):
		self.level = old_level + 1
		self.max_level = max_level		
		self.attribute_value = value
		self.parent = parent
		self.children = children
		all_same = True
		reference = labels[0]
		for loop in range(1,len(labels)):
			if (labels[loop]!=reference):
				all_same = False
				break
		if(all_same == True):
			self.label = labels[0]
			return
		self.build(data, labels, attributes)
		return

	def build(self, data, labels, attributes):
		self.attribute = choose_best_attribute(data, labels, attributes)
		best_attribute_column = choose_best_attribute_column(attributes,self.attribute)
		attribute_data = data[:, best_attribute_column]
		child_attributes = find_child_attribures(attributes,self.attribute)
		self.children = []
		for val in np.unique(attribute_data):
			child_data = np.delete(data[attribute_data == val,:], best_attribute_column,1)
			child_labels = labels[attribute_data == val]
			self.children.append(DecisionTree(child_data, child_labels, child_attributes,self.max_level,self.level,val,self,None))
	
	def classify(self, data):
		if len(data.shape) == 1:
			data = np.reshape(data, (1,len(data)))
		if self.children is None:
			return get_label(len(data),self.label)
		labels = np.zeros(len(data))
		for child in self.children:
			child_attr_index = data[:,self.attribute] == child.attribute_value
			labels[child_attr_index ] = child.classify(data[child_attr_index])
		return labels

# Reading number of Training Examples
with open('data2.csv') as file:
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
with open('data2.csv') as file:
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
with open('test2.csv') as file:
    line_count=0
    for line in file:    
        line_count = line_count+1

# Defining Data Matrix
w1 = 8
h = line_count
Test_Data = np.zeros(shape=(h,w1))

# Reading the Test Data Provided
with open('test2.csv') as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(8):
                Test_Data[line_count][i] = line[i]
    
        line_count = line_count+1

attributes  = list(range(len(Training_Data[0])))
tree = DecisionTree(Training_Data, Training_Label, attributes, 8, 0,None, None, None)
y = tree.classify(Test_Data)
with open('15EC10071_2.out','w') as file:
	for x in y:
		file.write(str(int(x)))
		file.write(" ")
file.close()