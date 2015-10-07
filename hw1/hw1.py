import numpy as np
import matplotlib.pyplot as plt

pathToData = './iris/iris.data'

'''
Attribute Information:
   1. sepal length in cm,2. sepal width in cm,3. petal length in cm,4. petal width in cm
   5. class: 1. Iris Setosa, 2. Iris Versicolour, 3. Iris Virginica
'''

listIrisData = []
setDatasl=[]
setDatasw=[]
setDatapl=[]
setDatapw = []
verDatasl=[]
verDatasw=[]
verDatapl=[]
verDatapw = []
virDatasl=[]
virDatasw=[]
virDatapl=[]
virDatapw = []

def parseData():
    with open(pathToData, 'r') as datafile:
        for line in datafile:
            temp = line.strip('\n').split(',')
            data = IrisData(temp[0], temp[1], temp[2], temp[3], temp[4])
            listIrisData.append(data)

def plotData( data0, data1 ):
    dataA, =plt.plot( data0[0], data1[0], 'ro' )
    dataB, =plt.plot( data0[1], data1[1], 'gx' )
    dataC, =plt.plot( data0[2], data1[2], 'b^' )
    plt.title( data0[3]+' VS '+data1[3] )
    plt.xlabel(data0[3])
    plt.ylabel(data1[3])
    plt.legend( [ dataA, dataB, dataC ], [ 'setosa', 'versicolor', 'virginica' ] )
    plt.show()

def sortData():
    for data in listIrisData:
        #print data.sepalLength
        if data.irisClass == 'Iris-setosa':
            setDatasl.append(data.sepalLength)
            setDatasw.append(data.sepalWidth)
            setDatapl.append(data.petalLength)
            setDatapw.append(data.petalWidth)
        elif data.irisClass == 'Iris-versicolor':
            verDatasl.append(data.sepalLength)
            verDatasw.append(data.sepalWidth)
            verDatapl.append(data.petalLength)
            verDatapw.append(data.petalWidth)
        elif data.irisClass == 'Iris-virginica':
            virDatasl.append(data.sepalLength)
            virDatasw.append(data.sepalWidth)
            virDatapl.append(data.petalLength)
            virDatapw.append(data.petalWidth)
#(x, y) = (sepal length, sepal width), (sepal length, petal length), (sepal length, petal width), (sepal width, petal length), (sepal width, petal width), (petal length, petal width)

def test(datax, datay):
    x = []
    y = []
    if datax == 'sepal length' and datay == 'sepal width':
        x.append(setDatasl)
        x.append(verDatasl)
        x.append(virDatasl)
        x.append('datax')
        y.append(setDatasw)
        y.append(verDatasw)
        y.append(virDatasw)
        y.append('datay')
        plotData(x, y)

class IrisData:
    count = 0
    def __init__(self, sepalLength, sepalWidth, petalLength, petalWidth, irisClass):
        self.sepalLength = sepalLength
        self.sepalWidth = sepalWidth
        self.petalLength = petalLength
        self.petalWidth = petalWidth
        self.irisClass = irisClass
        IrisData.count += 1

def main():
    parseData()
    sortData()
    test('sepal length', 'sepal width')
    #a = [1,2,3,'abc']
    #b = [2,2,2, 'cba']
    #plotData(a,b)

if __name__ == '__main__':
    main()