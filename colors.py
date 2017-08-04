import numpy as np

file = open('data.csv', 'r')

r = []
g = []
b = []
c = []

line = file.readline()
for i in range(78):
	x = line.split(',')
	r.append(int(x[1][2:]))
	g.append(int(x[2]))
	b.append(int(x[3][: len(x[3]) - 2]))
	c.append(int(x[4][: len(x[4]) - 1]))
	line = file.readline()

X = []
for i in range(78):
	X.append([r[i],g[i],b[i]])


from sklearn.neighbors import KNeighborsClassifier as knc
knn = knc(n_neighbors = 12)
print knn.fit(X,c)
print knn.predict([[0,0,128]])
	


