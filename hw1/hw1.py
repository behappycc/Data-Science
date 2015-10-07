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
    dataA, =plt.plot( data0[0][0], data1[0][0], 'ro' )
    dataB, =plt.plot( data0[0][1], data1[0][1], 'gx' )
    dataC, =plt.plot( data0[0][2], data1[0][2], 'b^' )
    plt.title( data0[0][3]+' VS '+data1[0][3] )
    plt.xlabel(data0[0][3])
    plt.ylabel(data1[0][3])
    plt.legend( [ dataA, dataB, dataC ], [ 'setosa', 'versicolor', 'virginica' ] )
    plt.show()

def sortData():
    for data in listIrisData:
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

def test(datax, datay):
    x = []
    y = []
    if datax == 'sepal_length' and datay == 'sepal_width':
        x.append([setDatasl, verDatasl, virDatasl, datax])
        y.append([setDatasw,verDatasw, virDatasw, datay])
        plotData(x, y)
    elif datax == 'sepal_length' and datay == 'petal_length':
        x.append([setDatasl, verDatasl, virDatasl, datax])
        y.append([setDatapl,verDatapl, virDatapl, datay])
        plotData(x, y)
    elif datax == 'sepal_length' and datay == 'petal_width':
        x.append([setDatasl, verDatasl, virDatasl, datax])
        y.append([setDatapw,verDatapw, virDatapw, datay])
        plotData(x, y)
    elif datax == 'sepal_width' and datay == 'petal_length':
        x.append([setDatasw, verDatasw, virDatasw, datax])
        y.append([setDatapl,verDatapl, virDatapl, datay])
        plotData(x, y)
    elif datax == 'sepal_width' and datay == 'petal_width':
        x.append([setDatasw, verDatasw, virDatasw, datax])
        y.append([setDatapw,verDatapw, virDatapw, datay])
        plotData(x, y)
    elif datax == 'petal_length' and datay == 'petal_width':
        x.append([setDatapl, verDatapl, virDatapl, datax])
        y.append([setDatapw,verDatapw, virDatapw, datay])
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
    test('sepal_length', 'sepal_width')
    test('sepal_length', 'petal_length')
    test('sepal_length', 'petal_width')
    test('sepal_width', 'petal_length')
    test('sepal_width', 'petal_width')
    test('petal_length', 'petal_width')

if __name__ == '__main__':
    main()