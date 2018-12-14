# Roll               : 15EC10071
# Name               : Avinab Saha
# Assignment Number  : 1
# Flags              : python3 15EC10071_1.py <datafile.csv>

# import necessary package
import sys

count = len(sys.argv)
if (count!=2):
    print("Please use correct format: python3 <code filename> <data filename>")
    sys.exit(0)


# Defining Data Matrix
w, h = 9, 20
Matrix = [[0 for x in range(w)] for y in range(h)] 

# Read the CSV File line-by-line
with open(sys.argv[1]) as file:
    line_count=0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for i in range(9):
            Matrix[line_count][i]=line[i]
    
        line_count = line_count+1

# Count Number of 1's
noOfOnes = 0
for i in range(20):
    if (Matrix[i][8]=='1'):
        noOfOnes = noOfOnes+1

# Defining Final Data Matrix
w, h = 9, noOfOnes
Matrix2 = [[0 for x in range(w)] for y in range(h)] 

# Copy To Final Data Matrix
rowCount = 0
for i in range (20):
    if (Matrix[i][8]=='0'):
        continue
    else:
        for j in range(9):
            Matrix2[rowCount][j]=Matrix[i][j]
        rowCount = rowCount+1

# Array to Store Status of all the Variables & Make them all zero
w = 8
Status = [0 for x in range(w)]
for i in range(8): 
    Status[i] = 0

for i in range(8):
    initial  = Matrix2[0][i]
    flag = 1
    for j in range(noOfOnes):
        if(initial!= Matrix2[j][i]):
            flag = 0
    if (flag==1):
        if(initial=='1'):
            Status[i] = 1
        else:
            Status[i] = -1

# Count Number of Non Zero Elements
countNonZero = 0;
for i in range(8):
    if(Status[i]!=0):
        countNonZero = countNonZero+1

# Formatted Output
print(countNonZero,end = "")
print(",",end = "")
countNow = 0
for i in range(8):
    if(Status[i] == 1):
        print(i+1,end = "")
        countNow = countNow + 1
        if (countNow!= countNonZero):
            print(",", end = "")
        if (countNow == countNonZero):
            print()
    if(Status[i] == -1):
        print((i+1)*-1,end = "")
        countNow = countNow + 1
        if (countNow!= countNonZero):
            print(",", end = "")
        if (countNow == countNonZero):
            print()  