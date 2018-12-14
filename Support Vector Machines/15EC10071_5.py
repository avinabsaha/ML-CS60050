import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.svm import SVC

def load_train_data():
	with open('spambase.data','r') as f:
		data = []
		for l in f.readlines():
			data.append([float(x) for x in l.strip('\r\n').split(',')])
	f.close()
	return np.array(data)

data = load_train_data()
print(data.shape)

x= data[:,:len(data[0])-1]
y = data[:,-1]


# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)
length_of_training_data = len(y_train)
length_of_test_data = len(y_test)



# Linear Kernel
for i in np.arange(0.000,0.05,0.001):
    c= i+0.001
    linear_model = SVC(kernel='linear', C=c) 
    linear_model.fit(X_train, y_train)
    predicted= linear_model.predict(X_train)
    correct = np.sum(predicted == y_train)
    #print("Value of C:"),
    print(c),
    #print("Train Accuracy:"),
    print(100*float(correct)/length_of_training_data),
    predicted_test= linear_model.predict(X_test)
    correct_test = np.sum(predicted_test == y_test)
    #print("       Test Accuracy"),
    print(100*float(correct_test)/length_of_test_data)

# Quadratic Kernel
for i in np.arange(0.000,0.05,0.001):
    c= i+0.001
    quadratic_model = SVC(kernel='poly', C=c,degree=2) 
    quadratic_model.fit(X_train, y_train)
    predicted= quadratic_model.predict(X_train)
    correct = np.sum(predicted == y_train)
    #print("Value of C:"),
    print(c),
    #print("Train Accuracy:"),
    print(100*float(correct)/length_of_training_data),
    predicted_test= quadratic_model.predict(X_test)
    correct_test = np.sum(predicted_test == y_test)
    #print("       Test Accuracy"),
    print(100*float(correct_test)/length_of_test_data)



# RBF Kernel
for i in range(1,200):
    c= float(i)/2.0
    rbf_model = SVC(kernel='rbf', C=c) 
    rbf_model.fit(X_train, y_train)
    predicted= rbf_model.predict(X_train)
    correct = np.sum(predicted == y_train)
    #print("Value of C:"),
    print(c),
    #print("Train Accuracy:"),
    print(100*float(correct)/length_of_training_data),
    predicted_test= rbf_model.predict(X_test)
    correct_test = np.sum(predicted_test == y_test)
    #print("       Test Accuracy"),
    print(100*float(correct_test)/length_of_test_data)

