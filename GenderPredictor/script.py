from sklearn import tree

#Classifier
clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43], [181, 50, 42], [181, 85, 43], [164, 56, 35], [178, 56, 40], [173, 57, 39] ]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male', 'female', 'female', 'female', 'female', 'female']


#creates a plot over the data
clf = clf.fit(X, Y)

#makes a prediction on out data and analyzes it
#through the plot to estimate a gender
prediction = clf.predict([[181, 65, 37]])

#Prints the prediciton
print(prediction)
