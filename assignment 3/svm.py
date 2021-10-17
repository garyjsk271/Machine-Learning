#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #3
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import svm
from sklearn import metrics
import csv

dbTest = []
X_training = []
Y_training = []
X_test = []
Y_test = []
C = [1, 5, 10, 100]
degrees = [1, 2, 3]
kernels = ["linear", "poly", "rbf"]
decision_function_shapes = ["ovo", "ovr"]
highestAccuracy = 0

#reading the data in a csv file
with open('optdigits.tra', 'r') as trainingFile:
  reader = csv.reader(trainingFile)
  for i, row in enumerate(reader):
      X_training.append(row[:-1])
      Y_training.append(row[-1])

#reading the data in a csv file
with open('optdigits.tes', 'r') as testingFile:
  reader = csv.reader(testingFile)
  for i, row in enumerate(reader):
      dbTest.append(row)
      X_test.append( row[:-1] )
      Y_test.append( int(row[-1]) )

#created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
maxAccuracy = 0.0
for c in C: #iterates over c
    for degree in degrees: #iterates over degree
        for kernel in kernels: #iterates kernel
           for shape in decision_function_shapes: #iterates over decision_function_shape

                #Create an SVM classifier that will test all combinations of c, degree, kernel, and decision_function_shape as hyperparameters. For instance svm.SVC(c=1)
                clf = svm.SVC(C = c, kernel = kernel, degree = degree, decision_function_shape = shape)

                #Fit SVM to the training data
                clf.fit(X_training, Y_training)

                #make the classifier prediction for each test sample and start computing its accuracy
                Y_predicted = []
                for testSample in X_test:
                    class_predicted = int( clf.predict( [testSample] )[0] )
                    Y_predicted.append(class_predicted)
                #check if the calculated accuracy is higher than the previously one calculated. If so, update update the highest accuracy and print it together with the SVM hyperparameters
                #Example: "Highest SVM accuracy so far: 0.92, Parameters: a=1, degree=2, kernel= poly, decision_function_shape = 'ovo'"
                accuracy = metrics.accuracy_score(Y_test, Y_predicted)
                if accuracy > maxAccuracy:
                    maxAccuracy = accuracy
                    print("Highest SVM accuracy so far: {:.4f}, Parameters: c={}, degree={}, kernel={}, decision_function_shape={}"\
                          .format(maxAccuracy, c, degree, kernel, shape) )











