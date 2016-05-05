import pandas as pd
from sklearn.cross_validation import StratifiedKFold
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import zero_one_loss




## FILE modified from Katie's Song Classifier Assignment
## ------------------------------------------------------------------ ##
##                              Get the Data                          ##
## ------------------------------------------------------------------ ##

feature_vectors = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_features.csv')
labels = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_labels.csv')['0']

## separate into training and validation sets
k = 10
skf = StratifiedKFold(labels, n_folds=k)

## ------------------------------------------------------------------ ##
##                             Random Forrest                         ##
## ------------------------------------------------------------------ ##

## run SVC w linear kernel
average_error = 0
for train_index, test_index in skf:
  X_train, X_test = feature_vectors.iloc[train_index, :], feature_vectors.iloc[test_index, :]
  Y_train, Y_test = labels.iloc[train_index], labels.iloc[test_index]

  ## train svc
  print 'fitting random forest'
  rf = RandomForestClassifier()
  rf.fit(X_train, Y_train)

  ## predict
  predictions = rf.predict(X_test)
  error = zero_one_loss(predictions, Y_test)
  average_error += (1./k) * error

print "Random Forest Classifier: %4.2f%s" % (100 * average_error,'%')
print rf.feature_importances_

'''## ------------------------------------------------------------------ ##
##                       Cross Validation for SVC (poly)              ##
## ------------------------------------------------------------------ ##

## run SVC w polynomial kernel
average_error = 0
for train_index, test_index in skf:
  X_train, X_test = feature_vectors.iloc[:, train_index], feature_vectors.iloc[:, test_index]
  Y_train, Y_test = labels.iloc[train_index], labels.iloc[test_index]

  ## train svc
  svc = SVC(kernel='poly')
  svc.fit(X_train, Y_train)

  ## predict
  predictions = svc.prediction(X_test)
  error = zero_one_loss(predictions, Y_test)
  average_error += (1./k) * error

print "SVC w Polynomail Kernel Average Error: %4.2f%s" % (100 * averageError,'%')

## ------------------------------------------------------------------ ##
##                       Cross Validation for SVC (rbf)               ##
## ------------------------------------------------------------------ ##

## run SVC w rbf
average_error = 0
for train_index, test_index in skf:
  X_train, X_test = feature_vectors.iloc[:, train_index], feature_vectors.iloc[:, test_index]
  Y_train, Y_test = labels.iloc[train_index], labels.iloc[test_index]

  ## train svc
  svc = SVC(kernel='rbf')
  svc.fit(X_train, Y_train)

  ## predict
  predictions = svc.prediction(X_test)
  error = zero_one_loss(predictions, Y_test)
  average_error += (1./k) * error

print "SVC w RBF Kernel Average Error: %4.2f%s" % (100 * averageError,'%')


'''