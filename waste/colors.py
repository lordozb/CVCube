import numpy as np

def colors(x1, x2, x3):

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
	knn.fit(X,c)
	x = np.array([x1,x2,x3])	
	keyval = {0:'white',1:'black',2:'red',3:'green',4:'blue',5:'yellow',6:'cyan',7:'purple',8:'pink',9:'brown',10:'grey',11:'orange'}
	ans = knn.predict([x])
	return keyval[ans[0]]


