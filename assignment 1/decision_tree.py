#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
ageToInt =  { 
    "Young" : 1,
    "Prepresbyopic" : 2, 
    "Presbyopic" : 3 
}

spectaclePrescriptionToInt = { 
    "Myope" : 1, 
    "Hypermetrope" : 2 
}

astigmatismToInt = { 
    "Yes" : 1, 
    "No" : 2 
}

tearProductionRateToInt = { 
    "Reduced" : 1, 
    "Normal" : 2 
}

for data in db:
    data[0] = ageToInt[data[0]]
    data[1] = spectaclePrescriptionToInt[data[1]]
    data[2] = astigmatismToInt[data[2]]
    data[3] = tearProductionRateToInt[data[3]]
    X.append(data[:len(data) - 1] )

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
for data in db:
    Y.append(1 if data[-1] == "Yes" else 2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()